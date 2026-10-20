from collections import Counter

import rdflib
from pyshacl import validate
from rdflib.namespace import SH

from utility import config

SHAPES = '''
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix :   <SCHEMA_IRI> .

:DegreeShape a sh:NodeShape ;
    sh:targetClass :Degree ;

    # Degrees referenced but not in the dataset have no title
    sh:property [
        sh:path :hasTitle ;
        sh:minCount 1 ;
        sh:message "Degree is referenced but not in the dataset" ;
    ] ;

    # degree must have at least one major
    sh:property [
        sh:path :hasMajor ;
        sh:minCount 1 ;
        sh:message "Degree has no majors" ;
    ] ;
    
    sh:sparql [
        sh:message "Degree has no study type" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this WHERE {
                $this :hasTitle ?t .
                FILTER NOT EXISTS { $this :hasStudyType ?s }
            }
        """ ;
    ] ;

    sh:sparql [
        sh:message "Degree has no total points" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this WHERE {
                $this :hasTitle ?t .
                FILTER NOT EXISTS { $this :hasTotalPoints ?p }
            }
        """ ;
    ] ;

    sh:sparql [
        sh:message "Combined degree includes a degree that is not in the dataset" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this ?value WHERE {
                $this :includesDegree ?value .
                FILTER NOT EXISTS { ?value :hasTitle ?t }
            }
        """ ;
    ] .

:MajorShape a sh:NodeShape ;
    sh:targetClass :Major ;

    sh:property [
        sh:path :hasUnit ;
        sh:minCount 1 ;
        sh:message "Major has no units" ;
    ] ;

    sh:sparql [
        sh:message "Major has more than 48 credit points at level 1" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this (SUM(?credit) AS ?value) WHERE {
                $this :hasUnit ?unit .
                ?unit :hasLevel 1 ;
                      :hasCredit ?credit .
            }
            GROUP BY $this
            HAVING (SUM(?credit) > 48)
        """ ;
    ] ;

    sh:sparql [
        sh:message "Major has no level 3 units (no capstone level)" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this WHERE {
                $this :hasUnit ?any .
                FILTER NOT EXISTS { $this :hasUnit ?u . ?u :hasLevel 3 }
            }
        """ ;
    ] .
  :UnitShape a sh:NodeShape ;
    sh:targetClass :Unit ;

    # Units referenced but not in the dataset (FloatingUnits) have no title
    sh:property [
        sh:path :hasTitle ;
        sh:minCount 1 ;
        sh:message "Unit is referenced but not in the dataset" ;
    ] ;

    # A unit can't be its own prerequisite.
    sh:sparql [
        sh:message "Unit is its own prerequisite (directly or through a cycle)" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this WHERE { $this :hasPrerequisite $this . }
        """ ;
    ] ;

    sh:sparql [
        sh:message "Unit has no credit points" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this WHERE {
                $this :hasTitle ?t .
                FILTER NOT EXISTS { $this :hasCredit ?c }
            }
        """ ;
    ] ;

    sh:sparql [
        sh:message "Unit has no level" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this WHERE {
                $this :hasTitle ?t .
                FILTER NOT EXISTS { $this :hasLevel ?l }
            }
        """ ;
    ] ;

    sh:sparql [
        sh:message "Unit level is outside 1-9" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this ?value WHERE {
                $this :hasLevel ?value .
                FILTER(?value < 1 || ?value > 9)
            }
        """ ;
    ] ;

    sh:sparql [
        sh:message "Unit has no outcomes" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this WHERE {
                $this :hasTitle ?t .
                FILTER NOT EXISTS { $this :hasOutcome ?o }
            }
        """ ;
    ] ;

    sh:sparql [
        sh:message "Unit requires (directly or indirectly) a unit that is not in the dataset" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this ?value WHERE {
                $this :hasTitle ?t ;
                      :hasPrerequisite ?value .
                ?value a :FloatingUnit .
            }
        """ ;
    ] .
'''.replace("SCHEMA_IRI", config.SCHEMA_IRI)


def check(world):
    data = rdflib.Graph()
    for triple in world.as_rdflib_graph():       
        data.add(triple)

    shapes = rdflib.Graph().parse(data=SHAPES, format="turtle")
    conforms, results, report = validate(data, shacl_graph=shapes, inference="rdfs")

    summary = Counter(str(m) for m in results.objects(None, SH.resultMessage))
    return conforms, summary, report
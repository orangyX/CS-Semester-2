from collections import Counter

import rdflib
from pyshacl import validate
from rdflib.namespace import SH

from utility import config

SHAPES = '''
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix :   <SCHEMA_IRI> .

# RULE 3 - a degree must have at least one major
# Every degree must exist in the dataset and have at least one major
:DegreeShape a sh:NodeShape ;
    sh:targetClass :Degree ;

    # Degrees referenced but not in the dataset have no title
    sh:property [
        sh:path :hasTitle ;
        sh:minCount 1 ;
        sh:message "Degree is referenced but not in the dataset" ;
    ] ;

    # RULE 3 - a degree must have at least one major
    sh:property [
        sh:path :hasMajor ;
        sh:minCount 1 ;
        sh:message "Degree has no majors" ;
    ] .

:UnitShape a sh:NodeShape ;
    sh:targetClass :Unit ;

    # Units referenced but not in the dataset (FloatingUnits) have no title
    sh:property [
        sh:path :hasTitle ;
        sh:minCount 1 ;
        sh:message "Unit is referenced but not in the dataset" ;
    ] ;

    # RULE 1 - a unit can't be its own prerequisite.
    # After reasoning, hasPrerequisite is transitive, so this also catches cycles.
    sh:sparql [
        sh:message "Unit is its own prerequisite (directly or through a cycle)" ;
        sh:select """
            PREFIX : <SCHEMA_IRI>
            SELECT $this WHERE { $this :hasPrerequisite $this . }
        """ ;
    ] .

# RULE 6 - no major over 48 credit points at level 1
:MajorShape a sh:NodeShape ;
    sh:targetClass :Major ;
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
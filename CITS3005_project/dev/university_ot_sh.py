from pyshacl import validate
from rdflib import Graph
from pathlib import Path
from university_ot import w, onto

# "@prefix sh: <http://www.w3.org/ns/shacl#>" # These will need to be re-integrated in later. turtle will complain
# "@prefix xsd: <http://www.w3.org/2001/XMLSchema#>"
# "@prefix : <http://uwa/uni.ot#>"

ot_data = w.as_rdflib_graph() # Transform the world into a graph (rdflib)
ot_graph = Graph()
sh_graph = Graph()

for s, p, o in ot_data: # Copy over otherwise class incompatibility forces error (debug w/ Claude)
    ot_graph.add((s, p, o))

print(f"Successfully loaded ot_graph with {len(ot_graph)} triples")

# The shape describes the following constraints:
    # - degreeCode, degreeTitle, degreeCreditsToComplete, degreeFullTimeDuration are functional properties
    # - degree has at least one school
    # - degree requires min. 144 credits to complete, max. 240 credits to complete
    # - degree has min. full time duration of 3 years, max. duration of 5 years
    # - degree has at least one location (available in)
    # - degree has at least one major
degree_sh = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://uwa/uni.ot#> .
:DegreeShape a sh:NodeShape ;
    sh:targetClass :Degree ;

    sh:property [
        sh:path :degreeCode ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string
    ] ;

    sh:property [
        sh:path :degreeTitle ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string
    ] ;

    sh:property [
        sh:path :degreeSchool ;
        sh:minCount 1 ;
        sh:class :School ;
    ] ;

    sh:property [
        sh:path :degreeCreditsToComplete ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:minInclusive 144 ;
        sh:maxInclusive 240 ;
        sh:datatype xsd:integer
    ] ;

    sh:property [
        sh:path :degreeFullTimeDuration ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:minInclusive 3 ;
        sh:maxInclusive 5 ;
        sh:datatype xsd:integer
    ] ;

    sh:property [
        sh:path :degreeLocation ;
        sh:minCount 1 ;
        sh:class :Location
    ] ;

    sh:property [
        sh:path :degreeHasMajor ;
        sh:minCount 1 ;
        sh:class :Major
    ] .
"""

# A unit cannot be its own prerequisite; a prerequisite of a prerequisite is a prerequisite (irreflexivity and transitivity already applied, left as a stub for now)

# No major should exceed 48 credits at level 1

# Instructions on defining a shape:
    # 1. add the required prefixes (as demonstrated above)
    # 2. declare the shape name (usually just NameShape) to a sh:NodeShape
    # 3. declare the target class
    # 4. assign properties as required
# Documentation: https://www.w3.org/TR/shacl/#introduction

sh_graph.parse(data=degree_sh, format="turtle")

result = validate(ot_graph, shacl_graph=sh_graph)

for r in result:
    print(r)
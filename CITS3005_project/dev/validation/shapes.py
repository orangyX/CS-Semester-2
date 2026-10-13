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

major_sh = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://uwa/uni.ot#> .
:MajorShape a sh:NodeShape ;
    sh:targetClass :Major ;

    sh:property [
        sh:path :majorCode ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string
    ] ;

    sh:property [
        sh:path :majorTitle ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype
    ] ;

    sh:property [
        sh:path :majorSchool ;
        sh:minCount 1 ;
        sh:class :School
    ] ;

    sh:property [
        sh:path :majorDescription ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string 
    ] ;

    sh:property [
        sh:path :majorOutcomes ;
        sh:minCount 1 ;
        sh:datatype xsd:string
    ] ;

"""

# NOT DONE: ADD CREDIT RESTRICTION FOR LEVEL 1 MAJOR

unit_sh = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://uwa/uni.ot#> .
:UnitShape a sh:NodeShape ;
    sh:targetClass :Unit ;

    sh:property [
        sh:path :unitCode ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string
    ] ;

    sh:property [
        sh:path :unitTitle ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string
    ] ;

    sh:property [
        sh:path :unitSchool ;
        sh:minCount 1 ;
        sh:class :School
    ] ;

    sh:property [
        sh:path :unitLevel ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:minInclusive 1 ;
        sh:maxInclusive 5 ;
        sh:datatype xsd:integer 
    ] ;

    sh:property [
        
    ]
"""
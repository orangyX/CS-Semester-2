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
    ] ;

    sh:property [
        sh:path :degreeStudyType ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:class :StudyType
    ] .
"""

cb_degree_sh = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://uwa/uni.ot#> .
:CombinedBachelorShape a sh:NodeShape ;
    sh:targetClass :CombinedBachelor ;

    sh:property [
        sh:path :combinedBachelorIncludes ;
        sh:minCount 2 ;
        sh:maxCount 2 ;
        sh:class :Degree
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
        sh:datatype xsd:string
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

    sh:property [
        sh:path :majorBridgingUnits ;
        sh:minCount 0 ;
        sh:class :Unit
    ] .

"""

# NOT DONE: ADD CREDIT RESTRICTION FOR LEVEL 1 MAJOR

unit_sh = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://uwa/uni.ot#> .
:UnitShape a sh:NodeShape ;
    sh:targetClass :Unit ;

    sh:not [
        sh:class :FloatingUnit
    ] ;

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
        sh:path :unitDescription ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string
    ] ;

    sh:property [
        sh:path :unitAwardsCredits ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:minInclusive 0 ;
        sh:maxInclusive 24 ;
        sh:datatype xsd:integer
    ] ;

    sh:property [
        sh:path :unitSemesterAvailability ;
        sh:minCount 1 ;
        sh:datatype xsd:string
    ] ;

    sh:property [
        sh:path :unitLocation ;
        sh:minCount 1 ;
        sh:class :Location
    ] ;

    sh:property [
        sh:path :unitOutcomes ;
        sh:minCount 1 ;
        sh:datatype xsd:string
    ] ;
    
    sh:property [
        sh:path :unitAssessmentTypes ;
        sh:minCount 1 ;
        sh:datatype xsd:string
    ] ;

    sh:property [
        sh:path :unitContactTypes ;
        sh:minCount 1 ;
        sh:class :ContactMode
    ] ;

    sh:property [
        sh:path :unitHasPrerequisite ;
        sh:class :Unit
    ] ;

    sh:property [
        sh:path :unitIsPrerequisiteOf ;
        sh:class :Unit 
    ] ;

    sh:property [
        sh:path :unitIsCoreInMajor ;
        sh:class :Major
    ] .
"""
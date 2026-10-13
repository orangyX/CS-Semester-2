# This file literally just stores the test blocks; copy and paste this stuff back in if you need test specific components that were before tested

# SWRL Rule testing
# BE_Hons = Degree("BE_Hons")
# BsC = Degree("BsC")

# MechEng = Major("MechEng")
# CompSci = Major("CompSci")

# BE_Hons.degreeHasMajor = [MechEng]
# BsC.degreeHasMajor = [CompSci]

# BE_BsC = Degree("BE_BsC")

# BE_BsC.combinedDegreeIncludes = [BE_Hons, BsC]

# cits2200 = Unit("DataStructuresAndAlgorithms")
# cits2200.unitOutcomes = ["DSA"]

# CompSci.majorHasCoreUnit = [cits2200]

# TEST SWRL RULE: any degree with a major -> major is in philosophy
# bsc = Degree("BP004")
# cmp_sc = Major("MJD_CMPSCI")

# bsc.degreeHasStudyType = [bachelor]
# bsc.degreeHasMajor = [cmp_sc]
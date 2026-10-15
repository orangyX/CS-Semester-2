from owlready2 import Imp

major_is_in_philosophy_rule = Imp().set_as_rule(
    "degreeHasMajor(?d, ?m), degreeStudyType(?d, ?s), StudyType("Bachelorscourse") -> degreeHasMajor("BH005", ?m)"
)
variable (M S A E C L : Prop)

theorem alarm (h₁ : (M ∨ S) → A) (h₂ : A → E) (h₃ : (E ∧ C) → L) :
    ((M ∨ S) ∧ C) → L :=
    fun h₄ =>
        have hMS : M ∨ S ;+

variable (p q r s : Prop)

theorem t2 (h₁ : q → r) (h₂ : p → q) : p → r :=
    fun h₃ : p => show r from h₁ (h₂ h₃)

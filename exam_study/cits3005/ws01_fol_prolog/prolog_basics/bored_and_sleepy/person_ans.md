# F2

## F2(a) question
Give one model of P, the set of atoms.

### F3(a) answer
| Clause | Meaning | True unless |
| :--- | :--- | :--- |
| awake; sleeping :- person. | person if awake or sleeping | awake and not sleeping false |
| sleeping; young :- bored. | bored if sleeping and young | not sleeping and not young |
| bored :- old | if old, then bored | not old |
| :- young, old | not (young and old) | both true |
| :- awake, sleeping | not (awake and sleeping) | both true |
| awake. | awake | awake false |

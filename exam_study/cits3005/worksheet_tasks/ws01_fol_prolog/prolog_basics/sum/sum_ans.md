# E6

## E6(a) question
What does ?- sum([3,1,4], N). return, and in what order are the additions performed?

### E6(a) answer
| Step | List | Sum |
| :--- | :--- | :--- |
| 1 | sum([3, 1, 4], N) | 0 |
| 2 | sum([1, 4], N) | 0 |
| 3 | sum([4], N) | 0 |
| 4 | sum([], 0) | 0 |
| 5 | sum([4], M (0)) | M is 0 + 4 |
| 6 | sum([1, 4], M (4)) | M is 4 + 1 |
| 7 | sum(3, 1, 4), M(5) | N is M + 3 |

Yield N = 8

## E6(b) question
What happens with ?- sum(L, 8)., and why?

### E6(b) answer
Following error is yielded:
```
ERROR: Arguments are not sufficiently instantiated
ERROR: In:
ERROR:   [13] 8 is 0+_15116
ERROR:   [12] sum([_15146],8) at c:/users/jaxma/exam_study/cits3005/ws01_fol_prolog/prolog_basics/sum/sum.pl:1
ERROR:   [11] toplevel_call(user:user: ...) at c:/program files/swipl/boot/toplevel.pl:1529
   Exception: (13) 8 is 0+_3288 ? creep
   Exception: (12) sum(_1674, 8) ? creep
```

* First clause: failure
* Second clause: sum(M, T); T unbounded, succeeding with T = [], M = 0
    * Reaches 8 is 0+H; H not bounded
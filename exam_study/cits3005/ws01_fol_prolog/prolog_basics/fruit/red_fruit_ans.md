# E2
## b.
Give every answer, in order, to ?- redFruit(X). and to ?- red(X). (pressing ; each time).

### E2(b)
Steps. 
?- red(X).
X = apple;
X = tomato.

?- redFruit(X).
    fruit(X). % X = apple
    red(apple).
X = apple.

## c.
?- redFruit(tomato). answers false. What does that false actually mean?

### E2(c)
'false' means that red(tomato) is not provable from the knowledge base.
* fruit(tomato) is absent
* prolog operates under the closed-world assumption; anything it is unable to prove is false

## d.
SWI-Prolog prints a warning when it loads exactly this file. What is it, and how do you silence it properly?

### E2(d)
```
Warning: c:/users/jaxma/exam_study/cits3005/ws01_fol_prolog/prolog_basics/red_fruit.pl:3:
Warning:    Clauses of red/1 are not together in the source-file
Warning:    Earlier definition at c:/users/jaxma/exam_study/cits3005/ws01_fol_prolog/prolog_basics/red_fruit.pl:1
Warning:    Current predicate: green/1
Warning:    Use :- discontiguous red/1. to suppress this message
```

Warning: red/1 are not grouped together, since green/1 sits between both.
* Resolvent: group red/1 clauses.
* Other case resolvent: if exists another green clause, the above fix should also be applied.
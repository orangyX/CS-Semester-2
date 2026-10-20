parent(david, john).
parent(jim, david).
parent(alice, jim).
parent(lily, alice).

ancestor(A, B) :- parent(A, X), ancestor(X, B).
ancestor(A, B) :- parent(A, B).
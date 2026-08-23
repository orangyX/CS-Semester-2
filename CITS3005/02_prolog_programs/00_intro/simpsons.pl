parent(marge, maggy).
parent(marge, bart).
parent(marge, lisa).
parent(homer, maggy).
parent(homer, bart).
parent(homer, lisa).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

related(X, Y) :-
    sibling(X, Y);
    parent(X, Y);
    parent(Y, X),
    X \= Y.
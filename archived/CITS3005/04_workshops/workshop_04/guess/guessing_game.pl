play :- random(1, 100, R),
    write("Guess int between 1 to 99: "),
    read(X),
    check(R, X),
    loop(R).

loop(R) :-
    read(X),
    number(X),
    check(R, X).

check(R, X) :- X < R,
    write("Low"),
    loop(R).

check(R, X) :- X > R,
    write("High"),
    loop(R).

check(R, X) :- X == R,
    write("Good").
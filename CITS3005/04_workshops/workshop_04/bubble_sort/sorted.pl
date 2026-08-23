sorted([]).
sorted([_X]).
sorted([X|[Y|Ys]]) :-
    X =< Y, 
    sorted([Y|Ys]).
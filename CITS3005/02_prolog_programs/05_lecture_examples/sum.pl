sum([], 0).
sum([H|T], N) :- sum(T, M), N is M + H.
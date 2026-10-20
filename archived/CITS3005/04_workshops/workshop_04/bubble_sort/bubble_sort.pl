% Check for sortedness
sorted([]).
sorted([_X]).
sorted([X|[Y|Z]]) :-
    X =< Y,
    sorted([Y|Z]).

% Case 1; elements are out of order, hence a swap is required
swap([Xs, Ys|Rest], [Ys, Xs|Rest]) :-
    Xs > Ys.

% Case 2; elements are in order, swap not required
swap([Xs|Tail1], [Xs|Tail2]) :-
    swap(Tail1, Tail2).

% Bubble sort call area
% Case 1: the list is unsorted
bubble_sort(Xs, Sorted) :-
    swap(Xs, Swapped),
    bubble_sort(Swapped, Sorted).

% Case 2: the list is sorted
bubble_sort(Sorted, Sorted) :-
    sorted(Sorted).
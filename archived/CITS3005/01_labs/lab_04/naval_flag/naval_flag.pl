% For a random list of colors red, white, blue; must sort the list s.t. it has the order red, white, blue
% [red, blue, white, red, white] -> [red, red, white, white, blue]

% Given a List input, we wish to yield Dutch
order_colours(List, Dutch) :-
    % We take a list, and need to seperate into Red, White, and Blue buckets
    split_colours(List, Red, White, Blue),
    % Prolog only allows us to glue 2 lists at a time; glue listA, listB, store in Temp
    append(Red, White, Temp),
    % Here, do the same
    append(Temp, Blue, Dutch).

% What we will need to store the colours in
split_colours([], [], [], []).

% First fact; if red is the start of the list, take it, put it in Red, and call split_colours with Tail (red not included)
split_colours([red|Tail], [red|Red], White, Blue) :-
    split_colours(Tail, Red, White, Blue).

% Second fact; if white is at the start of the list, put into White, call split_colours with Tail
split_colours([white|Tail], Red, [white|White], Blue) :-
    split_colours(Tail, Red, White, Blue).

$ Final fact; if white is at the start of the list, put into Blue, and also call split_colours with Tail
split_colours([blue|Tail], Red, White, [blue|Blue]) :-
    split_colours(Tail, Red, White, Blue).
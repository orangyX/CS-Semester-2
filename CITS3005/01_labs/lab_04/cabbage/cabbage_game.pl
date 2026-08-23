% Notes:
    % Goat + cabbage = cabbage eaten
    % Wolf + goat = goat eaten
    % The boat can only store the farmer, and one other item

% Solution:
    % farmer + wolf + cabbage + goat |                  | 
    % wolf + cabbage                 | farmer + goat    | 
    % wolf + cabbage + farmer        |                  | goat
    % cabbage                        | farmer + wolf    | goat
    % cabbage                        |                  | farmer + wolf + goat
    % cabbage                        | farmer + goat    | wolf
    % farmer + goat + cabbage        |                  | wolf
    % goat                           | farmer + cabbage | wolf
    % goat                           |                  | farmer + wolf + cabbage
    % goat                           | farmer           | wolf + cabbage
    %                                | farmer + goat    | wolf + cabbage
    %                                |                  | farmer + wolf + goat + cabbage

objects
starting_positions
solution()
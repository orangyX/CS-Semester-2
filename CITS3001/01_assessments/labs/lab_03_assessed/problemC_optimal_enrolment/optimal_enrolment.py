import sys

"""
    Consider:
        [0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0]

    Then, filling it out yields:
        [0, 0, 0, 0, 0] -> 0 hours to spend
        [0, 0, 0, 0, 0] -> nothing available to spend 1 hour on
        [0, 0, 0.6, 0.6, 0.6] -> can spend 2 hours; yield 0.6; cannot spend on 3, 4, 5 hour components, hence we store 0.6
        [0, 0, 0.6, 0.7, 0.7] -> We can spend 2 hours; do so, but we can also spend 3 hours, yielding 0.7; a new best, so we copy that into 4 hours
        [0, 0, 0.6, 0.7, 0.8] -> Same as a above, but we can now spend 4 hours to yield 0.8, a new best
        [0, 0, 0.6, 1.3, 1.3] -> We spend 2 hours, with 3 remaining:
                                    - Choose to not spend, yields 0.6
                                    - Choose to spend, yields 1.3; we select 1.3 since it is the max
                                 Then, looking into the 4 hour component, we have 2 options, again:
                                    - Do nothing (this guarantees 1.3 being read over) -> we choose this option, as it yields the max
                                    - Spend 4 hours, yielding 0.8
"""

"""
    Complexities:
        - Time complexity: O(rows * cols); since we iterate upon both rows and columns
            - Operations in the loops are constant-time
        - Space complexity:
            - O(rows * cols); requires such space due to instantiati
            on of a 2d matrix
"""

def optimal_enrolment(units, num_units, hours_avail):
    # Formulate to have hours_avail along the row; units along the column
    rows, cols = num_units + 1, hours_avail + 1
    dp_table = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        # Fetch the hour, probability components
        hour, prob = units[i-1]

        for j in range(1, cols):
            # Impossible to spend hours, so we just take what was given previously
            if j < hour:
                dp_table[i][j] = dp_table[i-1][j]
            else:
                # It is possible to spend hours, so that leaves us with 2 choices:
                    # Do not spend hours; that means that we only consider the result from past passes
                    # Spend hours, and sum the probability
                # From the above, we set dp_table[i][j] to be the max of the two choices
                # j-1 computes the hours remaining after spending some on i-1
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-hour] + prob)

    return dp_table[-1][-1]

inputs = sys.stdin.read().split()
num_units = int(inputs[0])
hours_avail = int(inputs[1])
units = []

# First 2 inputs are the number of units, and hours available
# Read first 2; do not need to iterate over these again
# Introduce a step-size of 2, hence i yields the hour, i + 1 yields the probability
for i in range(2, len(inputs), 2):
    units.append((int(inputs[i]), int(inputs[i+1])))

# Call function, divide by 100; display to 2-decimal places
print(f"{optimal_enrolment(units, num_units, hours_avail) / 100:.2f}")
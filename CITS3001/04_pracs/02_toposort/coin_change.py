import functools

def coin_change(amt: int, coins: list[int]) -> int:
    @functools.cache
    def recursive_remain(x: int):
        # If remaining becomes -ve, invalid
        if x < 0:
            return None

        # Base case: if remaining is 0, no more coins are required
        if x == 0:
            return 0

        best = None

        # Iterate through the coins
        for c in coins:
            remaining = x - c

            # Check minimum no. coins required after using c
            n = recursive_remain(remaining)

            if n is not None:
                # First solution
                if best is None:
                    best = n + 1

                else:
                    if n + 1 < best:
                        best = n + 1
        return best
    return recursive_remain(amt)
# Test case
amt = 64
coins = [1, 2, 3]

if __name__ == "__main__":
    print(coin_change(amt, coins))
    print(coin_change(111, coins))
def coin_change(coins: list[int], amt: int) -> int:
    dp_table = [None for _ in range(amt + 1)]

    dp_table[0] = 0

    for i in range(1, amt + 1):
        best = i + 1

        for c in coins:
            if i-c >= 0:
                if not dp_table[i-c] is None:
                    if dp_table[i-c] + 1 < best:
                        best = dp_table[i-c] + 1

        dp_table[i] = best if best <= i else None

    return dp_table[amt]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amt = 72
print(coin_change(coins, amt))
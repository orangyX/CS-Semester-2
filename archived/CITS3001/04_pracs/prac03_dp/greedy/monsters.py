import sys

def monster_order(monsters: list[int, int], damage: int) -> int:
    # Consider sorting monsters yielding damage gain, and other monsters yielding damage reduction
    easy_monsters = [x for x in monsters if x[1] >= 0]
    hard_monsters = [x for x in monsters if x[1] < 0]

    # Sort by health, in ascending order
    easy_monsters = sorted(easy_monsters, key = lambda x: x[0])
    hard_monsters = sorted(hard_monsters, key = lambda x: -x[1])

    for x in easy_monsters:
        if damage > x[0]:
            damage += x[1]
        else:
            return -1

    for x in hard_monsters:
        if damage > x[0]:
            # Since damages here are negative, it will decrement the damage we do
            damage += x[1]
        else:
            return -1

    return damage

inputs = sys.stdin.read().split()
num_monsters = int(inputs[0])
damage = int(inputs[1])

monsters = []

for i in range(2, 2 * (num_monsters + 1), 2):
    monsters.append((int(inputs[i]), int(inputs[i+1])))

print(monster_order(monsters, damage))
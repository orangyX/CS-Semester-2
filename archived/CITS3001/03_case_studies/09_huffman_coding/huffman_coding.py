import sys
import heapq

class Node:
    def __init__(self, char, freq, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        """
            Imperative; heapq makes use of "<" operator; this does not work between objects
                - Tell lt function how to compare
        """
        return self.freq < other.freq

    def __repr__(self):
        """
            Yields a printable version of Node, rather than "Node object at ..."
        """

        char_str = f"'{self.char}'" if self.char else "None"

        return f"Node({self.freq}, {char_str})"

def get_tree(alphabet: dict[str: int]) -> heapq[Node]:
    """
        Builds the binary huffman tree, comprised of:
            - Parent nodes; with left, right children, storing their sums
            - Leaves, storing the char, and the frequency of that char
    """
    heap = []

    for char, freq in alphabet.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        nodeA = heapq.heappop(heap)
        nodeB = heapq.heappop(heap)
        parent = Node(None, nodeA.freq + nodeB.freq, nodeA, nodeB)
        heapq.heappush(heap, parent)

    return heap

def yield_optimal_binary(huffman_tree: list[Node]) -> int:
    """
        Returns the optimal number of bits required for the current alphabet:
            - Computation: total_bits += freq * depth (depth = no. bits)
            - DFS: considers all routes from src to each leaf
                - Binary tree structure means that a visited recording is not required here
    """

    total_bits = 0

    def dfs(src: Node, bits_so_far: int):
        # Allows us to mutate the outer variable
        nonlocal total_bits

        if src.left == None and src.right == None:
            total_bits += bits_so_far * src.freq
            return

        # Recur on left, and right children
        dfs(src.left, bits_so_far + 1)
        dfs(src.right, bits_so_far + 1)

    # Begin recursion; pass the root node, and 0 -> bits_so_far
    dfs(huffman_tree[0], 0)

    return total_bits

string_input = sys.stdin.read().strip()
alphabet = {}

for word in string_input:
    for char in word:
        char = "_" if char == " " else char
        if char not in alphabet:
            alphabet[char] = 1
        else:
            alphabet[char] += 1

alphabet = dict(sorted(alphabet.items(), key=lambda x: x[1]))

huffman_tree = get_tree(alphabet)
print(yield_optimal_binary(huffman_tree))
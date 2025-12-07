import heapq
import os
from collections import defaultdict

class Node:
    def __init__(self, freq, word, left=None, right=None):
        self.freq = freq
        self.word = word
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq
    
#Teste para criar uma imagem, não sei se vai dar certo    
def export_graphviz(root, filename="huffman.dot"):
    nodes = []
    edges = []
    counter = 0

    def visit(node):
        nonlocal counter
        if node is None:
            return None

        my_id = counter
        counter += 1

        if node.word is None:
            label = "*"
        else:
            label = node.word

        nodes.append(f'  n{my_id} [label="{label}", shape=circle];')

        if node.left:
            left_id = visit(node.left)
            edges.append(f'  n{my_id} -> n{left_id} [label="0"];')
        if node.right:
            right_id = visit(node.right)
            edges.append(f'  n{my_id} -> n{right_id} [label="1"];')

        return my_id

    visit(root)

    with open(filename, "w", encoding="utf8") as f:
        f.write("digraph Huffman {\n")
        f.write("  rankdir=TB;\n") 
        f.write("  node [fontname=\"Arial\"];\n")
        for n in nodes:
            f.write(n + "\n")
        for e in edges:
            f.write(e + "\n")
        f.write("}\n")

    print(f"Arquivo {filename} gerado com sucesso!")


def compute_frequencies(words):
    freq = defaultdict(int)
    for w in words:
        freq[w] += 1
    return freq

def build_huffman_tree(freq):
    heap = [Node(freq[w], w) for w in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged = Node(n1.freq + n2.freq, None, n1, n2)
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node.word is not None:
        codebook[node.word] = prefix
    else:
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook

def encode_text(words, codebook):
    return " ".join(codebook[w] for w in words)

def pretty_tree(node, prefix="", is_left=True):
    if node is None:
        return ""
    if node.word is None:
        label = f"(*{node.freq})" 
    else:
        label = f"({node.word},{node.freq})"

    if prefix == "": 
        line = label + "\n"
    else:
        branch = "├── " if is_left else "└── "
        line = prefix + branch + label + "\n"
    text = line
    if node.left or node.right:
        new_prefix = prefix + ("│   " if is_left else "    ")
        text += pretty_tree(node.left, new_prefix, True)
        text += pretty_tree(node.right, new_prefix, False)

    return text


def process_texts(input_path, output_path):
    with open(input_path, "r", encoding="utf8") as f:
        content = f.read().strip()

    texts = [t.strip() for t in content.split("\n\n")]

    with open(output_path, "w", encoding="utf8") as out:
        for i, text in enumerate(texts, 1):
            words = text.replace(".", "").replace(",", "").split()

            freq = compute_frequencies(words)
            tree = build_huffman_tree(freq)
            codebook = generate_codes(tree)
            encoded = encode_text(words, codebook)

            export_graphviz(tree, filename=f"huffman_texto_{i}.dot")

            out.write(f"=== TEXTO {i} ===\n")
            out.write("\nÁRVORE DE HUFFMAN:\n")
            out.write(pretty_tree(tree))

            out.write("\nCÓDIGOS GERADOS:\n")
            for w, c in codebook.items():
                out.write(f"{w}: {c}\n")

            out.write("\nTEXTO COMPRIMIDO:\n")
            out.write(encoded + "\n\n")
    print("Arquivo output.dat gerado com sucesso!")

if __name__ == "__main__":
    input_path = os.path.join("data", "input.dat")
    output_path = os.path.join("data", "output.dat")
    process_texts(input_path, output_path)

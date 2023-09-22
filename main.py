import json
from node_id_encoder import encode_node_id

# A importação do arquivo level.json vem da pasta debug
# se quiser utilizar outro arquivo, coloque o seu caminho correto

json_file = open("./debug/level.json", "r")

matrix = json.load(json_file)
inverted_matrix = [list(coluna) for coluna in zip(*matrix)]

graph = open("all_graph.json", "w")

all_graph = {"topology": {}, "meta": {}}


# Dentro do loop eu preciso olhar para as 4 direções da matriz

for i in range(len(inverted_matrix)):
    for j in range(len(inverted_matrix[i])):
        edges = [None] * 4
        id = str(encode_node_id(i, j))

        # Vertice de cima (top)
        if i - 1 >= 0:
            edges[0] = inverted_matrix[i - 1][j].get("type")

        # Verice direita (right)
        if j + 1 < len(inverted_matrix[i]):
            edges[1] = inverted_matrix[i][j + 1].get("type")

        # Vertice de baixo (bottom)
        if i + 1 < len(inverted_matrix):
            edges[2] = inverted_matrix[i + 1][j].get("type")

        # Vertice esquerda (left)
        if j - 1 >= 0:
            edges[3] = inverted_matrix[i][j - 1].get("type")

        if inverted_matrix[i][j].get("type") != "none":
            # Formatado em cima-dir-baixo-esq
            binary_edges = "" 
            for edge in edges:
                if edge != "none":
                    binary_edges += "1"
                else:
                    binary_edges += "0"
            all_graph["topology"][id] = binary_edges

        node = {
            "type": matrix[i][j].get("type"),
            "position": (i, j),
        }

        all_graph["meta"][id] = node


json.dump(all_graph, graph, indent=1)

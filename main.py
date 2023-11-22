import json
from node_id_encoder import encode_node_id

# A importação do arquivo level.json vem da pasta debug
# se quiser utilizar outro arquivo, coloque o seu caminho correto

json_file = open("./debug/level-cs.json", "r")

map = json.load(json_file)

matrix = map['map']


# print(matrix)

graph = open("graph-cs.json", "w")

all_graph = {"topology": {}, "meta": {}, "core": {}, "spawners": []}

all_graph["core"] = map["metadata"]["core"]
all_graph["spawners"] = map["metadata"]["spawners"]


# Dentro do loop eu preciso olhar para as 4 direções da matriz

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        edges = [None] * 4
        id = str(encode_node_id(i, (len(matrix[i]) - j - 1)))

        # Vertice de cima (top)
        if i - 1 >= 0:
            edges[0] = matrix[i - 1][j].get("type")

        # Verice direita (right)
        if j + 1 < len(matrix[i]):
            edges[1] = matrix[i][j + 1].get("type")

        # Vertice de baixo (bottom)
        if i + 1 < len(matrix):
            edges[2] = matrix[i + 1][j].get("type")

        # Vertice esquerda (left)
        if j - 1 >= 0:
            edges[3] = matrix[i][j - 1].get("type")

        if matrix[i][j].get("type") != "none":
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
        }

        all_graph["meta"][id] = node


json.dump(all_graph, graph, indent=1)

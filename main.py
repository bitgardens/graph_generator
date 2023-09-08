import json

json_file = open('./data.json', 'r')

matrix = json.load(json_file)

graph = open('all_graph.json', 'w')
# graph_list = open('graph.json', 'w')

all_graph = []
# graph = {"connections": {}}

# Dentro do loop eu preciso olhar para as 4 direções da matriz

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        edges = [None] * 4

        # Vertice de cima
        if (i - 1 >= 0):
            edges[0] = matrix[i - 1][j].get("type")

        # Verice direita
        if (j + 1 < len(matrix[i])):
            edges[1] = matrix[i][j + 1].get("type")

        # Vertice de baixo
        if (i + 1 < len(matrix)):
            edges[2] = matrix[i + 1][j].get("type")

        # Vertice esquerda
        if (j - 1 >= 0):
            edges[3] = matrix[i][j - 1].get("type")

        node = {
            "type": matrix[i][j].get("type"),
            "name": i*10 + j + 1,
            "position": (i, j),
            "edges": edges
        }

        all_graph.append(node)

        # graph["connections"].update(**edges)


json.dump(all_graph, graph, indent=1)

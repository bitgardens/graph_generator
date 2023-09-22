# Graph Generator

Essa função tem como responsabilidade pegar a matriz gerada pelo `map_generator` e gerar o grafo à partir dela (veja o grafo [aqui](./all_graph.json)).

O grafo é gerado em um arquivo JSON que está dividido em dois atributos, `topography` inclui o `id` - gerado pela função [node_id_encoder](./node_id_encoder.py) - que é atribuído ao valor `binary_edges`, representando o tipo dos 4 vértices vizinhos. O outro atributo, `meta`, é responsável por armazenar, pelo mesmo id, o tipo e a coordenada do respectivo vértice, oferecendo informações concretas, sem compactação.

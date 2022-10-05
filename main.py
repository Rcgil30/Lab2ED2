import folium
import pandas as pd

"""Creaciòn del grafo"""
class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.connections: list[Node] = []
        self.weights: list[float] = []
        self.pos = 0

    def __repr__(self) -> str:
        return self.data
class Grafo:
    def __init__(self) -> None:
        self.listavertices: list[Node] = []
        self.listaciudades: list[str] = []
        self.MatrizDis: list[list[int]]
        self.MatrizRec: list[list[Node]]

    def MatrizDistancia(self) -> list[list[int]]:
        Matriz = []
        length = len(self.listavertices)
        for i in range(length):
            Fila = []
            for j in range(length):
                Fila.append(float("inf"))
            Matriz.append(Fila)
        for i in range(length):
            Matriz[i][i] = 0
        for vertice in self.listavertices:
            for conexion in vertice.connections:
                Matriz[vertice.pos][conexion.pos] = vertice.weights[vertice.connections.index(conexion)]
        return Matriz

    def MatrizRecorrido(self):
        Matriz = []
        length = len(self.listavertices)
        for i in range(length):
            Fila = []
            for j in range(length):
                Fila.append(0)
            Matriz.append(Fila)
        for vertice in self.listavertices:
            for i in range(length):
                Matriz[i][vertice.pos] = vertice
        
        return Matriz

    def menorCosto(self, listaPesos: list[int]):
        min = float("inf")
        for peso in listaPesos:
            if peso < min:
                min = peso
                minindex = listaPesos.index(peso)
        return minindex
    
    def FloydWarshall(self):
        n = len(self.listavertices)
        Matriz = self.MatrizDistancia()
        MatrizR = self.MatrizRecorrido()
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    Min = min(Matriz[i][j], Matriz[i][k] + Matriz[k][j])
                    if Min != Matriz[i][j]:
                        MatrizR[i][j] = self.listavertices[k]
                    Matriz[i][j] = Min
                    
        self.MatrizDis = Matriz
        self.MatrizRec = MatrizR

    def PrintCamino(self, start: str, finish: str):
        node1 = self.listavertices[self.listaciudades.index(start)]
        node2 = self.listavertices[self.listaciudades.index(finish)]
        print(node1, end=" -> ")
        if node2 in node1.connections and self.MatrizRec[node1.pos][node2.pos] == node2:
            print(node2)
        else:
            aux = node2
            path = []
            while aux not in node1.connections:
                aux = self.MatrizRec[node1.pos][aux.pos]
                path.append(aux)
            path.reverse()
            for node in path:
                print(node, end=" -> ")
            print(node2)


grafo = Grafo()
vuelos = pd.read_csv('data/totalvuelos.csv')
"""Iteramos a través del df y añadimos las ciudades al grafo"""
c = 0
for city in vuelos["Ciudad_Origen"]:
    if city not in grafo.listaciudades:
        grafo.listaciudades.append(city)
        nodo = Node(city)
        grafo.listavertices.append(nodo)
        nodo.pos = c
        c += 1


for index, info in vuelos.iterrows():
    indexor = grafo.listaciudades.index(info["Ciudad_Origen"])
    indexdes = grafo.listaciudades.index(info["Ciudad_Destino"])
    
    ciudad_or = grafo.listavertices[indexor]
    ciudad_des = grafo.listavertices[indexdes]
    #print(ciudad_or)
    #print(ciudad_des)
    ciudad_or.connections.append(ciudad_des)
    ciudad_or.weights.append(round(info["distance_km"]))

grafo.FloydWarshall()

print("Camino minimo")
grafo.PrintCamino("GUAPI", "ARMENIA")
print()
"""
for vertice in grafo.listavertices:
    print(vertice, end=" -> ")
    for conexion in vertice.connections:
        print(conexion, end=" ")
    print()
"""

"""m = grafo.MatrizDistancia()
for f in m:
    print(f, end="\n")"""
"""
f = grafo.FloydWarshall()[0]
for m in f:
    print(m)
"""
map = folium.Map(location=[4.570868,-74.297333],zoom_start=6)
for index, location_info in vuelos.iterrows():
    folium.Marker([location_info["lat_st"], location_info["lng_st"]], popup=location_info["Ciudad_Origen"]).add_to(map)
#Por ahora sin lineas
#for index, location_info in vuelos.iterrows():
#    folium.vector_layers.PolyLine([(location_info["lat_st"], 
#    location_info["lng_st"]),(location_info["lat_end"], location_info["lng_end"])],color="blue",weight=3, 
#    popup=str(location_info["distance_km"])+"km").add_to(map)
map.save("map.html")
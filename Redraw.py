import webbrowser
from main import grafo
import pandas as pd
import folium

def Update_Map(start: str, finish: str):
    if start == finish:
        return
    else:
        vuelos = pd.read_csv('data/totalvuelos.csv')
        
        map = folium.Map(location=[4.570868,-74.297333],zoom_start=6)
        for index, location_info in vuelos.iterrows():
            folium.Marker([location_info["lat_st"], location_info["lng_st"]], popup=location_info["Ciudad_Origen"]).add_to(map)
        if finish == "TODOS":
            lista = grafo.listavertices
            for node in lista:
                if node.data != start:
                    lista2 = grafo.ListaRecorrido(start, node.data)
                    for node1 in lista2:
                        index = lista2.index(node1)
                        if index != len(lista2) - 1:
                            node2 = lista2[lista2.index(node1) + 1]
                            folium.vector_layers.PolyLine([(node1.lat, node1.long), (node2.lat, node2.long)], color="blue", weight=3).add_to(map)
        else:
            lista = grafo.ListaRecorrido(start, finish)
            for node in lista:
                index = lista.index(node)
                if index != len(lista) - 1:
                    node2 = lista[lista.index(node) + 1]
                    folium.vector_layers.PolyLine([(node.lat, node.long), (node2.lat, node2.long)], color="blue", weight=3).add_to(map)

    map.save("map.html")


Update_Map("SAN ANDRES", "TODOS")
webbrowser.open("youtube.com")


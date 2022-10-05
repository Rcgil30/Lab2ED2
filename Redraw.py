import webbrowser
from main import grafo
import pandas as pd
import folium

def Update_Map(start: str, finish: str):
    vuelos = pd.read_csv('data/totalvuelos.csv')
    lista = grafo.ListaRecorrido(start, finish)
    map = folium.Map(location=[4.570868,-74.297333],zoom_start=6)
    for index, location_info in vuelos.iterrows():
        folium.Marker([location_info["lat_st"], location_info["lng_st"]], popup=location_info["Ciudad_Origen"]).add_to(map)
    for node in lista:
        index = lista.index(node)
        if index != len(lista) - 1:
            node2 = lista[lista.index(node) + 1]
            folium.vector_layers.PolyLine([(node.lat, node.long), (node2.lat, node2.long)], color="blue", weight=3).add_to(map)

    map.save("map.html")


Update_Map("GUAPI", "ARMENIA")


webbrowser.open("index.html")
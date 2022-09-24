import folium
import pandas as pd
vuelos = pd.read_csv('data/totalvuelos.csv')
map = folium.Map(location=[4.570868,-74.297333],zoom_start=6)
for index, location_info in vuelos.iterrows():
    folium.Marker([location_info["lat_st"], location_info["lng_st"]], popup=location_info["Ciudad_Origen"]).add_to(map)
map.save("map.html")
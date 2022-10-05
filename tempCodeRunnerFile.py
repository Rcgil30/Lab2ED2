"""for index, location_info in vuelos.iterrows():
    folium.vector_layers.PolyLine([(location_info["lat_st"], 
    location_info["lng_st"]),(location_info["lat_end"], location_info["lng_end"])],color="blue",weight=3, 
    popup=str(location_info["distance_km"])+"km").add_to(map)"""
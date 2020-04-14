import folium
map= folium.Map(location=[7.8731,  80.7718],zoom_start=8,titles="Mapbox Bright")
fg=folium.FeatureGroup(name="Your Destination")
for coordinate in ([7.8731,80.7718],[6.0495233,80.2522632]):
    fg.add_child(folium.Marker(location=[6.0495233,80.2522632], popup="Hi, This is Anjana's place", icon=folium.Icon(color="green")))
    map.add_child(fg)
    fg.add_child(folium.Marker(location=[7.023589899, 79.963741399], popup="Hi, This is Pasindu's place",icon=folium.Icon(color="black")))
    map.add_child(fg)
    fg.add_child(folium.Marker(location=[6.767306, 79.952473], popup="Hi, This is Sunanda's place",icon=folium.Icon(color="red")))
    map.add_child(fg)
    fg.add_child(folium.Marker(location=[6.1018267,80.3641048], popup="Hi, This is Chamodi's place",icon=folium.Icon(color="blue")))
    map.add_child(fg)
    map.save("folium.html")
    print(map)
 
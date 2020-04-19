import folium

# create map Object
m = folium.Map(location=[7.8731, 80.7718], zoom_start=8)

# Global tooltip
tooltip = 'Click for more info'

# Create markers
folium.Marker([7.8731, 80.7718],
              popup='<strong>Center point</strong>',
              tooltip=tooltip).add_to(m);
folium.Marker([6.0495233,80.2522632],
              popup="Hi, This is Anjana's place",
              icon=folium.Icon(color="green", icon="leaf")).add_to(m)

# Circle marker
folium.CircleMarker(
    location = [7.023589899, 79.963741399],
    radius=50,
    popup='Pasindu area',
    color= '#428bca',
    fill=True,
    fill_color='blue'
).add_to(m)

# Genarate map
m.save('map01.html')
print('Check the folder')

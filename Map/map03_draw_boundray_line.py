import folium
import os

# create map Object
m = folium.Map(location=[7.8731, 80.7718], zoom_start=8)

# Global tooltip
tooltip = 'Click for more info'

# Geojson Data
overlay = os.path.join('overlay.json')

# Create markers
folium.Marker([7.8731, 80.7718],
              popup='<strong>Center point</strong>',
              tooltip=tooltip).add_to(m);
folium.Marker([6.0495233, 80.2522632],
              popup="Hi, This is Anjana's place",
              icon=folium.Icon(color="green", icon="leaf")).add_to(m)

folium.GeoJson(overlay, name='Galle').add_to(m)

# Generate map
m.save('map03.html')
print('Check the folder')

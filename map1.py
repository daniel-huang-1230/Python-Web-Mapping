import folium
#first create a map object
map=folium.Map(location=[38.58, -99], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name='My Map')

for coordinates in [[38.2, -99.1],[39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup='Hi I am a marker', icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('Map1.html')


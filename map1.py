import folium, pandas
#first create a map object
map=folium.Map(location=[38.58, -99], zoom_start=6, tiles="Mapbox Bright")
data = pandas.read_csv("Volcanoes_USA.txt")
fg = folium.FeatureGroup(name='My Map')

#convert the pandas series to python list
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])



for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('Map1.html')


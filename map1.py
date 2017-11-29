import folium, pandas
# first create a map object
map = folium.Map(location=[38.58, -99], zoom_start=6, tiles="Mapbox Bright")
data = pandas.read_csv("Volcanoes_USA.txt")
fg = folium.FeatureGroup(name='My Map')
# convert the pandas series to python list
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, fill=True, color='gray', fill_opacity=0.7, fill_color=color_producer(el), popup=str(el)+" m"))

map.add_child(fg)

map.save('Map1.html')


# a function that determines the color of the marker based on elevation

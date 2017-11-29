import folium, pandas
# first create a map object
map = folium.Map(location=[38.58, -99], zoom_start=6, tiles="Mapbox Bright")
data = pandas.read_csv("Volcanoes_USA.txt")
fgv = folium.FeatureGroup(name='Volcanoes')
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
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, fill=True, color='gray', fill_opacity=0.7,
                                     fill_color=color_producer(el), popup=str(el)+" m"))

fgp = folium.FeatureGroup(name='Population')
# add another layer: the GeoJson object
# the x inside the lambda expression is 'feature' in geojson object ----can refer to the doc of folium library
fgp.add_child(folium.GeoJson(data=(open('world.json','r', encoding='utf-8-sig')).read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgp)
map.add_child(fgv)
# it's important to add the layer control object after we've added all feature group(s)
map.add_child(folium.LayerControl())
map.save('Map1.html')


# a function that determines the color of the marker based on elevation

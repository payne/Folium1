import folium

m = folium.Map(location=[45.5236, -122.6750])

tooltip = "Click me!"
folium.Marker(
    [40.7127, -74.0059], popup="<i>New York City</i>", tooltip=tooltip).add_to(m)


m.save('map.html')
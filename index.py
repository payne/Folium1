import folium
import pandas as pd
import os

def makeChoropleth(m, geo_data, data):
    choropleth = folium.Choropleth(
    geo_data=geo_data,
    name='choropleth',
    data=data,
    columns=['State','Recursers'],
    nan_fill_color='grey',
    nan_fill_opacity=0.4,
    key_on='feature.id',
    fill_color='YlGn',
    legend_name='# of Recursers',
    highlight = True,
    fill_opacity=0.5
    ).add_to(m)
    return choropleth 

def conusChropleth(m, states, state_data, folium):
    choropleth = makeChoropleth(m, states, state_data)
    folium.LayerControl().add_to(m)

    # Display Region Label
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], labels=True)
    )

def main():
    states = os.path.join('data', 'us-states.json')
    countries245 = os.path.join('data', '245countries.json')
    recurse_data = os.path.join('data', 'recurse.csv')
    state_data = pd.read_csv(recurse_data)

    m = folium.Map(location=[48, -102], zoom_start=3)

    # TODO: Get both chropleth maps to work.
    # conusChropleth(m, states, state_data, folium)

    choropleth = makeChoropleth(m, countries245, None)

    # TODO: How to get the number of Recursers as the tool tip?
    m.save('index.html')

if __name__ == "__main__":
    main()


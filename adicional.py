import plotly.express as px

# Datos de volcanes de El Salvador En 3D
datos_volcanes = {
    'volcan': ['Santa Ana', 'San Salvador', 'San Miguel', 'Izalco', 'Conchagua'],
    'altura': [2381, 1893, 2130, 1950, 1225],
    'ultima_erupcion': [2005, 1917, 2002, 1966, 2000],
    'tipo': ['Estratovolcán', 'Estratovolcán', 'Estratovolcán', 'Cono de escoria', 'Estratovolcán'],
    'x': [1, 2, 3, 4, 5],  
    'y': [2, 1, 3, 4, 5],  
    'z': [2381, 1893, 2130, 1950, 1225]  
}

fig_3d = px.scatter_3d(
    datos_volcanes,
    x='x',
    y='y', 
    z='z',
    color='altura',
    size='altura',
    hover_name='volcan',
    hover_data={
        'altura': True,
        'ultima_erupcion': True,
        'tipo': True,
        'x': False,
        'y': False,
        'z': False
    },
    title='🌋 Volcanes de El Salvador - Vista 3D',
    size_max=20,
    color_continuous_scale='reds'
)

# Personalizar el hover
fig_3d.update_traces(
    hovertemplate=(
        "<b>%{hovertext}</b><br>" +
        "📏 Altura: %{customdata[0]} m<br>" +
        "🔥 Última erupción: %{customdata[1]}<br>" +
        "🏔️ Tipo: %{customdata[2]}<br>" +
        "<extra></extra>"
    ),
    marker=dict(
        sizemode='diameter',
        sizeref=100
    )
)

fig_3d.update_layout(
    scene=dict(
        xaxis_title='Coordenada X',
        yaxis_title='Coordenada Y', 
        zaxis_title='Altura (metros)',
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.5)
        )
    ),
    height=600
)

fig_3d.show()


 #  mapa de el salvador intercativo

import plotly.express as px

# países de Centroamérica
datos_centroamerica = {
    'pais': ['Guatemala', 'Honduras', 'El Salvador', 'Nicaragua', 'Costa Rica', 'Panamá', 'Belice'],
    'poblacion': [17900000, 9900000, 6500000, 6600000, 5100000, 4300000, 400000],
    'area_km2': [108889, 112492, 21041, 130373, 51100, 75420, 22966],
    'capital': ['Ciudad de Guatemala', 'Tegucigalpa', 'San Salvador', 'Managua', 'San José', 'Panamá', 'Belmopán']
}

# mapa de Centroamérica
fig = px.choropleth(
    datos_centroamerica,
    locations='pais',
    locationmode='country names',
    color='poblacion',
    scope='north america',
    title='🗺️ MAPA DE CENTROAMÉRICA',
    color_continuous_scale='viridis',
    hover_name='pais',
    hover_data={
        'poblacion': ':,',
        'area_km2': ':,',
        'capital': True
    }
)

# Personalizar el hover
fig.update_traces(
    hovertemplate=(
        "<b>%{location}</b><br>" +
        "🏙️ Capital: %{customdata[2]}<br>" +
        "👥 Población: %{customdata[0]:,} hab<br>" +
        "📏 Área: %{customdata[1]:,} km²<br>" +
        "<extra></extra>"
    )
)


fig.update_geos(
    visible=False,
    center=dict(lat=12.0, lon=-85.0),
    lataxis_range=[5.0, 18.0],    
    lonaxis_range=[-92.0, -77.0], 
    showcountries=True,
    countrycolor="black",
    showland=True,
    landcolor="lightgreen",
    showocean=True,
    oceancolor="lightblue"
)

fig.update_layout(
    width=800,
    height=600,
    font=dict(size=12),
    title_font=dict(size=20, family="Arial Black"),
    geo=dict(bgcolor='lightcyan')
)

fig.show()
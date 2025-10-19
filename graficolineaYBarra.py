import plotly.express as px

# GRÁFICO 1: LÍNEA - TEMPERATURA MÁS LLAMATIVO


fig1 = px.line(
    x=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    y=[32, 33, 34, 33, 32, 31, 31, 31, 30, 30, 31, 31],
    title="🔥 Temperatura Mensual en El Salvador 🌴",
    labels={'x': 'Meses del Año', 'y': 'Temperatura (°C)'},
    markers=True,
    line_shape="spline",  
    color_discrete_sequence=['#FF6B35']  
)


fig1.update_traces(
    line=dict(width=4),     
    marker=dict(size=8, symbol='diamond')  
)

fig1.update_layout(
    plot_bgcolor='lightcyan',
    paper_bgcolor='white',
    font=dict(family="Arial", size=12, color="darkblue"),
    title_font=dict(size=18, color="#E74C3C", family="Arial Black"),
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        linecolor='black',
        linewidth=2
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        linecolor='black',
        linewidth=2
    )
)

# Añadir anotación
fig1.add_annotation(
    text="📌 Marzo es el mes más caluroso",
    x="Marzo", y=34,
    showarrow=True,
    arrowhead=2,
    bgcolor="gold"
)

fig1.show()


# GRÁFICO 2: BARRAS


fig2 = px.bar(
    x=['Pupusas', 'Yuca Frita', 'Tamales', 'Sopa de Pata', 'Atol de Elote'],
    y=[1500, 450, 200, 300, 180],
    title="🎯 Comidas Más Populares de El Salvador 🇸🇻",
    labels={'x': 'Comida Típica', 'y': 'Ventas Diarias'},
    color=[1500, 450, 200, 300, 180],
    color_continuous_scale='viridis' 
)

# Hacerlo más llamativo
fig2.update_traces(
    marker=dict(
        line=dict(width=2, color='black')  # Borde negro en las barras
    ),
    texttemplate='%{y} ventas/día',  # Texto en barras
    textposition='outside'
)

fig2.update_layout(
    plot_bgcolor='lightyellow',
    paper_bgcolor='white', 
    font=dict(family="Arial", size=12, color="darkgreen"),
    title_font=dict(size=18, color="#27AE60", family="Arial Black"),
    xaxis=dict(
        tickangle=-45,  
        linecolor='black',
        linewidth=2
    ),
    yaxis=dict(
        linecolor='black',
        linewidth=2
    ),
    coloraxis_colorbar=dict(
        title="Popularidad"
    )
)

# Añadir anotación
fig2.add_annotation(
    text="🏆 ¡Las pupusas son las más vendidas!",
    x=0, y=1600,
    showarrow=False,
    bgcolor="lightgreen",
    font=dict(size=14, color="darkgreen")
)

fig2.show()

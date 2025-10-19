import plotly.express as px


datos_turismo = {
    'destino': ['Playas', 'Volcanes', 'Pueblos', 'Ciudades', 'Sitios Arqueológicos'],
    'visitantes': [45, 25, 15, 10, 5],
    'colores': ['#FF6B35', '#4ECDC4', '#45B7D1', '#96CEB4', '#F9C80E']
}

# Crear gráfico de pastel 
fig = px.pie(
    names=datos_turismo['destino'],
    values=datos_turismo['visitantes'],
    title="🏖️ Turismo en El Salvador 🌋",
    color=datos_turismo['destino'],
    color_discrete_sequence=datos_turismo['colores'],
    hole=0.4
)

fig.update_traces(
    textinfo='percent+label',  #  porcentaje y nombre 
    textfont=dict(size=12, family="Arial", color="white"), 
    marker=dict(
        line=dict(color='white', width=2)
    ),
    pull=[0.1, 0, 0, 0, 0],  
    textposition='inside'
)

# Diseño 
fig.update_layout(
    font=dict(family="Arial", size=10, color="#2C3E50"),  
    title_font=dict(size=16, color="#E74C3C", family="Arial Black"),  
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="left",
        x=1.05,  
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#2C3E50',
        borderwidth=1,
        font=dict(size=10),  
        itemwidth=30  
    ),
    annotations=[dict(
        text='45%',  
        x=0.5, y=0.5,
        font_size=16,  
        showarrow=False,
        font=dict(color="#E74C3C", family="Arial Black")
    )],
    margin=dict(l=20, r=20, t=50, b=20),  
    width=600, 
    height=400  
)

# Añadir anotación 
fig.add_annotation(
    text="💡 Playas: 45% favoritas",
    xref="paper", yref="paper",
    x=0.02, y=0.98,
    showarrow=False,
    bgcolor="rgba(255, 107, 53, 0.9)",
    bordercolor="white",
    borderwidth=1,
    font=dict(color="white", size=10, family="Arial")
)

fig.show()

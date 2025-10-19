import plotly.express as px
# px.scatter() — Gráficos de dispersión 

# Datos sobre carreras, sueldos y demanda laboral
datos = {
    'carrera': [
        'Medicina', 'Ing. Software', 'Derecho', 'Arquitectura', 
        'Ing. Civil', 'Administración', 'Contaduría', 'Psicología',
        'Comunicaciones', 'Enfermería', 'Docencia', 'Turismo'
    ],
    'sueldo_promedio': [
        3500, 2800, 2200, 2000, 1800, 1500, 1400, 1200, 1100, 1000, 900, 800
    ],
    'demanda_mercado': [95, 98, 85, 75, 80, 70, 65, 60, 55, 90, 50, 45],
    'años_estudio': [7, 5, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4],
    'sector': [
        'Salud', 'Tecnología', 'Legal', 'Construcción', 'Construcción',
        'Empresarial', 'Empresarial', 'Salud', 'Medios', 'Salud', 'Educación', 'Servicios'
    ]
}

# Crear el gráfico 
fig = px.scatter(
    datos,
    x="demanda_mercado",
    y="sueldo_promedio",
    size="años_estudio",
    color="sector",
    size_max=25,
    hover_name="carrera",
    text="carrera",
    title="🎓 MERCADO LABORAL EL SALVADOR: Carreras vs Sueldos y Demanda",
    labels={
        'sueldo_promedio': 'Sueldo Mensual Promedio (USD) 💰',
        'demanda_mercado': 'Demanda en el Mercado (%) 📊',
        'años_estudio': 'Años de Estudio 📚',
        'sector': 'Sector Económico',
        'carrera': 'Carrera Profesional'
    },
    color_discrete_sequence=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3E92CC', '#291720'],
    template='plotly_white'
)

# Personalización 
fig.update_layout(
    font=dict(family="Montserrat, Arial", size=12, color="#2C3E50"),
    title_font=dict(size=24, color="#2C3E50", family="Montserrat Black"),
    legend=dict(
        orientation="v",
        yanchor="top",
        y=0.98,
        xanchor="left",
        x=1.02,
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#BDC3C7',
        borderwidth=1,
        font=dict(size=11, color="#2C3E50")
    ),
    xaxis=dict(
        showgrid=True,
        gridcolor='rgba(189, 195, 199, 0.3)',
        linecolor='#2C3E50',
        linewidth=2,
        range=[40, 100],
        ticksuffix="%",
        title_font=dict(size=14, color="#2C3E50")
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='rgba(189, 195, 199, 0.3)',
        linecolor='#2C3E50',
        linewidth=2,
        tickprefix="$",
        title_font=dict(size=14, color="#2C3E50")
    ),
    plot_bgcolor='rgba(248, 249, 250, 0.8)',
    paper_bgcolor='white',
    hoverlabel=dict(
        bgcolor="white",
        bordercolor="#2C3E50",
        font_size=12,
        font_color="#2C3E50"
    ),
    width=1000,
    height=600
)

# marcadores
fig.update_traces(
    marker=dict(
        line=dict(width=2, color='white'),
        sizemin=8,
        opacity=0.8
    ),
    textfont=dict(
        family="Arial",
        size=11,
        color="#2C3E50"
    ),
    textposition='top center'
)

# Anotaciones informativas
fig.add_annotation(
    text="💡 <b>Top Carreras:</b> Medicina e Ing. Software lideran en sueldo y demanda",
    xref="paper", yref="paper",
    x=0.02, y=0.98,
    showarrow=False,
    bgcolor="rgba(46, 134, 171, 0.9)",
    bordercolor="#2C3E50",
    borderwidth=1,
    font=dict(color="white", size=12, family="Arial")
)

fig.add_annotation(
    text="🇸🇻 Datos representativos del mercado laboral salvadoreño",
    xref="paper", yref="paper",
    x=0.5, y=0.02,
    showarrow=False,
    font=dict(color="#7F8C8D", size=10, family="Arial"),
    align="center"
)

fig.show()


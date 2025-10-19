import plotly.express as px
import numpy as np


#  Edades de la población salvadoreña
np.random.seed(123)
edades = np.random.normal(35, 15, 1000).clip(0, 80)  # Edades entre 0-80 años

# Histograma 
fig_simple = px.histogram(
    x=edades,
    title="👥 Distribución de Edades en El Salvador",
    labels={'x': 'Edad', 'y': 'Cantidad de Personas'},
    nbins=12,
    color_discrete_sequence=['#2E86AB']
)

# Personalización 
fig_simple.update_traces(
    marker=dict(
        line=dict(width=2, color='white'),
        opacity=0.8
    )
)

fig_simple.update_layout(
    font=dict(family="Arial", size=12),
    title_font=dict(size=18, color="#2E86AB", family="Arial Black"),
    xaxis=dict(
        title="Edad (años)",
        showgrid=True
    ),
    yaxis=dict(
        title="Número de Personas", 
        showgrid=True
    ),
    plot_bgcolor='lightyellow',
    height=400
)

#  líneas de referencia
fig_simple.add_vline(x=18, line_dash="dot", line_color="red", 
                    annotation_text="Mayoría de Edad")
fig_simple.add_vline(x=60, line_dash="dot", line_color="orange", 
                    annotation_text="Edad de Jubilación")

fig_simple.show()


 # diagrama de caja

import plotly.express as px

# Datos de calificaciones por materia
fig = px.box(
    x=["Matemáticas"] * 30 + ["Ciencias"] * 30 + ["Literatura"] * 30 + ["Historia"] * 30,
    y=[85, 78, 92, 67, 88, 74, 95, 82, 79, 91, 72, 84, 89, 76, 93, 68, 87, 81, 94, 77, 86, 83, 90, 75, 96, 69, 85, 80, 92, 73] + 
      [90, 82, 88, 85, 92, 78, 95, 87, 83, 91, 79, 86, 89, 84, 93, 80, 88, 85, 94, 81, 87, 84, 92, 82, 96, 83, 89, 86, 91, 79] +
      [78, 85, 72, 90, 75, 88, 70, 92, 77, 86, 74, 89, 76, 87, 73, 91, 79, 84, 71, 93, 80, 83, 69, 94, 82, 85, 68, 95, 81, 86] +
      [82, 88, 85, 90, 83, 87, 86, 89, 84, 91, 81, 88, 85, 92, 83, 87, 86, 90, 84, 89, 85, 91, 82, 88, 86, 93, 84, 87, 85, 92],
    title="📚 Calificaciones por Materia",
    labels={'x': 'Materias', 'y': 'Calificación'}
)


fig.update_traces(
    boxmean=True,
    marker=dict(size=6, opacity=0.6),
    hovertemplate=(
        "<b>%{x}</b><br><br>" +
        "📊 <b>Estadísticas:</b><br>" +
        "• Mínimo: %{min}<br>" +
        "• Cuartil 1 (Q1): %{q1}<br>" +
        "• Mediana: %{median}<br>" +
        "• Cuartil 3 (Q3): %{q3}<br>" +
        "• Máximo: %{max}<br>" +
        "• Media: %{mean:.1f}<br>" +
        "• Límite Superior: %{upperfence}<br>" +
        "• Límite Inferior: %{lowerfence}<br>" +
        "<extra></extra>"
    )
)

fig.update_layout(
    font=dict(family="Arial", size=12),
    title_font=dict(size=18, color="#2C3E50"),
    xaxis=dict(title="Materias"),
    yaxis=dict(title="Calificación", range=[60, 100]),
    plot_bgcolor='white',
    height=500,
    showlegend=False
)

# líneas de referencia
fig.add_hline(y=70, line_dash="dash", line_color="green", annotation_text="Aprobación (70)")
fig.add_hline(y=90, line_dash="dash", line_color="gold", annotation_text="Excelencia (90)")

fig.show()
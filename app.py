import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

# ------------------------
# App Initialization
# ------------------------
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX]  # Clean modern theme
)

# ------------------------
# Data
# ------------------------
chart_data = pd.DataFrame({
    "x": list(range(30)),
    "y": [2 ** x for x in range(30)]
})

# ------------------------
# Plot
# ------------------------
fig = px.scatter(
    chart_data,
    x="x",
    y="y",
    title="Exponential Growth Visualization",
    labels={"x": "Apps", "y": "Fun with Data"},
    template="simple_white"
)

fig.update_traces(
    marker=dict(size=12, opacity=0.8),
    hovertemplate="Apps: %{x}<br>Value: %{y}<extra></extra>"
)

fig.update_layout(
    title_x=0.5,
    margin=dict(l=40, r=40, t=60, b=40),
    height=450
)

# ------------------------
# Layout
# ------------------------
app.layout = dbc.Container(fluid=True, children=[

    # Navbar
    dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand("🚀 Databricks Dash App", className="fw-bold fs-4"),
        ]),
        color="dark",
        dark=True,
        sticky="top"
    ),

    dbc.Container(className="mt-4", children=[

        # Header Section
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H2("Hello World from Vargab 👋", className="fw-bold"),
                    html.P(
                        "An interactive Dash application showcasing clean UI, "
                        "responsive design, and data visualization.",
                        className="text-muted"
                    )
                ]),
                width=12
            )
        ], className="mb-4"),

        # Cards and Chart Section
        dbc.Row([

            # Cards Column
            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("📊 Chart Overview", className="card-title"),
                                html.P(
                                    "This scatter plot demonstrates exponential growth "
                                    "using interactive Plotly visuals.",
                                    className="card-text"
                                )
                            ])
                        ], className="shadow-sm"),
                        width=12
                    )
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("⚡ Tech Stack", className="card-title"),
                                html.Ul([
                                    html.Li("Dash"),
                                    html.Li("Plotly"),
                                    html.Li("Bootstrap")
                                ])
                            ])
                        ], className="shadow-sm"),
                        width=12
                    )
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("🎯 Use Case", className="card-title"),
                                html.P(
                                    "Ideal for analytics dashboards, "
                                    "Databricks visual apps, and demos."
                                )
                            ])
                        ], className="shadow-sm"),
                        width=12
                    )
                ])
            ], md=4, className="mb-4"),

            # Chart Column
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id="fare-scatter",
                            figure=fig,
                            config={"displayModeBar": False}
                        )
                    ])
                ], className="shadow"),
                md=8, className="mb-4"
            )
        ]),

        # Footer
        dbc.Row([
            dbc.Col(
                html.P(
                    "Built with ❤️ using Dash & Plotly",
                    className="text-center text-muted mt-4"
                )
            )
        ])
    ])
])

# ------------------------
# Run App
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)

from dash import html
from pages.components.NavHeader import NavHeader
from pages.components.Footer import Footer

atr_dashboard_layout = html.Div(
    children=[
        NavHeader(),
        html.Div(
            className="flex items-center justify-center h-[93vh] w-full",
            children=[
                html.Iframe(
                    src='https://www.arcgis.com/apps/dashboards/544be5648f894c0d9f9f039cd9d34912',
                    className="w-screen h-full mt-0"
                )
            ]
        ),
        Footer()
    ]
)

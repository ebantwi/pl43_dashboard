from dash import html
from pages.components.NavHeader import NavHeader
from pages.components.Banner import Banner
from pages.components.Card import Card
from pages.components.Footer import Footer

home_layout = html.Div(
    children=[
        NavHeader(),
        Banner(),
        html.Div(
            children=[
                html.P("- Dashboards -", className="text-center text-4xl text-gray-500 uppercase"),
            ],
            className="flex justify-center items-center h-full mt-4"
        ),
        Card(),
        Footer()
    ]
)

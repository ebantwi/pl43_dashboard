from dash import html
from pages.components.NavHeader import NavHeader
from pages.components.Footer import Footer

tim_dashboard_layout = html.Div(
    children=[
        NavHeader(),
        html.Div(
            className="flex items-center justify-center h-[93vh] w-full",
            children=[
                html.Iframe(
                    src='https://app.powerbigov.us/view?r=eyJrIjoiYWQxYjM2YzgtNDA0ZS00OGU4LWIxMDItNGQwYTE1MTMyNjBhIiwidCI6ImQ3N2M3ZjRkLWQ3NjctNDYxZi1iNjI1LTA2Mjg3OTJlOWUyYSJ9&pageName=ReportSection232327be9685a786e28a',
                    className="w-screen h-full mt-0"
                )
            ]
        ),
        Footer()
    ]
)

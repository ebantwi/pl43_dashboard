from dash import html
from pages.components.NavHeader import NavHeader
from pages.components.Footer import Footer

no_page_layout = html.Div(
    children=[
        NavHeader(),
        html.Div(
            className="flex items-center justify-center h-[100vh] w-full",
            children=[
                html.Section(
                    className="bg-white ",
                        children=[
                    html.Div(
                        className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6",
                            children=[
                                html.Div(
                                    className="mx-auto max-w-screen-sm text-center",
                                    children=[
                                html.H1(
                            "404",
                            className="mb-4 text-7xl tracking-tight font-extrabold lg:text-9xl text-primary-600 dark:text-primary-500"
                        ),
                        html.P(
                            "Page is under Construction.",
                            className="mb-4 text-3xl tracking-tight font-bold text-amber-700 md:text-4xl"
                        ),
                        html.P(
                            "Sorry, the requested page is under construction. You'll find lots to explore on the home page.",
                            className="mb-4 text-lg font-medium text-gray-900 "
                        ),
                        html.A(
                            "Back to Homepage",
                            href="/",
                            className="inline-flex text-white bg-blue-600 hover:bg-primary-800 transition-all duration-300 transform hover:scale-105 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        )
                    ]
                )
            ]
        )
    ]
)
            ]
        ),
        Footer()
    ]
)
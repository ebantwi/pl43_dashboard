from dash import html

def NavHeader():
    page_logo = html.Div(
                    className = "flex items-center p-16 ",
                    children = [
                        html.A(
                                "ARL",
                                href="/",
                                className="text-white text-3xl font-bold tracking-wide hover:text-gray-200 px-3 py-2 rounded-md hover:transition-all duration-300 transform hover:scale-110"
                                ),
                    ]
    )

    page_links = html.Div(
                    className="flex items-center p-16 space-x-2",
                    children=[
                        html.A(
                                "Home",
                                href="/",
                                className="text-white text-lg font-bold hover:text-amber-400 px-3 py-2 rounded-md"
                                ),
                        html.A(
                                "About",
                                href="/about",
                                className="text-white text-lg font-bold hover:text-amber-400 px-3 py-2 rounded-md"
                                ),
                        html.A(
                                "Contact",
                                href="/contact",
                                className="text-white text-lg font-bold hover:text-amber-400 px-3 py-2 rounded-md"
                                ),
                            ]
                )
                
    navbar = html.Div(
        className = "bg-blue-950 shadow-2xl shadow-amber-100/20 p-4 h-16 flex justify-between items-center z-10 sticky top-0",
        children = [
            page_logo,
            page_links,
        ]
    )
    return navbar
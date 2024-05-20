from dash import html

def Footer():
    # Define the footer element
    footer = html.Div(
        className="bg-blue-950 shadow-2xl shadow-indigo-600/70 p-4 h-70",  # Background and shadow matching NavHeader
        children=[
            # Footer content
            html.Div(
                className="flex justify-center items-center text-white",  # Flex container and text color
                children=[
                    # Left section of the footer
                    html.Div(
                        className="text-lg font-medium",
                        children=[
                            html.P("© 2024 ARL. All rights reserved."),
                            html.A("Privacy Policy | Terms of Use", href='https://www.uky.edu/see/privacy')
                        ]
                    ),
                    
                ]
            )
        ]
    )
    
    return footer

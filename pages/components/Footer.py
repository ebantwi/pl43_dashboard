from dash import html

def Footer():
    # Define the footer element
    footer = html.Div(
        className="bg-blue-950 shadow-2xl shadow-indigo-600/70 p-4 h-35",  # Background and shadow matching NavHeader
        children=[
            # Footer content
            html.Div(
                className="flex justify-between items-center text-white",  # Flex container and text color
                children=[
                    # Left section of the footer
                    html.Div(
                        className="text-sm",
                        children=[
                            html.P("© 2024 ARL. All rights reserved."),
                            html.P("Privacy Policy | Terms of Use")
                        ]
                    ),
                    
                    # Right section of the footer
                    html.Div(
                        className="text-sm space-x-4",
                        children=[
                            html.A(
                                "Facebook",
                                href="#",
                                className="hover:text-amber-400"  # Hover effect matching NavHeader
                            ),
                            html.A(
                                "Twitter",
                                href="#",
                                className="hover:text-amber-400"
                            ),
                            html.A(
                                "LinkedIn",
                                href="#",
                                className="hover:text-amber-400"
                            )
                        ]
                    )
                ]
            )
        ]
    )
    
    return footer

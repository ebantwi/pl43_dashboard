from dash import html

def Card():
    atr_card = html.A(
        href="/atr_dashboard",  # URL to the ATR Dashboard page
        className="bg-gray-100 border rounded-lg overflow-hidden shadow-xl shadow-indigo-300/70 w-[28vw] h-[60vh] hover:transition-all duration-300 transform hover:scale-105",
        children=[
            html.Img(
                src="./assets/traffic_flow.jpeg",
                className="h-1/2 w-full object-cover"
            ),
            html.Div(
                className="p-4",
                children=[
                    html.H4(
                        "ATR Dashboard",
                        className="text-2xl font-semibold text-gray-800 mb-1"
                    ),
                    html.P(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum.",
                        className="text-gray-600"
                    )
                ]
            )
        ]
    )

    mobility_card = html.A(
        href="/mobility_dashboard",
        className="bg-gray-100 border rounded-lg overflow-hidden shadow-xl shadow-indigo-300/70 w-[28vw] h-[60vh] hover:transition-all duration-300 transform hover:scale-105",
        children=[
            html.Img(
                src="./assets/mobility.jpeg",
                className="h-1/2 w-full object-cover"
            ),
            html.Div(
                className="p-4",
                children=[
                    html.H4(
                        "Mobility Dashboard",
                        className="text-2xl font-semibold text-gray-800 mb-2"
                    ),
                    html.P(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum.",
                        className="text-gray-600"
                    )
                ]
            )
        ]
    )

    safety_card = html.A(
        href="/tim_dashboard",
        className="bg-gray-100 border rounded-lg overflow-hidden shadow-xl shadow-indigo-300/70 w-[28vw] h-[60vh] hover:transition-all duration-300 transform hover:scale-105",
        children=[
            html.Img(
                src="./assets/crash.jpeg",
                className="h-1/2 w-full object-cover"
            ),
            html.Div(
                className="p-4",
                children=[
                    html.H4(
                        "TIM Dashboard",
                        className="text-2xl font-semibold text-gray-800 mb-2"
                    ),
                    html.P(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum.",
                        className="text-gray-600"
                    )
                ]
            )
        ]
    )

    card_row = html.Div(
        className="flex justify-center space-x-10 mt-8 mb-8",
        children=[
            atr_card,
            mobility_card,
            safety_card
        ]
    )

    return card_row

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
                        "This tool provides a summary of traffic patterns across the state using the latest data from count stations, following the Traffic Monitoring Guide. It provides total traffic volumes and assesses the quality of data from each station. Detailed statistics are available at both the station level and aggregated by Functional Classification.",
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
                        "Comprehensive analytics on traffic congestion, travel times, and reliability metrics provide data-driven insights that enhance the understanding of traffic patterns and aid in planning to improve overall travel efficiency. This information can be leveraged to make informed decisions, reduce congestion, and enhance the reliability of the state transportation network.",
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
                        "Comprehensive analytics on traffic incidents, response times, and impact metrics provide data-driven insights that enhance the understanding of incident patterns and aid in planning to improve overall traffic flow and safety. This information can be leveraged to make informed decisions, expedite incident responses, and minimize disruptions to the transportation network.",
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

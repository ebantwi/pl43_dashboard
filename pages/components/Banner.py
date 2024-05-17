from dash import html

def Banner():

    # Overlay div to add a black tint
    black_tint_shadow = html.Div(
        className="absolute inset-0 bg-black opacity-75",  # Black overlay with opacity
    )

    # Title
    title = html.H1(
                "Dashboards & Story Maps HUB",
                className="text-amber-500 text-7xl font-bold text-center p-4 tracking-tight relative z-20"
            )

    text1 = html.P(
                 "Hub for intuitive and analytical dashboard applications.",
                 className="text-white text-lg text-center relative z-10"
             )

    text2 = html.P(
                 "providing Kentucky mobility and safety data insights in the form of graphs charts, tables, and maps.",
                 className="text-white text-lg text-center relative z-10"
             )

    # Container div to center the title and text
    center_container = html.Div(
        className="flex flex-col items-center justify-center h-full",  # Center content vertically and horizontally
        children=[
            
            title,
            text1,
            text2,
        ]
    )
            
    # Banner div with background image and styles
    banner = html.Div(
        # Tailwind classes for background image, width, and height
        className="bg-cover bg-center w-full h-1/2 relative",

        # Inline styles for mask properties and background image
        style={
            "--mask": "radial-gradient(58.14px at 50% calc(100% - 78px),#000 99%,#0000 101%) calc(50% - 52px) 0/104px 100%, radial-gradient(58.14px at 50% calc(100% + 52px),#0000 99%,#000 101%) 50% calc(100% - 26px)/104px 100% repeat-x",
            "-webkit-mask": "var(--mask)",
            "mask": "var(--mask)",
            "background-image": "url('assets/bridge.jpeg')",  # URL to the image in the assets folder
            "background-size": "cover",  # Cover the entire banner with the image
            "background-position": "center",  # Center the image
            "height": "78vh",  # Set height to 68% of the viewport height
        },

        children=[
            black_tint_shadow,
            center_container,  
        ]
    )

    return banner

# Notes:
# https://css-generators.com/wavy-shapes/  webpage to generate wavy shapes
# https://svgwave.in/
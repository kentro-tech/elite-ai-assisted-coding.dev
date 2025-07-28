import air
from components.layout import base_layout
from components.tool_cards import tool_cards_grid

def tool_reviews_page() -> air.Html:
    """
    Renders the tool reviews listing page using Air tags.
    
    Returns:
        An Air Html component representing the tool reviews page
    """
    return base_layout(
        "Tool Reviews",
        "Reviews of AI coding tools and practices that actually work and improve your productivity",
        "/static/CourseCard.jpg",
        air.Div(
            # Hero Section with Gradient Background
            air.Div(
                air.Div(
                    air.H1(
                        "AI Tool Reviews That Actually Help",
                        class_="text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent"
                    ),
                    air.P(
                        "Real-world testing and honest reviews of AI coding tools from a practicing developer",
                        class_="text-xl md:text-2xl text-base-content/80 max-w-3xl mx-auto"
                    ),
                    class_="text-center py-16 px-4"
                ),
                class_="bg-gradient-to-b from-base-200 to-base-100 mb-12"
            ),
            
            # Course Promo Banner
            air.Div(
                air.Div(
                    air.Div(
                        air.A(
                            air.Img(
                                src="/static/CourseCard.jpg",
                                alt="Course Card",
                                class_="rounded-lg shadow-md max-w-sm w-full"
                            ),
                            href="https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC",
                            class_="block"
                        ),
                        air.Div(
                            air.H2("Want to master AI-assisted coding?", class_="card-title text-2xl mb-4"),
                            air.P("Join our course to learn advanced techniques and patterns that will 10x your productivity with any AI coding tool.", class_="mb-4"),
                            air.A(
                                air.Strong("Enroll Now on Maven →"),
                                href="https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC",
                                class_="btn btn-primary btn-lg"
                            )
                        ),
                        class_="flex flex-col md:flex-row items-center gap-6"
                    ),
                    class_="card-body"
                ),
                class_="card bg-base-200 shadow-xl mb-12"
            ),
            
            # Section Header
            air.Div(
                air.H2("Featured Tool Reviews", class_="text-3xl font-bold mb-2"),
                air.P("In-depth analysis of the tools that actually improve your workflow", class_="text-base-content/70"),
                class_="text-center mb-8"
            ),
            
            # Tool Cards Grid with HTMX
            tool_cards_grid(),
            
            
            class_="max-w-6xl mx-auto px-4 py-8"
        )
    )



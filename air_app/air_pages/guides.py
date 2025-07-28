import air
from air_markdown import Markdown
from components.layout import base_layout
from components.guide_cards import guide_cards_grid

def guides_page() -> air.Html:
    """
    Renders the guides listing page using Air tags.
    
    Returns:
        An Air Html component representing the guides page
    """
    return base_layout(
        "Guides",
        "Universal Techniques and Concepts for using and curating context for AI",
        "/static/CourseCard.jpg",
        air.Div(
            air.H1("Guides", class_="text-4xl font-bold mb-4 text-center"),
            air.P(
                "Universal Techniques and Concepts for using and curating context for AI",
                class_="text-lg text-center mb-8"
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
            
            # Guide Cards Grid with HTMX
            guide_cards_grid(),
            
            class_="max-w-6xl mx-auto"
        )
    )



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
                            air.P("Join my course to learn advanced techniques and patterns that will 10x your productivity with any AI coding tool.", class_="mb-4"),
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

def guide_page(guide_name: str) -> air.Html:
    """
    Renders an individual guide page.
    
    Args:
        guide_name: The name of the guide
        
    Returns:
        An Air Html component representing the guide page
    """
    # Load markdown content
    content_path = f"content/guides/{guide_name}.md"
    
    try:
        markdown_content = open(content_path, 'r', encoding='utf-8').read()
    except FileNotFoundError:
        markdown_content = f"# Guide Not Found\n\nThe guide '{guide_name}' could not be found."
    
    return base_layout(
        f"{guide_name.replace('-', ' ').title()} - Isaac Flath",
        f"Learn about {guide_name.replace('-', ' ')} with practical insights and techniques for AI-assisted coding.",
        air.Main(
            air.Div(
                air.Div(
                    # Breadcrumb navigation
                    air.Div(
                        air.Div(
                            air.A("Home", href="/", class_="link link-hover"),
                            air.Span("/", class_="mx-2 text-base-content/60"),
                            air.A("Guides", href="/guides", class_="link link-hover"),
                            air.Span("/", class_="mx-2 text-base-content/60"),
                            air.Span(guide_name.replace("-", " ").title(), class_="text-base-content/60"),
                            class_="breadcrumbs text-sm mb-8"
                        ),
                        class_="max-w-4xl mx-auto"
                    ),
                    
                    # Article content
                    air.Div(
                        air.Article(
                            Markdown(markdown_content),
                            class_="prose prose-lg max-w-none"
                        ),
                        class_="max-w-4xl mx-auto bg-base-100 rounded-lg shadow-sm p-8 mb-8"
                    ),
                    
                    # Back to guides button
                    air.Div(
                        air.A(
                            "← Back to Guides",
                            href="/guides",
                            class_="btn btn-outline btn-primary"
                        ),
                        class_="max-w-4xl mx-auto mt-12 mb-8"
                    ),
                    
                    class_="container mx-auto px-4 py-8"
                ),
                class_="min-h-screen"
            ),
            class_="min-h-screen"
        )
    )


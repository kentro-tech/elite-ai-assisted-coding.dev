import air
from air_markdown import Markdown
from components.layout import base_layout
from components.course_promo import course_promo
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
        air.Div(
            air.H1("Tool Reviews", class_="text-4xl font-bold mb-4 text-center"),
            air.P(
                "Reviews of AI coding tools and practices that actually work and improve your productivity",
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
            
            # Tool Cards Grid with HTMX
            tool_cards_grid(),
            
            class_="max-w-6xl mx-auto"
        )
    )

def tool_review_page(tool_name: str) -> air.Html:
    """
    Renders an individual tool review page.
    
    Args:
        tool_name: The name of the tool to review
        
    Returns:
        An Air Html component representing the tool review page
    """
    # Load markdown content
    content_path = f"content/tool-reviews/{tool_name}.md"
    
    try:
        markdown_content = open(content_path, 'r', encoding='utf-8').read()
    except FileNotFoundError:
        markdown_content = f"# Tool Review Not Found\n\nThe tool review for '{tool_name}' could not be found."
    
    return base_layout(
        f"{tool_name.replace('-', ' ').title()} Tool Review - Isaac Flath",
        f"Detailed review of {tool_name.replace('-', ' ')} AI coding tool with real-world testing and insights.",
        air.Main(
            air.Div(
                air.Div(
                    # Breadcrumb navigation
                    air.Div(
                        air.Div(
                            air.A("Home", href="/", class_="link link-hover"),
                            air.Span("/", class_="mx-2 text-base-content/60"),
                            air.A("Tool Reviews", href="/tool-reviews", class_="link link-hover"),
                            air.Span("/", class_="mx-2 text-base-content/60"),
                            air.Span(tool_name.replace("-", " ").title(), class_="text-base-content/60"),
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
                    
                    # Back to reviews button
                    air.Div(
                        air.A(
                            "← Back to Tool Reviews",
                            href="/tool-reviews",
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


import air
from air_markdown import Markdown
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
            
            # Course Promo Banner - Enhanced Design
            air.Div(
                air.Div(
                    # Badge
                    air.Div(
                        air.Span("Limited Time Offer", class_="badge badge-accent badge-lg"),
                        class_="absolute -top-3 left-1/2 transform -translate-x-1/2"
                    ),
                    air.Div(
                        # Left side - Image
                        air.A(
                            air.Div(
                                air.Img(
                                    src="/static/CourseCard.jpg",
                                    alt="Context Engineering for Coding Course",
                                    class_="rounded-xl shadow-2xl w-full object-cover h-full"
                                ),
                                class_="relative overflow-hidden group"
                            ),
                            href="https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC",
                            class_="block flex-shrink-0 w-full md:w-96 h-64 md:h-auto"
                        ),
                        # Right side - Content
                        air.Div(
                            air.Div(
                                air.Span("🎓 Maven Course", class_="badge badge-primary badge-outline mb-4"),
                                class_="flex items-center gap-2"
                            ),
                            air.H2(
                                "Master AI-Assisted Coding",
                                class_="text-3xl md:text-4xl font-bold mb-4"
                            ),
                            air.P(
                                "Learn the exact techniques I use daily to 10x my productivity with AI tools. From prompt engineering to context curation, get practical skills that work.",
                                class_="text-lg mb-6 text-base-content/80"
                            ),
                            # Benefits list
                            air.Div(
                                air.Div(
                                    air.svg.Svg(
                                        air.svg.Path(d="M5 13l4 4L19 7", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                        class_="w-5 h-5 text-success",
                                        fill="none",
                                        stroke="currentColor",
                                        viewBox="0 0 24 24"
                                    ),
                                    air.Span("Live coding sessions", class_="text-base"),
                                    class_="flex items-center gap-2"
                                ),
                                air.Div(
                                    air.svg.Svg(
                                        air.svg.Path(d="M5 13l4 4L19 7", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                        class_="w-5 h-5 text-success",
                                        fill="none",
                                        stroke="currentColor",
                                        viewBox="0 0 24 24"
                                    ),
                                    air.Span("Real-world examples", class_="text-base"),
                                    class_="flex items-center gap-2"
                                ),
                                air.Div(
                                    air.svg.Svg(
                                        air.svg.Path(d="M5 13l4 4L19 7", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                        class_="w-5 h-5 text-success",
                                        fill="none",
                                        stroke="currentColor",
                                        viewBox="0 0 24 24"
                                    ),
                                    air.Span("Lifetime access", class_="text-base"),
                                    class_="flex items-center gap-2"
                                ),
                                class_="space-y-2 mb-8"
                            ),
                            # CTA Button
                            air.A(
                                air.Span("Enroll Now", class_="mr-2"),
                                air.Span("→", class_="text-xl"),
                                href="https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC",
                                class_="btn btn-primary btn-lg shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-200"
                            ),
                            air.P(
                                air.Span("Use code ", class_="text-sm"),
                                air.Code("ISAAC", class_="text-sm font-bold"),
                                air.Span(" for exclusive discount", class_="text-sm"),
                                class_="mt-4 text-base-content/60"
                            ),
                            class_="flex flex-col justify-center"
                        ),
                        class_="flex flex-col md:flex-row gap-8 items-stretch"
                    ),
                    class_="card-body p-8 md:p-12"
                ),
                class_="card bg-gradient-to-br from-base-200 to-base-300 shadow-2xl mb-16 relative overflow-visible"
            ),
            
            # Section Header
            air.Div(
                air.H2("Featured Tool Reviews", class_="text-3xl font-bold mb-2"),
                air.P("In-depth analysis of the tools that actually improve your workflow", class_="text-base-content/70"),
                class_="text-center mb-8"
            ),
            
            # Tool Cards Grid with HTMX
            tool_cards_grid(),
            
            # Bottom CTA
            air.Div(
                air.Div(
                    air.H3("Ready to level up your AI coding skills?", class_="text-2xl font-bold mb-4"),
                    air.P("Join hundreds of developers who've transformed their workflow", class_="mb-6 text-base-content/80"),
                    air.A(
                        "Get Started with the Course",
                        href="https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC",
                        class_="btn btn-primary btn-wide"
                    ),
                    class_="text-center"
                ),
                class_="mt-16 p-8 bg-base-200 rounded-2xl"
            ),
            
            class_="max-w-6xl mx-auto px-4 py-8"
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


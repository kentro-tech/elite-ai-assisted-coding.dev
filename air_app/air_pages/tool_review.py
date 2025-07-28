import air
from air_markdown import Markdown
from components.layout import base_layout
import os

def tool_review_page(tool_name: str) -> air.Html:
    """
    Creates an individual tool review page with markdown content.
    
    Args:
        tool_name: The name of the tool review to display
        
    Returns:
        An Air Html component for the tool review page
    """
    # Load markdown content
    content_path = f"content/tool-reviews/{tool_name}.md"
    
    try:
        markdown_content = open(content_path, 'r', encoding='utf-8').read()
    except FileNotFoundError:
        markdown_content = f"# Tool Review Not Found\n\nThe tool review for '{tool_name}' could not be found."
    
    # Determine the social card image based on tool name
    tool_image_map = {
        "amp": "/static/AmpToolReview.png",
        "cursor": "/static/CursorToolReview.png",
        "gemini-cli": "/static/GeminiCliToolReview.png"
    }
    social_image = tool_image_map.get(tool_name, "/static/CourseCard.jpg")
    
    return base_layout(
        f"{tool_name.replace('-', ' ').title()} Tool Review - Isaac Flath & Eleanor Berger",
        f"Detailed review of {tool_name.replace('-', ' ')} AI coding tool with real-world testing and insights.",
        social_image,
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
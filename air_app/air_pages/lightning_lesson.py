import air
from air_markdown import Markdown
from components.layout import base_layout
import os

def lightning_lesson_page(lesson_name: str) -> air.Html:
    """
    Creates an individual lightning lesson page with markdown content.
    
    Args:
        lesson_name: The name of the lightning lesson to display
        
    Returns:
        An Air Html component for the lightning lesson page
    """
    # Load markdown content
    content_path = f"content/lightning-lessons/{lesson_name}.md"
    
    try:
        markdown_content = open(content_path, 'r', encoding='utf-8').read()
    except FileNotFoundError:
        markdown_content = f"# Lightning Lesson Not Found\n\nThe lightning lesson '{lesson_name}' could not be found."
    
    return base_layout(
        f"{lesson_name.replace('-', ' ').title()} - Lightning Lessons",
        f"Lightning lesson on {lesson_name.replace('-', ' ')}",
        "/static/default-social.png",
        air.Main(
            air.Div(
                air.Div(
                    # Breadcrumb navigation
                    air.Div(
                        air.Div(
                            air.A("Home", href="/", class_="link link-hover"),
                            air.Span("/", class_="mx-2 text-base-content/60"),
                            air.A("Lightning Lessons", href="/lightning-lessons", class_="link link-hover"),
                            air.Span("/", class_="mx-2 text-base-content/60"),
                            air.Span(lesson_name.replace('-', ' ').title(), class_="text-base-content/60"),
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
                    
                    # Back to lessons button
                    air.Div(
                        air.A(
                            "← Back to Lightning Lessons",
                            href="/lightning-lessons",
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
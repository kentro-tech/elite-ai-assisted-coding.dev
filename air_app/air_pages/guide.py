import air
from air_markdown import Markdown
from components.layout import base_layout
import os
import re

def process_markdown_content(content: str) -> str:
    """
    Process markdown content to remove any automatic table of contents.
    """
    # Remove any existing TOC sections
    content = re.sub(r'## Contents.*?(?=##|\Z)', '', content, flags=re.DOTALL)
    content = re.sub(r'# Contents.*?(?=##|\Z)', '', content, flags=re.DOTALL)
    return content.strip()

def guide_page(guide_name: str) -> air.Html:
    """
    Creates an individual guide page with markdown content.
    
    Args:
        guide_name: The name of the guide to display
        
    Returns:
        An Air Html component for the guide page
    """
    # Load markdown content
    content_path = f"content/guides/{guide_name}.md"
    
    try:
        with open(content_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
            markdown_content = process_markdown_content(raw_content)
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
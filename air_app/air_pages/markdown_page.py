import air
from air_markdown import Markdown
from typing import List, Optional

def markdown_page(
    title: str,
    content: str,
    description: str = "",
    categories: Optional[List[str]] = None,
    date: Optional[str] = None,
    image: Optional[str] = None
) -> air.Html:
    """
    Creates a page with markdown content.
    
    Args:
        title: Page title
        content: Markdown content
        description: Page description
        categories: List of categories
        date: Publication date
        image: Featured image path
        
    Returns:
        An Air Html component
    """
    categories = categories or []
    
    # Create category badges
    category_badges = [
        air.Span(category, class_="badge badge-primary badge-outline mr-1")
        for category in categories
    ]
    
    # Create the page
    return air.Html(
        air.Head(
            air.Title(title),
            air.Meta(name="description", content=description),
        ),
        air.Body(
            air.Div(
                # Header
                air.Div(
                    air.H1(title, class_="text-4xl font-bold mb-4"),
                    
                    # Categories
                    air.Div(*category_badges, class_="flex flex-wrap gap-2 mb-4") if categories else "",
                    
                    # Date
                    air.Div(f"Published: {date}", class_="text-sm text-gray-500 mb-6") if date else "",
                    
                    # Featured image
                    air.Img(src=image, alt=title, class_="w-full rounded-lg shadow-lg mb-8") if image else "",
                    
                    class_="mb-8"
                ),
                
                # Content with Markdown
                air.Div(
                    Markdown(content),
                    class_="prose max-w-none"
                ),
                
                class_="max-w-4xl mx-auto"
            ),
            class_="container mx-auto px-4 py-8"
        )
    )
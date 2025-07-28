import air
from air_markdown import Markdown
from typing import Optional

def markdown_content(content: str, class_name: Optional[str] = None) -> air.Div:
    """
    Renders markdown content using air-markdown.
    
    Args:
        content: Markdown content to render
        class_name: Optional CSS class to apply to the container
        
    Returns:
        An Air Div component with rendered markdown
    """
    return air.Div(
        Markdown(content),
        class_=f"prose max-w-none {class_name or ''}"
    )
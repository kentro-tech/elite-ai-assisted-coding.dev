import air
from typing import Optional, List

def tool_card(title: str, description: str, image_path: Optional[str] = None, 
              categories: Optional[List[str]] = None, date: Optional[str] = None, 
              url: str = "#") -> air.Div:
    """
    Creates a card component for tool reviews or guides.
    
    Args:
        title: The title of the card
        description: The description text
        image_path: Optional path to the image
        categories: Optional list of categories
        date: Optional date string
        url: The URL to link to
    
    Returns:
        An Air Div component representing the card
    """
    # Create category badges if categories are provided
    category_badges = []
    if categories:
        for category in categories:
            category_badges.append(
                air.Span(category, class_="badge badge-primary badge-outline mr-1")
            )
    
    # Create the card content
    card_content = [
        air.H2(title, class_="card-title"),
        air.P(description, class_="line-clamp-3"),
        air.Div(class_="flex flex-wrap gap-2 mt-2", *category_badges),
        air.Div(
            class_="card-actions justify-between items-center mt-4",
            air.Small(date) if date else None,
            air.A(
                air.Button("Read More", class_="btn btn-primary"),
                href=url
            )
        )
    ]
    
    return air.Div(
        class_="card bg-base-100 shadow-xl hover:shadow-2xl transition-shadow duration-300",
        air.Figure(
            air.Img(src=image_path, alt=title, class_="rounded-t-lg w-full h-48 object-cover")
        ),
        air.Div(class_="card-body", *card_content)
    )
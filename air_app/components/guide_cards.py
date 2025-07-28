import air
from typing import List, Dict, Any

# Sample guide data - in a real app this would come from a database
GUIDES_DATA = [
    {
        "id": "context-personalization-101",
        "title": "Optimize Your Dev Setup For Evals w/ Cursor Rules & MCP",
        "description": "Learn to optimize your dev environment with AI tools using Cursor Rules and Model Context Protocol",
        "image": "/static/CursorRulesOptions.png",
        "categories": ["Context", "Personalization"],
        "date": "2025-07-15",
        "url": "/guides/context-personalization-101"
    }
]

def guide_card(guide: Dict[str, Any]) -> air.Div:
    """
    Creates a single guide card component.
    
    Args:
        guide: Dictionary containing guide information
        
    Returns:
        An Air Div component representing a guide card
    """
    # Create category badges
    category_badges = [
        air.Span(category, class_="badge badge-primary badge-outline mr-1")
        for category in guide["categories"]
    ]
    
    return air.Div(
        air.Figure(
            air.A(
                air.Img(
                    src=guide["image"],
                    alt=guide["title"],
                    class_="w-full h-48 object-cover transition-transform duration-300 hover:scale-105"
                ),
                href=guide["url"],
                class_="block"
            ),
            class_="overflow-hidden"
        ),
        air.Div(
            air.H2(guide["title"], class_="card-title text-lg font-bold mb-2"),
            air.P(guide["description"], class_="text-base-content/70 mb-4 line-clamp-3"),
            air.Div(
                *category_badges,
                class_="flex flex-wrap gap-2 mb-4"
            ),
            air.Div(
                air.Small(guide["date"], class_="text-base-content/60"),
                air.A(
                    "Read Guide →",
                    href=guide["url"],
                    class_="btn btn-primary btn-sm"
                ),
                class_="card-actions justify-between items-center"
            ),
            class_="card-body p-6"
        ),
        class_="card bg-base-100 shadow-lg hover:shadow-xl transition-all duration-300 border border-base-200 hover:border-primary/20"
    )

def get_filtered_guide_cards(search: str = "", category: str = "all", sort: str = "date-desc", limit: int = None) -> str:
    """
    Returns filtered and sorted guide cards as HTML string for HTMX.
    
    Args:
        search: Search term to filter by
        category: Category to filter by
        sort: Sort order
        
    Returns:
        HTML string of filtered guide cards
    """
    # Filter guides
    filtered_guides = GUIDES_DATA.copy()
    
    if search:
        search_lower = search.lower()
        filtered_guides = [
            guide for guide in filtered_guides
            if search_lower in guide["title"].lower() or search_lower in guide["description"].lower()
        ]
    
    if category != "all":
        filtered_guides = [
            guide for guide in filtered_guides 
            if category in guide["categories"]
        ]
    
    # Sort guides
    if sort == "date-desc":
        filtered_guides.sort(key=lambda x: x["date"], reverse=True)
    elif sort == "date-asc":
        filtered_guides.sort(key=lambda x: x["date"])
    elif sort == "title-asc":
        filtered_guides.sort(key=lambda x: x["title"])
    elif sort == "title-desc":
        filtered_guides.sort(key=lambda x: x["title"], reverse=True)
    
    # Apply limit if specified
    if limit is not None:
        filtered_guides = filtered_guides[:limit]
        
    # Create cards
    cards = [guide_card(guide) for guide in filtered_guides]
    
    # Return as HTML string
    if not cards:
        return air.Div(
            air.P("No guides found matching your criteria.", class_="text-center text-gray-500 py-8"),
            class_="col-span-full"
        ).render()
    
    return "".join([card.render() for card in cards])

def guide_cards_grid() -> air.Div:
    """
    Creates the guide cards grid container with HTMX functionality.
    
    Returns:
        An Air Div component with the guide cards grid
    """
    return air.Div(
        # Filter Controls
        air.Div(
            air.Div(
                air.Label(
                    air.Input(
                        type="text",
                        placeholder="Search guides...",
                        class_="input input-bordered pr-12",
                        name="search",
                        hx_get="/partials/guide-cards",
                        hx_target="#guide-cards-container",
                        hx_trigger="keyup changed delay:300ms",
                        hx_include="[name='category'], [name='sort']"
                    ),
                    air.Span(
                        air.svg.Svg(
                            air.svg.Path(
                                stroke_linecap="round",
                                stroke_linejoin="round",
                                stroke_width="2",
                                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            class_="h-5 w-5",
                            fill="none",
                            viewBox="0 0 24 24",
                            stroke="currentColor"
                        ),
                        class_="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none text-base-content/50"
                    ),
                    class_="relative"
                ),
                class_="form-control"
            ),
            
            air.Select(
                air.Option("All Categories", value="all"),
                air.Option("Context", value="Context"),
                air.Option("Personalization", value="Personalization"),
                air.Option("Tools", value="Tools"),
                name="category",
                class_="select select-bordered",
                hx_get="/partials/guide-cards",
                hx_target="#guide-cards-container",
                hx_trigger="change",
                hx_include="[name='search'], [name='sort']"
            ),
            
            air.Select(
                air.Option("Newest First", value="date-desc"),
                air.Option("Oldest First", value="date-asc"),
                air.Option("Title (A-Z)", value="title-asc"),
                air.Option("Title (Z-A)", value="title-desc"),
                name="sort",
                class_="select select-bordered",
                hx_get="/partials/guide-cards",
                hx_target="#guide-cards-container",
                hx_trigger="change",
                hx_include="[name='search'], [name='category']"
            ),
            
            class_="flex flex-wrap gap-4 mb-8"
        ),
        
        # Loading indicator
        air.Div(
            air.Span("Loading...", class_="loading loading-spinner loading-md"),
            class_="htmx-indicator flex justify-center py-8"
        ),
        
        # Guide Cards Container
        air.Div(
            *[guide_card(guide) for guide in GUIDES_DATA],
            id="guide-cards-container",
            class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12"
        ),
        
        class_="max-w-6xl mx-auto"
    )
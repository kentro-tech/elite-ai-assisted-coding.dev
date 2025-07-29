import air
from typing import List, Dict, Any

# Sample tool data - in a real app this would come from a database
TOOLS_DATA = [
    # {
    #     "id": "openhands",
    #     "title": "Open Hands Tool Review",
    #     "description": "Web based AI coding agent with real-time collaboration and code generation",
    #     "image": "/static/OpenHandsToolReview.png",
    #     "category": "Web",
    #     "date": "2025-07-28",
    #     "url": "/tool-reviews/openhands"
    # },
    {
        "id": "cursor",
        "title": "Cursor Tool Review",
        "description": "IDE capabilities, tab completion, background agents, integrations, and terminal assistance",
        "image": "/static/CursorToolReview.png",
        "category": "IDE",
        "date": "2025-07-22",
        "url": "/tool-reviews/cursor"
    },
    {
        "id": "gemini-cli",
        "title": "Gemini CLI Tool Review", 
        "description": "Command-line interface for Gemini AI with code generation and assistance features",
        "image": "/static/GeminiCliToolReview.png",
        "category": "CLI",
        "date": "2025-07-15",
        "url": "/tool-reviews/gemini-cli"
    },
    {
        "id": "amp",
        "title": "AMP Tool Review",
        "description": "Web-based AI assistant for developers with collaborative features",
        "image": "/static/AmpToolReview.png", 
        "category": "Web",
        "date": "2025-07-10",
        "url": "/tool-reviews/amp"
    },

]

def tool_card(tool: Dict[str, Any]) -> air.Div:
    """
    Creates a single tool card component.
    
    Args:
        tool: Dictionary containing tool information
        
    Returns:
        An Air Div component representing a tool card
    """
    return air.Div(
        air.Figure(
            air.A(
                air.Img(
                    src=tool["image"],
                    alt=tool["title"],
                    class_="w-full h-48 object-cover transition-transform duration-300 hover:scale-105"
                ),
                href=tool["url"],
                class_="block"
            ),
            class_="overflow-hidden"
        ),
        air.Div(
            air.H2(tool["title"], class_="card-title text-lg font-bold mb-2"),
            air.P(tool["description"], class_="text-base-content/70 mb-4 line-clamp-3"),
            air.Div(
                air.Span(tool["category"], class_="badge badge-primary badge-outline"),
                class_="flex flex-wrap gap-2 mb-4"
            ),
            air.Div(
                air.Small(tool["date"], class_="text-base-content/60"),
                air.A(
                    "Read More →",
                    href=tool["url"],
                    class_="btn btn-primary btn-sm"
                ),
                class_="card-actions justify-between items-center"
            ),
            class_="card-body p-6"
        ),
        class_="card bg-base-100 shadow-lg hover:shadow-xl transition-all duration-300 border border-base-200 hover:border-primary/20"
    )

def get_filtered_tool_cards(search: str = "", category: str = "all", sort: str = "date-desc", limit: int = None) -> str:
    """
    Returns filtered and sorted tool cards as HTML string for HTMX.
    
    Args:
        search: Search term to filter by
        category: Category to filter by
        sort: Sort order
        
    Returns:
        HTML string of filtered tool cards
    """
    # Filter tools
    filtered_tools = TOOLS_DATA.copy()
    
    if search:
        search_lower = search.lower()
        filtered_tools = [
            tool for tool in filtered_tools
            if search_lower in tool["title"].lower() or search_lower in tool["description"].lower()
        ]
    
    if category != "all":
        filtered_tools = [tool for tool in filtered_tools if tool["category"] == category]
    
    # Sort tools
    if sort == "date-desc":
        filtered_tools.sort(key=lambda x: x["date"], reverse=True)
    elif sort == "date-asc":
        filtered_tools.sort(key=lambda x: x["date"])
    elif sort == "title-asc":
        filtered_tools.sort(key=lambda x: x["title"])
    elif sort == "title-desc":
        filtered_tools.sort(key=lambda x: x["title"], reverse=True)
    
    # Apply limit if specified
    if limit is not None:
        filtered_tools = filtered_tools[:limit]
        
    # Create cards
    cards = [tool_card(tool) for tool in filtered_tools]
    
    # Return as HTML string
    if not cards:
        return air.Div(
            air.P("No tools found matching your criteria.", class_="text-center text-gray-500 py-8"),
            class_="col-span-full"
        ).render()
    
    return "".join([card.render() for card in cards])

def tool_cards_grid() -> air.Div:
    """
    Creates the tool cards grid container with HTMX functionality.
    
    Returns:
        An Air Div component with the tool cards grid
    """
    return air.Div(
        # Filter Controls
        air.Div(
            air.Div(
                air.Label(
                    air.Input(
                        type="text",
                        placeholder="Search tools...",
                        class_="input input-bordered pr-12",
                        name="search",
                        hx_get="/partials/tool-cards",
                        hx_target="#tool-cards-container",
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
                air.Option("IDE", value="IDE"),
                air.Option("CLI", value="CLI"),
                air.Option("Web", value="Web"),
                name="category",
                class_="select select-bordered",
                hx_get="/partials/tool-cards",
                hx_target="#tool-cards-container",
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
                hx_get="/partials/tool-cards",
                hx_target="#tool-cards-container", 
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
        
        # Tool Cards Container
        air.Div(
            *[tool_card(tool) for tool in TOOLS_DATA],
            id="tool-cards-container",
            class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12"
        ),
        
        class_="max-w-6xl mx-auto"
    )
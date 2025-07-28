import air
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# Create the Air app
app = air.Air()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Import page components
from air_pages.index import index_page
from air_pages.tool_reviews import tool_reviews_page
from air_pages.tool_review import tool_review_page
from air_pages.guides import guides_page
from air_pages.guide import guide_page

# Routes using Air tags
@app.get("/")
async def index():
    return index_page()

@app.get("/tool-reviews")
async def tool_reviews():
    return tool_reviews_page()

@app.get("/tool-reviews/{tool_name}")
async def tool_review(tool_name: str):
    return tool_review_page(tool_name)

@app.get("/guides")
async def guides():
    return guides_page()

@app.get("/guides/{guide_name}")
async def guide(request: Request, guide_name: str):
    # Use the Air component for all guides
    return guide_page(guide_name)

# HTMX partial endpoints
@app.get("/partials/tool-cards")
async def tool_cards_partial(search: str = "", category: str = "all", sort: str = "date-desc", limit: int = None):
    from components.tool_cards import get_filtered_tool_cards
    return HTMLResponse(get_filtered_tool_cards(search, category, sort, limit))

@app.get("/partials/guide-cards")
async def guide_cards_partial(search: str = "", category: str = "all", sort: str = "date-desc", limit: int = None):
    from components.guide_cards import get_filtered_guide_cards
    return HTMLResponse(get_filtered_guide_cards(search, category, sort, limit))

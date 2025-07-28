import air
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import re
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from bs4 import BeautifulSoup
from air_markdown import Markdown

# Create the Air app
app = air.Air()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates for markdown pages
templates = Jinja2Templates(directory="templates")

# Import page components
from air_pages.index import index_page
from air_pages.tool_reviews import tool_reviews_page
from air_pages.tool_review import tool_review_page
from air_pages.guides import guides_page
from air_pages.guide import guide_page

def extract_toc(html_content):
    """Extract headings and create a table of contents"""
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])
    
    toc = []
    for heading in headings:
        # Create an ID if it doesn't exist
        if not heading.get('id'):
            heading_id = re.sub(r'[^\w-]', '', heading.text.lower().replace(' ', '-'))
            heading['id'] = heading_id
        else:
            heading_id = heading['id']
        
        # Determine the level based on the heading tag
        level = int(heading.name[1]) - 2  # h2 -> 0, h3 -> 1, etc.
        
        toc.append({
            'level': level,
            'text': heading.text,
            'id': heading_id
        })
    
    # Generate HTML for the TOC
    toc_html = '<ul class="menu menu-xs">'
    for item in toc:
        indent = '  ' * item['level']
        toc_html += f'{indent}<li><a href="#{item["id"]}" class="toc-link">{item["text"]}</a></li>'
    toc_html += '</ul>'
    
    return toc_html

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

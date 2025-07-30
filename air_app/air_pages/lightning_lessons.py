import air
from components.layout import base_layout
import os

def lightning_lessons_page() -> air.Html:
    """
    Renders the lightning lessons listing page using Air tags.
    
    Returns:
        An Air Html component representing the lightning lessons page
    """
    # Get all lightning lesson files
    lessons_dir = "content/lightning-lessons"
    lesson_cards = []
    
    if os.path.exists(lessons_dir):
        for filename in sorted(os.listdir(lessons_dir)):
            if filename.endswith('.md'):
                lesson_name = filename[:-3]  # Remove .md extension
                title = lesson_name.replace('-', ' ').title()
                
                lesson_cards.append(
                    air.Div(
                        air.A(
                            air.Div(
                                air.H3(title, class_="card-title text-xl"),
                                class_="card-body"
                            ),
                            href=f"/lightning-lessons/{lesson_name}",
                            class_="block hover:scale-105 transition-transform"
                        ),
                        class_="card bg-base-200 shadow-xl"
                    )
                )
    
    return base_layout(
        "Lightning Lessons",
        "Quick, focused lessons on AI-assisted development",
        "/static/default-social.png",
        air.Div(
            # Hero Section with Gradient Background
            air.Div(
                air.Div(
                    air.H1(
                        "Lightning Lessons",
                        class_="text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent"
                    ),
                    air.P(
                        "Quick, focused lessons on AI-assisted development techniques",
                        class_="text-xl md:text-2xl text-base-content/80 max-w-3xl mx-auto"
                    ),
                    class_="text-center py-16 px-4"
                ),
                class_="bg-gradient-to-b from-base-200 to-base-100 mb-12"
            ),
            
            # Lessons Grid
            air.Div(
                air.Div(*lesson_cards) if lesson_cards else air.P("No lessons available yet.", class_="text-center text-base-content/60"),
                class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
            ),
            
            class_="max-w-6xl mx-auto px-4 py-8"
        )
    )
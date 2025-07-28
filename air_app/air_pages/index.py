import air
from components.layout import base_layout
from components.course_promo import course_promo

def index_page() -> air.Html:
    """
    Renders the index page using Air tags.
    
    Returns:
        An Air Html component representing the index page
    """
    return base_layout(
        "Elite AI Assisted Coding",
        "A review of AI coding tools and practices that actually work and improve your productivity",
        air.Div(
            # Profile Section
            air.Div(
                air.Div(
                    air.Img(
                        src="/static/profile_img.jpg",
                        alt="Isaac Flath",
                        class_="rounded-lg shadow-lg w-full"
                    ),
                    class_="md:col-span-4"
                ),
                air.Div(
                    air.H1(
                        "Hey, I'm Isaac Flath",
                        class_="text-4xl font-bold mb-4"
                    ),
                    air.P(
                        "I've been deep in the AI coding tools space, testing everything from Cursor to Windsurf to see what actually delivers. Just honest reviews and techniques based on real coding sessions.",
                        class_="text-lg"
                    ),
                    class_="md:col-span-8"
                ),
                class_="grid grid-cols-1 md:grid-cols-12 gap-8 mb-12"
            ),
            
            # What You'll Find Here Section
            air.Div(
                air.H2(
                    "What You'll Find Here",
                    class_="text-3xl font-bold mb-6"
                ),
                air.Ul(
                    air.Li(
                        air.Strong("Guides"), ": Universal Techniques and Concepts for using and curating context for AI",
                        class_="text-lg"
                    ),
                    air.Li(
                        air.Strong("Unbiased Reviews"), ": I pay for these tools and try them myself",
                        class_="text-lg"
                    ),
                    air.Li(
                        air.Strong("Real Code Examples"), ": Hear exactly what tasks I used them",
                        class_="text-lg"
                    ),
                    air.Li(
                        air.Strong("Practical Insights"), ": What works, what doesn't, and when to use each tool",
                        class_="text-lg"
                    ),
                    air.Li(
                        air.Strong("Condensed Information"), ": I've condensed the information to the most useful so you don't need to spend hours on every tool to know what's worth your time to try for yourself.",
                        class_="text-lg"
                    ),
                    class_="list-disc list-inside space-y-2 ml-4"
                ),
                class_="mb-12"
            ),
            
            air.Div(class_="divider"),
            
            # Course Promo Section
            course_promo(),
            
            class_="max-w-6xl mx-auto"
        )
    )
import air
from components.layout import base_layout
from components.course_promo import course_promo
from components.tool_cards import tool_cards_grid

def tool_reviews_page() -> air.Html:
    """
    Renders the tool reviews listing page using Air tags.
    
    Returns:
        An Air Html component representing the tool reviews page
    """
    return base_layout(
        "Tool Reviews",
        "Reviews of AI coding tools and practices that actually work and improve your productivity",
        air.Div(
            air.H1("Tool Reviews", class_="text-4xl font-bold mb-4 text-center"),
            air.P(
                "Reviews of AI coding tools and practices that actually work and improve your productivity",
                class_="text-lg text-center mb-8"
            ),
            
            # Course Promo Banner
            air.Div(
                air.Div(
                    air.Div(
                        air.A(
                            air.Img(
                                src="/static/CourseCard.jpg",
                                alt="Course Card",
                                class_="rounded-lg shadow-md max-w-sm w-full"
                            ),
                            href="https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC",
                            class_="block"
                        ),
                        air.Div(
                            air.H2("Want to master AI-assisted coding?", class_="card-title text-2xl mb-4"),
                            air.P("Join my course to learn advanced techniques and patterns that will 10x your productivity with any AI coding tool.", class_="mb-4"),
                            air.A(
                                air.Strong("Enroll Now on Maven →"),
                                href="https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC",
                                class_="btn btn-primary btn-lg"
                            )
                        ),
                        class_="flex flex-col md:flex-row items-center gap-6"
                    ),
                    class_="card-body"
                ),
                class_="card bg-base-200 shadow-xl mb-12"
            ),
            
            # Tool Cards Grid with HTMX
            tool_cards_grid(),
            
            class_="max-w-6xl mx-auto"
        )
    )

def tool_review_page(tool_name: str) -> air.Html:
    """
    Renders an individual tool review page.
    
    Args:
        tool_name: The name of the tool to review
        
    Returns:
        An Air Html component representing the tool review page
    """
    # For now, we'll handle the cursor tool specifically
    if tool_name == "cursor":
        return cursor_review_page()
    else:
        # Return a placeholder for other tools
        return base_layout(
            f"{tool_name.title()} Tool Review",
            f"Review of {tool_name} AI coding tool",
            air.Div(
                air.H1(f"{tool_name.title()} Tool Review", class_="text-4xl font-bold mb-8"),
                air.P(f"Review content for {tool_name} coming soon!", class_="text-lg"),
                class_="max-w-4xl mx-auto"
            )
        )

def cursor_review_page() -> air.Html:
    """
    Renders the Cursor tool review page with table of contents.
    
    Returns:
        An Air Html component representing the Cursor review page
    """
    return base_layout(
        "Cursor Tool Review",
        "IDE capabilities, tab completion, background agents, integrations, and terminal assistance",
        air.Div(
            air.Div(
                # Main Content
                air.Div(
                    air.Div(
                        air.Blockquote(
                            "A technical reference for Cursor's AI-assisted development features",
                            class_="text-xl italic border-l-4 border-primary pl-4 mb-8"
                        ),
                        
                        air.H1("Overview", id="overview", class_="text-3xl font-bold mb-4"),
                        air.P(
                            "Cursor is a fork of VS Code that integrates AI assistance throughout the development workflow. "
                            "It is worth trying because it is a full IDE that gives a great diff experience on AI changes, "
                            "and is very aggressive with the AI assistance. Cursor is one of the tools I use day-to-day for "
                            "coding and it's a great tool.",
                            class_="mb-6"
                        ),
                        
                        # Course Promo
                        course_promo(),
                        
                        air.H1("Top IDE Features", id="top-ide-features", class_="text-3xl font-bold mb-4 mt-12"),
                        
                        air.H2("Tab Completion", id="tab-completion", class_="text-2xl font-bold mb-4"),
                        air.P(
                            "Cursor's completions use project-wide context rather than just the current file and are very aggressive, "
                            "which is good in some situations and annoying in others.",
                            class_="mb-4"
                        ),
                        
                        # Success Alert
                        air.Div(
                            air.Svg(
                                air.Path(
                                    stroke_linecap="round",
                                    stroke_linejoin="round",
                                    stroke_width="2",
                                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                class_="stroke-current shrink-0 h-6 w-6",
                                fill="none",
                                viewBox="0 0 24 24"
                            ),
                            air.Div(
                                air.H3("Helpful Use Case", class_="font-bold"),
                                air.P(
                                    "I was doing an OSS PR to add type hints to a new web development framework called 'air' (very repetitive task). "
                                    "These needed to be matched up to a HTML reference documentation, and agents kept leaving off or added tags. "
                                    "Cursor's tab completion let me copy/paste from reference docs then hit tab for it to tab complete and modify to python syntax very quickly. "
                                    "It got the pattern after the first couple and let me get through it all in very little time."
                                )
                            ),
                            class_="alert alert-success my-4"
                        ),
                        
                        # Warning Alert
                        air.Div(
                            air.Svg(
                                air.Path(
                                    stroke_linecap="round",
                                    stroke_linejoin="round",
                                    stroke_width="2",
                                    d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                class_="stroke-current shrink-0 h-6 w-6",
                                fill="none",
                                viewBox="0 0 24 24"
                            ),
                            air.Div(
                                air.H3("Unhelpful Use Case", class_="font-bold"),
                                air.P(
                                    "I was working on creating examples for a workshop I was teaching on FastHTML Syntax and Project Organization. "
                                    "The tab completion was extremely annoying, because it was project wide it kept trying to autocomplete and change my code to what I did somewhere else. "
                                    "I felt like I was fighting the tab completion constantly and having to keep telling it to go away A LOT because I had a very specific thing in mind I wanted to do."
                                )
                            ),
                            class_="alert alert-warning my-4"
                        ),
                        
                        air.H2("Chat/Agent Interface (Cmd+L Cmd+I)", id="chat-agent-interface", class_="text-2xl font-bold mb-4"),
                        air.P(
                            "Context-aware chat that understands project structure. This is pretty helpful with being able to easily reference lots of things with the @ syntax for files. "
                            "If you have code highlighted when you engage it that will be included in context specifically, and open files will also be in context for you.",
                            class_="mb-4"
                        ),
                        
                        # More content would continue here...
                        
                        class_="prose prose-lg max-w-none"
                    ),
                    class_="lg:col-span-3"
                ),
                
                # Table of Contents Sidebar
                air.Div(
                    air.Div(
                        air.H3("Table of Contents", class_="text-lg font-bold mb-2"),
                        air.Ul(
                            air.Li(air.A("Overview", href="#overview", class_="toc-link hover:text-primary transition-colors")),
                            air.Li(air.A("Top IDE Features", href="#top-ide-features", class_="toc-link hover:text-primary transition-colors")),
                            air.Li(air.A("Tab Completion", href="#tab-completion", class_="toc-link ml-4 hover:text-primary transition-colors")),
                            air.Li(air.A("Chat/Agent Interface", href="#chat-agent-interface", class_="toc-link ml-4 hover:text-primary transition-colors")),
                            class_="space-y-1"
                        ),
                        class_="sticky top-4 p-4 bg-base-100 rounded-lg shadow-md"
                    ),
                    class_="lg:col-span-1"
                ),
                
                class_="grid grid-cols-1 lg:grid-cols-4 gap-8"
            ),
            class_="max-w-6xl mx-auto"
        )
    )
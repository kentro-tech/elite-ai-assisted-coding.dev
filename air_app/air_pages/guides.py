import air
from components.layout import base_layout
from components.course_promo import course_promo
from components.guide_cards import guide_cards_grid

def guides_page() -> air.Html:
    """
    Renders the guides listing page using Air tags.
    
    Returns:
        An Air Html component representing the guides page
    """
    return base_layout(
        "Guides",
        "Universal Techniques and Concepts for using and curating context for AI",
        air.Div(
            air.H1("Guides", class_="text-4xl font-bold mb-4 text-center"),
            air.P(
                "Universal Techniques and Concepts for using and curating context for AI",
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
            
            # Guide Cards Grid with HTMX
            guide_cards_grid(),
            
            class_="max-w-6xl mx-auto"
        )
    )

def guide_page(guide_name: str) -> air.Html:
    """
    Renders an individual guide page.
    
    Args:
        guide_name: The name of the guide
        
    Returns:
        An Air Html component representing the guide page
    """
    # For now, we'll handle the context personalization guide specifically
    if guide_name == "context-personalization-101":
        return context_personalization_guide()
    else:
        # Return a placeholder for other guides
        return base_layout(
            f"{guide_name.replace('-', ' ').title()} Guide",
            f"Guide on {guide_name.replace('-', ' ')}",
            air.Div(
                air.H1(f"{guide_name.replace('-', ' ').title()} Guide", class_="text-4xl font-bold mb-8"),
                air.P(f"Guide content for {guide_name} coming soon!", class_="text-lg"),
                class_="max-w-4xl mx-auto"
            )
        )

def context_personalization_guide() -> air.Html:
    """
    Renders the context personalization guide with table of contents.
    
    Returns:
        An Air Html component representing the guide page
    """
    return base_layout(
        "Optimize Your Dev Setup For Evals w/ Cursor Rules & MCP",
        "Learn to optimize your dev environment with AI tools using Cursor Rules and Model Context Protocol",
        air.Div(
            air.Div(
                # Main Content
                air.Div(
                    air.Div(
                        air.H1("Optimize Your Dev Setup For Evals w/ Cursor Rules & MCP", class_="text-3xl font-bold mb-6"),
                        
                        air.P(
                            "This is a guide to help you optimize your dev setup to get the most out of AI. "
                            "It's showed with specific examples for eval frameworks, but the concepts are universally applicable to any tool. "
                            "It's a guide to help you understand the different layers of context and how to use them to your advantage for your AI tools.",
                            class_="mb-4"
                        ),
                        
                        air.P(
                            "This content was originally created and taught as part of Hamel and Shreya's AI Evals Course on Maven (30% off with that link!). "
                            "If you are building AI tools or products, it's a must-take course.",
                            class_="mb-6"
                        ),
                        
                        # Course Promo
                        course_promo(),
                        
                        air.H2("Why bother?", id="why-bother", class_="text-2xl font-bold mb-4 mt-8"),
                        air.Ul(
                            air.Li("Better AI assistance"),
                            air.Li("Training cutoff may mean outdated info"),
                            air.Li("Spending time determining what's important to your project is good - Forces you to understand your tools better"),
                            air.Li("Make AI better match your taste"),
                            air.Li("Show how AI integrates with your other tools, abstractions, or framework"),
                            class_="list-disc list-inside space-y-2 ml-4 mb-6"
                        ),
                        
                        air.H2("The Three Layers", id="the-three-layers", class_="text-2xl font-bold mb-4"),
                        air.Ol(
                            air.Li(
                                air.Strong("General Context"), ": Generic tool that works on almost anything",
                                air.Ul(
                                    air.Li("Repomix, GitMCP, etc."),
                                    class_="list-disc list-inside ml-4 mt-2"
                                )
                            ),
                            air.Li(
                                air.Strong("Curated Context"), ": Curated by an expert, such as the tool author",
                                air.Ul(
                                    air.Li("Library provided MCP, llms.txt, etc."),
                                    class_="list-disc list-inside ml-4 mt-2"
                                )
                            ),
                            air.Li(
                                air.Strong("Personalized Context"), ": Context that you can create that's unique to your project",
                                air.Ul(
                                    air.Li("Only you can make this and it's uniquely tailored to your taste and needs"),
                                    class_="list-disc list-inside ml-4 mt-2"
                                )
                            ),
                            class_="list-decimal list-inside space-y-4 ml-4 mb-6"
                        ),
                        
                        air.H2("General Context", id="general-context", class_="text-2xl font-bold mb-4"),
                        air.P(
                            "General context is a good starting point when exploring or unsure about a tool. "
                            "It's generic and not optimized for specific needs. It's fast and easy to set up. "
                            "It's useful for quick experimentation and exploration, but it's not the best for long-term use.",
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
                                air.H3("Good For", class_="font-bold"),
                                air.Ul(
                                    air.Li("Good starting point when exploring or unsure about a tool"),
                                    air.Li("Generic and not optimized for specific needs"),
                                    air.Li("Fast and easy to set up"),
                                    air.Li("Useful for quick experimentation and exploration"),
                                    class_="list-disc list-inside ml-4"
                                )
                            ),
                            class_="alert alert-success my-4"
                        ),
                        
                        # Tab functionality for different tools
                        air.Div(
                            air.A("Braintrust", class_="tab tab-active", onclick="showTab('braintrust')"),
                            air.A("Phoenix", class_="tab", onclick="showTab('phoenix')"),
                            air.A("Inspect", class_="tab", onclick="showTab('inspect')"),
                            class_="tabs tabs-boxed my-6"
                        ),
                        
                        air.Div(
                            air.H3("Repo Mix"),
                            air.P(
                                "RepoMix is a tool that lets you take a github repo and concatenate all the files based on a pattern into a single file. "
                                "This is useful for getting lots of context into a single file that you model can easily understand."
                            ),
                            air.Figure(
                                air.Img(
                                    src="/static/repomix_ui.png",
                                    alt="Repo Mix UI for Braintrust",
                                    class_="rounded-lg shadow-lg"
                                ),
                                air.Figcaption("Repo Mix UI for Braintrust", class_="text-center mt-2")
                            ),
                            id="braintrust",
                            class_="tab-content"
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
                            air.Li(air.A("Why bother?", href="#why-bother", class_="toc-link hover:text-primary transition-colors")),
                            air.Li(air.A("The Three Layers", href="#the-three-layers", class_="toc-link hover:text-primary transition-colors")),
                            air.Li(air.A("General Context", href="#general-context", class_="toc-link hover:text-primary transition-colors")),
                            class_="space-y-1"
                        ),
                        class_="sticky top-4 p-4 bg-base-100 rounded-lg shadow-md"
                    ),
                    class_="lg:col-span-1"
                ),
                
                class_="grid grid-cols-1 lg:grid-cols-4 gap-8"
            ),
            
            # Tab functionality script
            air.Script("""
                function showTab(tabId) {
                    // Hide all tab contents
                    document.querySelectorAll('.tab-content').forEach(content => {
                        content.style.display = 'none';
                    });
                    
                    // Show the selected tab content
                    document.getElementById(tabId).style.display = 'block';
                    
                    // Update active tab
                    document.querySelectorAll('.tabs .tab').forEach(tab => {
                        tab.classList.remove('tab-active');
                    });
                    event.target.classList.add('tab-active');
                }
                
                // Initialize the first tab as active
                document.addEventListener('DOMContentLoaded', function() {
                    showTab('braintrust');
                });
            """),
            
            class_="max-w-6xl mx-auto"
        )
    )
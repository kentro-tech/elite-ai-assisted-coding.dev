import air
from components.layout import base_layout

def index_page() -> air.Html:
    """
    Renders the index page using Air tags.
    
    Returns:
        An Air Html component representing the index page
    """
    return base_layout(
        "Elite AI Assisted Coding - Isaac Flath & Eleanor Berger",
        "Master AI coding tools with real-world reviews and proven techniques from expert instructors",
        "/static/CourseCard.jpg",
        air.Div(
            # Hero Section
            air.Div(
                air.Div(
                    # Profile and Introduction
                    air.Div(
                        air.Div(
                            air.Div(
                                air.Img(
                                    src="/static/profile_img.jpg",
                                    alt="Isaac Flath",
                                    class_="w-32 h-32 md:w-40 md:h-40 rounded-full shadow-xl border-2 border-base-300 object-cover aspect-square"
                                ),
                                air.Img(
                                    src="/static/eleanor.jpg",
                                    alt="Eleanor Berger",
                                    class_="w-32 h-32 md:w-40 md:h-40 rounded-full shadow-xl border-2 border-base-300 object-cover aspect-square"
                                ),
                                class_="flex justify-center gap-4 md:gap-8"
                            ),
                            class_="flex justify-center mb-6"
                        ),
                        air.Div(
                            air.H1(
                                "AI Coding Tools And Techniques that Actually Work",
                                class_="text-4xl md:text-5xl font-bold mb-6 bg-gradient-to-r from-base-content to-base-content/60 bg-clip-text text-transparent"
                            ),
                            air.P(
                                "Hey, we're Isaac Flath and Eleanor Berger. We've spent thousands of hours working with every AI coding tool to find what actually improves productivity. Now, we're sharing our knowledge with you. No hype, just honest insights from real development work.",
                                class_="text-xl md:text-2xl text-base-content/80 mb-8"
                            ),
                            # CTA Buttons
                            air.Div(
                                air.A(
                                    "Browse Tool Reviews",
                                    href="/tool-reviews",
                                    class_="btn btn-primary btn-lg mr-4"
                                ),
                                air.A(
                                    "Start with Guides",
                                    href="/guides",
                                    class_="btn btn-outline btn-lg"
                                ),
                                class_="flex flex-wrap gap-4 justify-center"
                            ),
                            class_="text-center"
                        ),
                        class_="hero-content flex-col items-center gap-8 py-12"
                    ),
                    class_="container mx-auto px-4"
                ),
                class_="hero min-h-[50vh] bg-gradient-to-br from-base-200 to-base-100"
            ),
            
            # Stats Section
            air.Div(
                air.Div(
                    class_="w-full max-w-4xl mx-auto -mt-16 relative z-10"
                ),
                class_="px-4 mb-16"
            ),
            
            # What You'll Find Section - Enhanced with Cards
            air.Div(
                air.H2(
                    "What Makes This Different",
                    class_="text-4xl font-bold mb-12 text-center"
                ),
                air.Div(
                    # Card 1
                    air.Div(
                        air.Div(
                            air.Div(
                                air.svg.Svg(
                                    air.svg.Path(d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                    class_="w-12 h-12 text-primary mb-4",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24"
                                ),
                                air.H3("Real Testing, Real Results", class_="card-title mb-2"),
                                air.P(
                                    "Every review is based on actual development work. We show you exactly what we built and how each tool performed.",
                                    class_="text-base-content/70"
                                ),
                                class_="card-body"
                            ),
                            class_="hover:shadow-xl transition-shadow duration-300"
                        ),
                        class_="card bg-base-200"
                    ),
                    # Card 2
                    air.Div(
                        air.Div(
                            air.Div(
                                air.svg.Svg(
                                    air.svg.Path(d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                    class_="w-10 h-10 text-accent/60 mb-4",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24"
                                ),
                                air.H3("No Affiliate Links", class_="card-title mb-2"),
                                air.P(
                                    "We pay for every tool ourselves. Our reviews are honest because we're not getting paid to promote any of them.",
                                    class_="text-base-content/70"
                                ),
                                class_="card-body"
                            ),
                            class_="hover:shadow-xl transition-shadow duration-300"
                        ),
                        class_="card bg-base-200"
                    ),
                    # Card 3
                    air.Div(
                        air.Div(
                            air.Div(
                                air.svg.Svg(
                                    air.svg.Path(d="M13 10V3L4 14h7v7l9-11h-7z", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                    class_="w-10 h-10 text-success mb-4",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24"
                                ),
                                air.H3("Actionable Insights", class_="card-title mb-2"),
                                air.P(
                                    "Everything is actionable because we're showing how it actually works in real development work we need to do.",
                                    class_="text-base-content/70"
                                ),
                                class_="card-body"
                            ),
                            class_="hover:shadow-xl transition-shadow duration-300"
                        ),
                        class_="card bg-base-200"
                    ),
                    class_="grid md:grid-cols-3 gap-6 mb-16"
                ),
                class_="container mx-auto px-4"
            ),
            
            # Course CTA Section - Premium Design
            air.Div(
                air.Div(
                    air.Div(
                        # Premium Badge
                        air.Div(
                            air.Span("🎓 Maven Course", class_="badge badge-warning badge-lg"),
                            class_="text-center mb-6"
                        ),
                        air.H2(
                            "Ready to 10x Your AI Coding Skills?",
                            class_="text-4xl md:text-5xl font-bold mb-6 text-center"
                        ),
                        air.P(
                            "Join our comprehensive course where we teach everything we've learned about AI-assisted development.",
                            class_="text-xl text-center mb-8 text-base-content/80 max-w-2xl mx-auto"
                        ),
                        # Course Features Grid
                        air.Div(
                            air.Div(
                                air.svg.Svg(
                                    air.svg.Path(d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                    class_="w-8 h-8 text-base-content/70 mb-2",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24"
                                ),
                                air.H4("Real projects", class_="font-bold"),
                                air.P("Applied to real projects with practical value", class_="text-sm text-base-content/70"),
                                class_="text-center"
                            ),
                            air.Div(
                                air.svg.Svg(
                                    air.svg.Path(d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                    class_="w-8 h-8 text-base-content/70 mb-2",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24"
                                ),
                                air.H4("Comprehensive Guides", class_="font-bold"),
                                air.P("Step-by-step instructions with real examples", class_="text-sm text-base-content/70"),
                                class_="text-center"
                            ),
                            air.Div(
                                air.svg.Svg(
                                    air.svg.Path(d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                    class_="w-8 h-8 text-base-content/70 mb-2",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24"
                                ),
                                air.H4("Community Access", class_="font-bold"),
                                air.P("Learn with other developers and direct access to us", class_="text-sm text-base-content/70"),
                                class_="text-center"
                            ),
                            air.Div(
                                air.svg.Svg(
                                    air.svg.Path(d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z", stroke_linecap="round", stroke_linejoin="round", stroke_width="2"),
                                    class_="w-8 h-8 text-base-content/70 mb-2",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24"
                                ),
                                air.H4("One Stop Shop", class_="font-bold"),
                                air.P("All important tool, technique, and strategy in one place", class_="text-sm text-base-content/70"),
                                class_="text-center"
                            ),
                            class_="grid grid-cols-2 md:grid-cols-4 gap-6 mb-8"
                        ),
                        # CTA Button
                        air.Div(
                            air.A(
                                air.Span("Enroll in the Course", class_="mr-2"),
                                air.Span("→", class_="text-xl"),
                                href="https://maven.com/kentro/context-engineering-for-coding?promoCode=AI-CODING",
                                class_="btn btn-warning btn-lg text-base-100 shadow-xl hover:shadow-2xl transform hover:-translate-y-1 transition-all duration-200"
                            ),
                            air.P(
                                air.Span("Use code ", class_="text-sm"),
                                air.Code("AI-CODING", class_="text-sm font-bold"),
                                air.Span(" for exclusive discount", class_="text-sm"),
                                class_="mt-4 text-base-content/60"
                            ),
                            class_="text-center"
                        ),
                        class_="p-12"
                    ),
                    class_="bg-gradient-to-br from-base-200 via-base-300 to-base-200 rounded-3xl shadow-2xl"
                ),
                class_="container mx-auto px-4 mb-16"
            ),
            
            # Quick Links Section
            air.Div(
                air.H2("Start Exploring", class_="text-3xl font-bold mb-8 text-center"),
                air.Div(
                    air.A(
                        air.Div(
                            air.H3("📝 Tool Reviews", class_="text-xl font-bold mb-2"),
                            air.P("In-depth analysis of AI coding tools", class_="text-base-content/70"),
                            class_="card-body"
                        ),
                        href="/tool-reviews",
                        class_="card bg-base-200 hover:bg-base-300 transition-colors"
                    ),
                    air.A(
                        air.Div(
                            air.H3("📚 Guides", class_="text-xl font-bold mb-2"),
                            air.P("Universal techniques for AI coding", class_="text-base-content/70"),
                            class_="card-body"
                        ),
                        href="/guides",
                        class_="card bg-base-200 hover:bg-base-300 transition-colors"
                    ),
                    class_="grid md:grid-cols-2 gap-6"
                ),
                class_="container mx-auto px-4 mb-16"
            ),
            
            class_=""
        )
    )
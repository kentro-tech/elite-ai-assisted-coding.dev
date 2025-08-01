import air
import os
from typing import List, Optional

def base_layout(title: str = "Isaac Flath & Eleanor Berger", 
                description: str = "Master AI-assisted coding with expert guidance from industry leaders",
                image: str = "/static/CourseCard.jpg",
                *content) -> air.Html:
    """
    Creates the base layout for all pages using Air tags.
    
    Args:
        title: Page title
        description: Page description for meta tag
        image: Path to social card image
        *content: Page content elements
    
    Returns:
        Complete HTML page with DaisyUI styling and HTMX
    """
    # Get base URL from environment or use default
    base_url = 'https://elite-ai-assisted-coding.dev'
    
    # Ensure image URL is absolute
    if image.startswith('/'):
        image_url = f"{base_url}{image}"
    else:
        image_url = image
    return air.Html(
        air.Head(
            air.Meta(charset="UTF-8"),
            air.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            air.Title(title),
            air.Meta(name="description", content=description),
            
            # Open Graph / Facebook
            air.Meta(property="og:type", content="website"),
            air.Meta(property="og:url", content=base_url),
            air.Meta(property="og:title", content=title),
            air.Meta(property="og:description", content=description),
            air.Meta(property="og:image", content=image_url),
            air.Meta(property="og:image:width", content="1200"),
            air.Meta(property="og:image:height", content="630"),
            air.Meta(property="og:site_name", content="Elite AI-Assisted Coding"),
            
            # Twitter Card
            air.Meta(name="twitter:card", content="summary_large_image"),
            air.Meta(name="twitter:title", content=title),
            air.Meta(name="twitter:description", content=description),
            air.Meta(name="twitter:image", content=image_url),
            air.Meta(name="twitter:site", content="@isaac_flath"),
            air.Meta(name="twitter:creator", content="@isaac_flath"),
            
            # DaisyUI and Tailwind CSS via CDN
            air.Link(href="https://cdn.jsdelivr.net/npm/daisyui@4.7.2/dist/full.min.css", rel="stylesheet", type="text/css"),
            air.Script(src="https://cdn.tailwindcss.com"),
            
            # HTMX
            air.Script(src="https://unpkg.com/htmx.org@1.9.10"),
            
            # Configure Tailwind and DaisyUI
            air.Script("""
                tailwind.config = {
                    theme: {
                        extend: {},
                    },
                    daisyui: {
                        themes: ["light"],
                        base: true,
                        styled: true,
                        utils: true,
                    },
                }
            """),
            
            # Custom CSS
            air.Link(href="/static/css/custom.css", rel="stylesheet", type="text/css")
        ),
        air.Body(
            # Navbar
            navbar(),
            
            # Main Content
            air.Main(
                air.Div(
                    *content,
                    class_="container mx-auto px-4 py-8"
                ),
                class_="min-h-screen"
            ),
            
            # Footer
            footer(),
            
            data_theme="light"
        )
    )

def navbar() -> air.Div:
    """Creates the navigation bar component following DaisyUI best practices."""
    return air.Div(
        air.Div(
            # Mobile menu button and brand
            air.Div(
                # Mobile dropdown menu
                air.Div(
                    air.Div(
                        air.svg.Svg(
                            air.svg.Path(
                                d="M4 6h16M4 12h8m-8 6h16",
                                stroke_linecap="round",
                                stroke_linejoin="round",
                                stroke_width="2"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            class_="h-5 w-5",
                            fill="none",
                            viewBox="0 0 24 24",
                            stroke="currentColor"
                        ),
                        tabindex="0",
                        role="button",
                        class_="btn btn-ghost lg:hidden"
                    ),
                    air.Ul(
                        air.Li(air.A("Home", href="/")),
                        air.Li(air.A("Tool Reviews", href="/tool-reviews")),
                        air.Li(air.A("Guides", href="/guides")),
                        tabindex="0",
                        class_="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow"
                    ),
                    class_="dropdown"
                ),
                # Brand/Logo
                air.A("Isaac & Eleanor", href="/", class_="btn btn-ghost text-xl font-bold"),
                class_="navbar-start"
            ),
            
            # Desktop menu
            air.Div(
                air.Ul(
                    air.Li(air.A("Home", href="/", class_="hover:bg-base-200 rounded-lg")),
                    air.Li(air.A("Tool Reviews", href="/tool-reviews", class_="hover:bg-base-200 rounded-lg")),
                    air.Li(air.A("Guides", href="/guides", class_="hover:bg-base-200 rounded-lg")),
                    class_="menu menu-horizontal px-1 gap-2"
                ),
                class_="navbar-end hidden lg:flex"
            ),
            class_="container mx-auto px-4"
        ),
        class_="navbar bg-base-100 shadow-lg sticky top-0 z-50"
    )

def footer() -> air.Footer:
    """Creates the footer component."""
    return air.Footer(
        air.Div(
            air.P("Isaac Flath & Eleanor Berger", class_="text-lg font-semibold mb-4"),
            air.P("Expert instructors in AI-assisted coding", class_="text-base-content/70")
        ),
        air.Div(
            air.H3("Connect with us", class_="text-base font-semibold mb-4"),
            air.Div(
                # Isaac's social links
                air.Div(
                    air.P("Isaac Flath", class_="font-medium mb-2"),
                    air.Div(
                        air.A(
                            air.svg.Svg(
                                air.svg.Path(d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewBox="0 0 24 24",
                                class_="fill-current"
                            ),
                            air.Span("LinkedIn", class_="sr-only"),
                            href="https://linkedin.com/in/isaacflath/",
                            class_="link link-hover"
                        ),
                        # air.A(
                        #     air.svg.Svg(
                        #         air.svg.Path(d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"),
                        #         xmlns="http://www.w3.org/2000/svg",
                        #         width="24",
                        #         height="24",
                        #         viewBox="0 0 24 24",
                        #         class_="fill-current"
                        #     ),
                        #     # air.Span("GitHub", class_="sr-only"),
                        #     # href="https://github.com/kentro-tech",
                        #     # class_="link link-hover"
                        # ),
                        air.A(
                            air.svg.Svg(
                                air.svg.Path(d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewBox="0 0 24 24",
                                class_="fill-current"
                            ),
                            air.Span("Twitter", class_="sr-only"),
                            href="https://twitter.com/isaac_flath",
                            class_="link link-hover"
                        ),
                        class_="flex gap-12"
                    )
                ),
                # Eleanor's social links
                air.Div(
                    air.P("Eleanor Berger", class_="font-medium mb-2"),
                    air.Div(
                        air.A(
                            air.svg.Svg(
                                air.svg.Path(d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewBox="0 0 24 24",
                                class_="fill-current"
                            ),
                            air.Span("LinkedIn", class_="sr-only"),
                            href="https://www.linkedin.com/in/intellectronica/",
                            class_="link link-hover"
                        ),
                        air.A(
                            air.svg.Svg(
                                air.svg.Path(d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewBox="0 0 24 24",
                                class_="fill-current"
                            ),
                            air.Span("Twitter", class_="sr-only"),
                            href="https://twitter.com/intellectronica",
                            class_="link link-hover"
                        ),
                        class_="flex gap-12"
                    )
                ),
                class_="grid grid-cols-1 md:grid-cols-2 gap-8"
            )
        ),
        class_="footer footer-center p-10 bg-base-200 text-base-content"
    )
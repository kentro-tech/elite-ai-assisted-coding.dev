import air
from typing import List, Tuple, Optional

def table_of_contents(items: List[Tuple[str, str, Optional[int] = 0]]) -> air.Div:
    """
    Creates a table of contents component with scrollspy functionality.
    
    Args:
        items: List of tuples containing (id, title, level) where level is the indentation level
               (0 for top level, 1 for first level indent, etc.)
    
    Returns:
        An Air Div component representing the table of contents
    """
    toc_items = []
    
    for item_id, title, level in items:
        indent_class = f"ml-{level * 4}" if level > 0 else ""
        toc_items.append(
            air.Li(
                air.A(
                    title, 
                    href=f"#{item_id}", 
                    class_=f"toc-link {indent_class} hover:text-primary transition-colors",
                    hx_get=f"##{item_id}",
                    hx_trigger="click",
                    hx_target="body",
                    hx_swap="none"
                )
            )
        )
    
    return air.Div(
        class_="sticky top-4 p-4 bg-base-100 rounded-lg shadow-md",
        air.H3("Table of Contents", class_="text-lg font-bold mb-2"),
        air.Ul(
            class_="space-y-1",
            *toc_items
        ),
        # Add scrollspy JavaScript
        air.Script("""
            document.addEventListener('DOMContentLoaded', function() {
                const tocLinks = document.querySelectorAll('.toc-link');
                const sections = Array.from(tocLinks).map(link => {
                    const id = link.getAttribute('href').substring(1);
                    return document.getElementById(id);
                }).filter(section => section !== null);
                
                function highlightTocLink() {
                    const scrollPosition = window.scrollY;
                    
                    // Find the section that is currently in view
                    let currentSection = sections[0];
                    for (const section of sections) {
                        if (section.offsetTop <= scrollPosition + 100) {
                            currentSection = section;
                        }
                    }
                    
                    // Highlight the corresponding TOC link
                    tocLinks.forEach(link => {
                        link.classList.remove('text-primary', 'font-bold');
                        if (link.getAttribute('href') === `#${currentSection.id}`) {
                            link.classList.add('text-primary', 'font-bold');
                        }
                    });
                }
                
                window.addEventListener('scroll', highlightTocLink);
                highlightTocLink(); // Initial highlight
            });
        """)
    )
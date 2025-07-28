import air
from typing import Optional

def youtube_embed(video_id: str, title: Optional[str] = None, 
                 width: str = "100%", height: str = "315") -> air.Div:
    """
    Creates a responsive YouTube video embed.
    
    Args:
        video_id: The YouTube video ID
        title: Optional title for the video
        width: Width of the video (default: 100%)
        height: Height of the video (default: 315px)
    
    Returns:
        An Air Div component representing the YouTube embed
    """
    iframe = air.Iframe(
        src=f"https://www.youtube.com/embed/{video_id}",
        title=title or "YouTube video player",
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
        allowfullscreen=True,
        width=width,
        height=height,
        class_="rounded-lg shadow-lg"
    )
    
    # If a title is provided, include it
    if title:
        return air.Div(
            class_="my-6",
            air.H3(title, class_="text-xl font-bold mb-2"),
            air.Div(
                class_="aspect-w-16 aspect-h-9",
                iframe
            )
        )
    else:
        return air.Div(
            class_="my-6 aspect-w-16 aspect-h-9",
            iframe
        )
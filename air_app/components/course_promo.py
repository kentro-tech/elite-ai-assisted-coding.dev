import air

def course_promo(image_path: str = "/static/CourseCard.jpg", 
                promo_code: str = "ISAAC") -> air.Div:
    """
    Creates a course promotion component.
    
    Args:
        image_path: Path to the course image
        promo_code: Promotion code for the course
    
    Returns:
        An Air Div component representing the course promotion
    """
    return air.Div(
        air.H3("Want Even More?", class_="text-2xl font-bold mb-4"),
        air.P(
            "I teach a course on Elite AI Assisted Coding with Eleanor Berger. "
            "Join us to learn the patterns that 10x your productivity with any AI coding tool.",
            class_="mb-4"
        ),
        air.Div(
            air.A(
                air.Img(
                    src=image_path,
                    alt="Course Card",
                    class_="rounded-lg shadow-md max-w-sm w-full"
                ),
                href=f"https://maven.com/kentro/context-engineering-for-coding?promoCode={promo_code}",
                class_="block"
            ),
            air.A(
                "Enroll Now on Maven →",
                href=f"https://maven.com/kentro/context-engineering-for-coding?promoCode={promo_code}",
                class_="btn btn-primary btn-lg"
            ),
            class_="flex flex-col md:flex-row items-center gap-6"
        ),
        class_="my-8 p-6 bg-base-200 rounded-xl shadow-lg"
    )
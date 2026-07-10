def text_aligning(thickness: int, char: str = "H") -> list[str]:
    if thickness < 1 or thickness % 2 == 0:
        raise ValueError("Thickness must be a positive odd number.")

    lines = []

    # Top Cone
    for i in range(thickness):
        lines.append((char * (2 * i + 1)).center(thickness * 2 - 1))

    # Top Pillars
    for _ in range(thickness + 1):
        lines.append(
            (char * thickness).center(thickness * 2)
            + (char * thickness).center(thickness * 6)
        )

    # Middle Belt
    for _ in range((thickness + 1) // 2):
        lines.append((char * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for _ in range(thickness + 1):
        lines.append(
            (char * thickness).center(thickness * 2)
            + (char * thickness).center(thickness * 6)
        )

    # Bottom Cone
    for i in range(thickness):
        lines.append(
            ((char * (2 * (thickness - i) - 1)).center(thickness * 2 - 1))
            .rjust(thickness * 6)
        )

    return lines
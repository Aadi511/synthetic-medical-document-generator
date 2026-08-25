from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

from distortions import (
    random_rotation,
    random_blur,
    add_scanner_noise
)

PRINT_FONTS = [
    r"venv\assets\fonts\Patrick_Hand\PatrickHand-Regular.ttf",
    r"venv\assets\fonts\Schoolbell\Schoolbell-Regular.ttf",
    r"venv\assets\fonts\Architects_Daughter\ArchitectsDaughter-Regular.ttf",
    r"venv\assets\fonts\Coming_Soon\ComingSoon-Regular.ttf",
    r"venv\assets\fonts\Shadows_Into_Light_Two\ShadowsIntoLightTwo-Regular.ttf"
]

CURSIVE_FONTS = [
    r"venv\assets\fonts\Kalam\Kalam-Regular.ttf",
    r"venv\assets\fonts\Caveat\Caveat-VariableFont_wght.ttf",
    r"venv\assets\fonts\Mrs_Sheppards\MrsSheppards-Regular.ttf"
]

SIGNATURE_FONTS = [
    r"venv\assets\fonts\GreatVibes-Regular.ttf",
    r"venv\assets\fonts\Mrs_Sheppards\MrsSheppards-Regular.ttf"
]

HANDWRITING_STYLES = {
    "print": {"font_size_min":70,"font_size_max":90,"rotation_min":-3,"rotation_max":3,"spacing_min":2,"spacing_max":5,"jitter":2},
    "messy_print": {"font_size_min":60,"font_size_max":100,"rotation_min":-12,"rotation_max":12,"spacing_min":-2,"spacing_max":5,"jitter":10},
    "shaky_print": {"font_size_min":65,"font_size_max":95,"rotation_min":-8,"rotation_max":8,"spacing_min":1,"spacing_max":5,"jitter":10},
    "cursive": {"font_size_min":70,"font_size_max":95,"rotation_min":-6,"rotation_max":6,"spacing_min":-2,"spacing_max":2,"jitter":3},
    "signature": {"font_size_min":90,"font_size_max":130,"rotation_min":-12,"rotation_max":12,"spacing_min":-10,"spacing_max":-2,"jitter":14}
}

def get_ink_color():
    palettes = [
        (10,20,random.randint(130,190),255),
        (0,0,random.randint(70,120),255),
        (random.randint(0,20),random.randint(0,20),random.randint(0,20),255),
        (random.randint(50,90),random.randint(50,90),random.randint(50,90),255)
    ]
    return random.choice(palettes)

def signature_variant(name):
    parts = name.split()
    if len(parts) < 2:
        return name
    first, last = parts[0], parts[-1]
    return random.choice([
        f"{first} {last}",
        f"{first[0]}. {last}",
        f"{first[0]} {last}",
        f"{first} {last[0]}.",
        f"{first[0]}{last[0]}",
        f"{first[0]}.{last[0]}."
    ])

def render_handwriting(text, style="print"):
    style_config = HANDWRITING_STYLES[style]

    if style == "signature":
        font_path = random.choice(SIGNATURE_FONTS)
    elif style == "cursive":
        font_path = random.choice(CURSIVE_FONTS)
    else:
        font_path = random.choice(PRINT_FONTS)

    img = Image.new("RGBA", (1800, 400), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    font_size = random.randint(
        style_config["font_size_min"],
        style_config["font_size_max"]
    )

    font = ImageFont.truetype(font_path, font_size)
    ink = get_ink_color()

    if style == "signature":
        text = signature_variant(text)
        x = random.randint(40,70)
        y = random.randint(120,180)

        draw.text((x,y), text, fill=ink, font=font)

        flourish_y = y + random.randint(40,80)
        draw.line(
            (
                x + random.randint(200,350),
                flourish_y,
                x + random.randint(700,1000),
                flourish_y + random.randint(-20,20)
            ),
            fill=ink,
            width=random.randint(1,3)
        )

    elif style == "cursive":
        current_x = 40
        baseline = 160

        for word in text.split():
            word_img = Image.new("RGBA",(900,250),(0,0,0,0))
            word_draw = ImageDraw.Draw(word_img)

            word_draw.text(
                (10,20),
                word,
                fill=ink,
                font=font
            )

            word_img = word_img.rotate(
                random.uniform(-2,2),
                expand=True,
                fillcolor=(0,0,0,0)
            )

            img.alpha_composite(
                word_img,
                (
                    current_x,
                    baseline + random.randint(-4,4)
                )
            )

            current_x += int(font.getlength(word)) + random.randint(20,40)

    else:
        start_x = 40
        baseline = 170

        for char in text:
            if char == " ":
                start_x += random.randint(20,40)
                continue

            jitter = style_config["jitter"]

            draw.text(
                (
                    start_x + random.randint(-jitter,jitter),
                    baseline + random.randint(-jitter,jitter)
                ),
                char,
                fill=ink,
                font=font
            )

            baseline += random.randint(-1,1)

            bbox = font.getbbox(char)
            char_width = bbox[2] - bbox[0]

            start_x += (
                char_width +
                random.randint(
                    style_config["spacing_min"],
                    style_config["spacing_max"]
                )
            )

    pressure = random.random()

    if pressure > 0.8:
        img = img.filter(ImageFilter.MaxFilter(3))
    elif pressure < 0.2:
        img = img.filter(ImageFilter.MinFilter(3))

    img = random_rotation(
        img,
        style_config["rotation_min"],
        style_config["rotation_max"]
    )

    img = random_blur(img)
    img = add_scanner_noise(img)

    return img


if __name__ == "__main__":
    for style in ["print","messy_print","shaky_print","cursive","signature"]:
        img = render_handwriting("Michael Johnson", style)
        img.save(f"test_{style}.png")

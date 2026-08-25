from PIL import Image, ImageDraw, ImageFont
import random

from distortions import (
    random_rotation,
    random_blur,
    add_scanner_noise
)

# =====================================================
# FONT POOLS
# =====================================================

PRINT_FONTS = [
    r"venv\assets\fonts\Patrick_Hand\PatrickHand-Regular.ttf",
    r"venv\assets\fonts\Schoolbell\Schoolbell-Regular.ttf",
    r"venv\assets\fonts\Architects_Daughter\ArchitectsDaughter-Regular.ttf",
    r"venv\assets\fonts\Coming_Soon\ComingSoon-Regular.ttf"
]

CURSIVE_FONTS = [
    r"venv\assets\fonts\Kalam\Kalam-Regular.ttf",
    r"venv\assets\fonts\Caveat\Caveat-VariableFont_wght.ttf"
]

# =====================================================
# STYLES
# =====================================================

HANDWRITING_STYLES = {

    "print": {
        "font_size_min": 70,
        "font_size_max": 90,
        "rotation_min": -3,
        "rotation_max": 3,
        "spacing_min": 2,
        "spacing_max": 5,
        "jitter": 2
    },

    "messy_print": {
        "font_size_min": 60,
        "font_size_max": 100,
        "rotation_min": -12,
        "rotation_max": 12,
        "spacing_min": -2,
        "spacing_max": 5,
        "jitter": 10
    },

    "shaky_print": {
        "font_size_min": 65,
        "font_size_max": 95,
        "rotation_min": -8,
        "rotation_max": 8,
        "spacing_min": 1,
        "spacing_max": 5,
        "jitter": 10
    },

    "cursive": {
        "font_size_min": 70,
        "font_size_max": 95,
        "rotation_min": -6,
        "rotation_max": 6,
        "spacing_min": -2,
        "spacing_max": 2,
        "jitter": 3
    },

    "signature": {
        "font_size_min": 90,
        "font_size_max": 130,
        "rotation_min": -12,
        "rotation_max": 12,
        "spacing_min": -10,
        "spacing_max": -2,
        "jitter": 14
    }
}


# =====================================================
# HANDWRITING GENERATOR
# =====================================================

def render_handwriting(text, style="print"):

    style_config = HANDWRITING_STYLES[style]

    # signatures and cursive use cursive fonts

    if style in ["cursive", "signature"]:
        font_path = random.choice(CURSIVE_FONTS)
    else:
        font_path = random.choice(PRINT_FONTS)

    img = Image.new(
        "RGBA",
        (1600, 350),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(img)

    font_size = random.randint(
        style_config["font_size_min"],
        style_config["font_size_max"]
    )

    font = ImageFont.truetype(
        font_path,
        font_size
    )

    start_x = 40
    baseline = 170

    for char in text:

        if char == " ":
            start_x += random.randint(20, 40)
            continue

        jitter = style_config["jitter"]

        x_jitter = random.randint(
            -jitter,
            jitter
        )

        y_jitter = random.randint(
            -jitter,
            jitter
        )

        # extra chaos for signatures

        if style == "signature":

            x_jitter += random.randint(-5, 5)

            y_jitter += random.randint(-12, 12)

            baseline += random.randint(-4, 4)

        else:

            baseline += random.randint(-1, 1)

        ink_color = (
            random.randint(0, 10),
            random.randint(0, 10),
            random.randint(130, 210),
            255
        )

        draw.text(
            (
                start_x + x_jitter,
                baseline + y_jitter
            ),
            char,
            fill=ink_color,
            font=font
        )

        bbox = font.getbbox(char)

        char_width = bbox[2] - bbox[0]

        start_x += (
            char_width +
            random.randint(
                style_config["spacing_min"],
                style_config["spacing_max"]
            )
        )

    img = random_rotation(
        img,
        style_config["rotation_min"],
        style_config["rotation_max"]
    )

    img = random_blur(img)

    img = add_scanner_noise(img)

    return img


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    style = random.choice([
        "print",
        "messy_print",
        "shaky_print",
        "cursive",
        "signature"
    ])

    img = render_handwriting(
        "Scott Gates",
        style
    )

    img.save(
        f"{style}_handwriting.png"
    )

    print(f"Generated: {style}")
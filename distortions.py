from PIL import ImageFilter, Image
import random
import numpy as np


# =====================================================
# ROTATION
# =====================================================

def random_rotation(img, min_angle, max_angle):

    angle = random.uniform(
        min_angle,
        max_angle
    )

    return img.rotate(
        angle,
        expand=True,
        fillcolor=(0, 0, 0, 0)
    )


# =====================================================
# BLUR
# =====================================================

def random_blur(img):

    blur_amount = random.uniform(
        0,
        1.0
    )

    return img.filter(
        ImageFilter.GaussianBlur(
            radius=blur_amount
        )
    )


# =====================================================
# SCANNER NOISE
# =====================================================

def add_scanner_noise(img):

    arr = np.array(img)

    # Keep alpha channel intact

    rgb = arr[:, :, :3]

    alpha = arr[:, :, 3]

    noise = np.random.normal(
        0,
        6,
        rgb.shape
    )

    rgb = rgb + noise

    rgb = np.clip(
        rgb,
        0,
        255
    ).astype(np.uint8)

    arr = np.dstack(
        (
            rgb,
            alpha
        )
    )

    return Image.fromarray(
        arr,
        mode="RGBA"
    )
from PIL import Image, ImageDraw, ImageFont

from patient_generator import generate_patient
from handwriting_engine import render_handwriting

# ==================================================
# CREATE FORM
# ==================================================

form = Image.new(
    "RGB",
    (1800, 3000),
    "white"
)

draw = ImageDraw.Draw(form)

# ==================================================
# FONT
# ==================================================

try:
    label_font = ImageFont.truetype(
        "arial.ttf",
        36
    )

    title_font = ImageFont.truetype(
        "arial.ttf",
        52
    )

except:
    label_font = ImageFont.load_default()
    title_font = ImageFont.load_default()

# ==================================================
# GENERATE PATIENT
# ==================================================

patient = generate_patient()

# ==================================================
# HEADER
# ==================================================

draw.rectangle(
    [(40, 40), (1760, 170)],
    outline="black",
    width=3
)

draw.text(
    (580, 75),
    "PATIENT INTAKE FORM",
    fill="black",
    font=title_font
)

# ==================================================
# SECTION 1
# ==================================================

draw.text(
    (60, 230),
    "PATIENT INFORMATION",
    fill="black",
    font=label_font
)

draw.line(
    [(60, 280), (1700, 280)],
    fill="black",
    width=2
)

fields = [

    ("PATIENT NAME", 340),
    ("DATE OF BIRTH", 520),
    ("SEX", 700),
    ("PHONE", 880),
    ("ADDRESS", 1060),
    ("INSURANCE ID", 1280)

]

for label, y in fields:

    draw.text(
        (80, y),
        label,
        fill="black",
        font=label_font
    )

    draw.line(
        [(80, y + 80), (1650, y + 80)],
        fill="black",
        width=2
    )

# ==================================================
# SECTION 2
# ==================================================

draw.text(
    (60, 1480),
    "MEDICAL INFORMATION",
    fill="black",
    font=label_font
)

draw.line(
    [(60, 1530), (1700, 1530)],
    fill="black",
    width=2
)

medical_fields = [

    ("SYMPTOMS", 1580),
    ("MEDICATIONS", 1760),
    ("ALLERGIES", 1940)

]

for label, y in medical_fields:

    draw.text(
        (80, y),
        label,
        fill="black",
        font=label_font
    )

    draw.line(
        [(80, y + 80), (1650, y + 80)],
        fill="black",
        width=2
    )

# ==================================================
# HANDWRITING IMAGES
# ==================================================

name_img = render_handwriting(
    patient["name"],
    style="print"
)

dob_img = render_handwriting(
    patient["dob"],
    style="print"
)

sex_img = render_handwriting(
    patient["sex"],
    style="print"
)

phone_img = render_handwriting(
    patient["phone"],
    style="print"
)

address_img = render_handwriting(
    patient["address"],
    style="print"
)

insurance_img = render_handwriting(
    patient["insurance_id"],
    style="print"
)

symptoms_img = render_handwriting(
    patient["symptoms"],
    style="messy_print"
)

medications_img = render_handwriting(
    patient["medications"],
    style="print"
)

allergies_img = render_handwriting(
    patient["allergies"],
    style="print"
)
history_img = render_handwriting(
    patient["medical_history"],
    style="messy_print"
)

# ==================================================
# RESIZE
# ==================================================

name_img = name_img.resize((1100, 180))
dob_img = dob_img.resize((800, 180))
sex_img = sex_img.resize((500, 180))
phone_img = phone_img.resize((900, 180))
address_img = address_img.resize((1300, 220))
insurance_img = insurance_img.resize((900, 180))

symptoms_img = symptoms_img.resize((1000, 180))
medications_img = medications_img.resize((1000, 180))
allergies_img = allergies_img.resize((1000, 180))
history_img = history_img.resize((1100, 250))

# ==================================================
# PASTE
# ==================================================

form.paste(
    name_img,
    (450, 270),
    name_img
)

form.paste(
    dob_img,
    (450, 450),
    dob_img
)

form.paste(
    sex_img,
    (450, 630),
    sex_img
)

form.paste(
    phone_img,
    (450, 810),
    phone_img
)

form.paste(
    address_img,
    (350, 980),
    address_img
)

form.paste(
    insurance_img,
    (500, 1210),
    insurance_img
)

form.paste(
    symptoms_img,
    (500, 1510),
    symptoms_img
)

form.paste(
    medications_img,
    (500, 1690),
    medications_img
)

form.paste(
    allergies_img,
    (500, 1870),
    allergies_img
)

# ==================================================
# MEDICAL HISTORY
# ==================================================

draw.text(
    (60, 2120),
    "MEDICAL HISTORY",
    fill="black",
    font=label_font
)

draw.line(
    [(60, 2170), (1700, 2170)],
    fill="black",
    width=2
)

form.paste(
    history_img,
    (350, 2200),
    history_img
)
# ==================================================
# SIGNATURE
# ==================================================

signature_img = render_handwriting(
    patient["name"],
    style="signature"
)

signature_img = signature_img.resize(
    (500, 120)
)

# Signature image
form.paste(
    signature_img,
    (1050, 2400),
    signature_img
)

# Signature line
draw.line(
    [(1000, 2580), (1700, 2580)],
    fill="black",
    width=2
)

# Label BELOW line
draw.text(
    (1180, 2600),
    "PATIENT SIGNATURE",
    fill="black",
    font=label_font
)

# ==================================================
# SAVE
# ==================================================

output_file = "filled_medical_form_v3.pdf"

form = form.convert("RGB")

form.save(
    output_file,
    "PDF",
    resolution=300.0
)
print("=" * 60)
print("MEDICAL FORM GENERATED")
print(output_file)
print("=" * 60)

import json

with open(
    "current_patient.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        patient,
        f,
        indent=4
    )
print(patient)
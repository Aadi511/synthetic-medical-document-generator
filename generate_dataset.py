import os
import sys
import csv
import json
import shutil
import subprocess

# ==================================================
# SETTINGS
# ==================================================

TOTAL = 10

OUTPUT_FOLDER = "dataset/images"
CSV_FILE = "dataset/labels.csv"

# ==================================================
# RESET DATASET
# ==================================================

if os.path.exists(OUTPUT_FOLDER):
    shutil.rmtree(OUTPUT_FOLDER)

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)

if os.path.exists(CSV_FILE):
    os.remove(CSV_FILE)

# ==================================================
# CREATE CSV
# ==================================================

with open(
    CSV_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "image",
        "name",
        "dob",
        "sex",
        "phone",
        "email",
        "address",
        "insurance_id",
        "visit_reason",
        "symptoms",
        "medications",
        "allergies",
        "doctor_name",
        "emergency_contact",
        "emergency_phone",
        "medical_history"
    ])

# ==================================================
# START
# ==================================================

print("=" * 60)
print("DATASET GENERATOR")
print("=" * 60)

print("\nPython Used:")
print(sys.executable)

# ==================================================
# GENERATE FORMS
# ==================================================

for i in range(TOTAL):

    print(f"\nGenerating {i+1}/{TOTAL}")

    result = subprocess.run(
        [
            sys.executable,
            "venv/src/form_rendered.py"
        ]
    )

    print(
        "Return Code:",
        result.returncode
    )

    if result.returncode != 0:

        print(
            "\nERROR: form_rendered.py failed"
        )

        break

    if not os.path.exists(
        "filled_medical_form_v3.pdf"
    ):

        print(
            "\nERROR: PDF not found"
        )

        break

    if not os.path.exists(
        "current_patient.json"
    ):

        print(
            "\nERROR: current_patient.json not found"
        )

        break

    image_name = (
        f"form_{i+1:05d}.pdf"
    )

    destination = os.path.join(
        OUTPUT_FOLDER,
        image_name
    )

    shutil.move(
        "filled_medical_form_v3.pdf",
        destination
    )

    with open(
        "current_patient.json",
        "r",
        encoding="utf-8"
    ) as f:

        patient = json.load(f)

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            image_name,
            patient["name"],
            patient["dob"],
            patient["sex"],
            patient["phone"],
            patient["email"],
            patient["address"],
            patient["insurance_id"],
            patient["visit_reason"],
            patient["symptoms"],
            patient["medications"],
            patient["allergies"],
            patient["doctor_name"],
            patient["emergency_contact"],
            patient["emergency_phone"],
            patient["medical_history"]
        ])

    print(
        f"Saved -> {image_name}"
    )

print("\n" + "=" * 60)
print("DATASET GENERATION COMPLETE")
print("=" * 60)
from faker import Faker
import random

fake = Faker()

# ==================================================

# PATIENT NAMES

# ==================================================

PATIENT_NAMES = [
"Sarah Lee",
"John Smith",
"Emily Brown",
"David Wilson",
"Michael Johnson",
"Olivia Davis",
"Daniel Miller",
"Sophia Anderson",
"James Taylor",
"Emma Thomas",
"William Moore",
"Ava Jackson",
"Benjamin White",
"Charlotte Harris",
"Lucas Martin",
"Mia Thompson",
"Noah Clark",
"Amelia Lewis",
"Henry Walker",
"Grace Hall"
]

# ==================================================

# SYMPTOMS

# ==================================================

SYMPTOMS = [
"Headache",
"Fever",
"Chest Pain",
"Dizziness",
"Back Pain",
"Shortness of Breath",
"Cough",
"Fatigue",
"Nausea",
"Abdominal Pain",
"Sore Throat",
"Runny Nose",
"Joint Pain",
"Muscle Weakness",
"Loss of Appetite",
"Vomiting",
"Diarrhea",
"Palpitations",
"Blurred Vision",
"Difficulty Sleeping",
"Anxiety",
"Depression",
"Skin Rash",
"Ear Pain",
"Frequent Urination",
"Swelling of Legs",
"Weight Loss",
"Weight Gain",
"Migraines",
"Neck Pain"
]

# ==================================================

# MEDICATIONS

# ==================================================

MEDICATIONS = [
"Paracetamol",
"Ibuprofen",
"Aspirin",
"Metformin",
"Atorvastatin",
"Omeprazole",
"Cetirizine",
"Amoxicillin",
"Azithromycin",
"Lisinopril",
"Losartan",
"Amlodipine",
"Levothyroxine",
"Prednisone",
"Albuterol",
"Insulin",
"Hydrochlorothiazide",
"Gabapentin",
"Sertraline",
"Fluoxetine"
]

# ==================================================

# ALLERGIES

# ==================================================

ALLERGIES = [
"None",
"Penicillin",
"Dust",
"Pollen",
"Peanuts",
"Seafood",
"Latex",
"Sulfa Drugs",
"Eggs",
"Milk",
"Soy",
"Shellfish",
"Bee Stings",
"Mold",
"Pet Dander"
]

# ==================================================

# MEDICAL HISTORY TEXT

# ==================================================

MEDICAL_HISTORY_TEXT = [
"No significant history",
"Asthma since childhood",
"Type 2 diabetes",
"Hypertension",
"High cholesterol",
"Previous stroke",
"Heart surgery in 2018",
"Chronic back pain",
"Migraine disorder",
"Kidney disease",
"Sleep apnea",
"Arthritis",
"Thyroid disorder",
"COPD",
"Anxiety disorder",
"Depression",
"History of cancer",
"Liver disease",
"Coronary artery disease",
"Chronic kidney disease"
]

# ==================================================

# VISIT REASONS

# ==================================================

VISIT_REASONS = [
"Routine Checkup",
"Follow-up Visit",
"Medication Refill",
"New Symptoms",
"Emergency Consultation",
"Specialist Referral",
"Annual Physical",
"Lab Review",
"Vaccination Visit",
"Post-Surgery Follow-up"
]

# ==================================================

# DOCTORS

# ==================================================

DOCTORS = [
"A Sharma",
"R Patel",
"K Singh",
"M Johnson",
"D Wilson",
"T Brown",
"S Taylor",
"J Anderson"
]
# ==================================================

# INSURANCE ID

# ==================================================

def generate_insurance_id():
    return f"INS-{random.randint(100000,999999)}"

# ==================================================

# MEDICAL HISTORY GENERATOR

# ==================================================

def generate_medical_history():


    count = random.randint(1, 3)

    return ", ".join(
    random.sample(
        MEDICAL_HISTORY_TEXT,
        count
    )
)


# ==================================================

# PATIENT GENERATOR

# ==================================================

def generate_patient():

    patient = {

    "name": random.choice(
        PATIENT_NAMES
    ),

    "dob": fake.date_of_birth(
        minimum_age=18,
        maximum_age=90
    ).strftime("%d/%m/%Y"),

    "form_date": fake.date_between(
        start_date="-2y",
        end_date="today"
    ).strftime("%d/%m/%Y"),

    "sex": random.choice([
        "Male",
        "Female"
    ]),

    "phone": fake.phone_number(),

    "email": fake.email(),

    "address": fake.address().replace(
        "\n",
        ", "
    ),

    "insurance_id": generate_insurance_id(),

    "visit_reason": random.choice(
        VISIT_REASONS
    ),

    "symptoms": random.choice(
        SYMPTOMS
    ),

    "medications": random.choice(
        MEDICATIONS
    ),

    "allergies": random.choice(
        ALLERGIES
    ),

    "doctor_name": random.choice(
        DOCTORS
    ),

    "emergency_contact": fake.name(),

    "emergency_phone": fake.phone_number(),

    "medical_history": generate_medical_history()
}

# ======================================
# MISSING FIELD SIMULATION
# ======================================

    if random.random() < 0.10:
        patient["allergies"] = ""

    if random.random() < 0.10:
        patient["medications"] = ""

    if random.random() < 0.05:
        patient["phone"] = ""

    if random.random() < 0.03:
        patient["address"] = ""

    if random.random() < 0.03:
        patient["email"] = ""

    if random.random() < 0.03:
        patient["insurance_id"] = ""

    return patient



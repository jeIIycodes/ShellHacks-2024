import re

def collect_scholarship_info():
    scholarship_info = {}

    # attempt @ validate function: numeric input within range using regex
    def get_valid_input(prompt, valid_options=None, regex=None):
        while True:
            user_input = input(prompt).strip().lower()
            
            if valid_options and user_input in valid_options:
                return user_input
            
            if regex and re.match(regex, user_input):
                return user_input
            
            print("Invalid input. Please try again.")

    # Education Information
    scholarship_info['Education'] = {}
    scholarship_info['Education']['Current FIU Student Status'] = input("Current FIU student status (freshman, sophomore, etc.): ").capitalize()
    scholarship_info['Education']['Field of Study/Major/Program'] = input("Field of Study/Major/Program: ").title()

    # Graduation Date Input (MM/YYYY) // attempt @ date validation
    while True:
        grad_date = input("Expected graduation date (MM/YYYY): ")
        if re.match(r"^(0[1-9]|1[0-2])\/\d{4}$", grad_date):
            scholarship_info['Education']['Expected Graduation Date (MM/YYYY)'] = grad_date
            break
        else:
            print("Invalid date format. Please enter in MM/YYYY format.")

    # GPA Input Validation (X.X / 4.0) // attempt @ date validation
    while True:
        gpa = input("GPA (if applicable) (X.X/4.0): ")
        if gpa == '' or (gpa.replace('.', '', 1).isdigit() and 0.0 <= float(gpa) <= 4.0):
            scholarship_info['Education']['GPA (if applicable)'] = gpa
            break
        else:
            print("Please enter a valid GPA (X.X format, max 4.0) or leave blank if not applicable.")

    # Personal Information
    scholarship_info['Personal Information'] = {}
    scholarship_info['Personal Information']['Name'] = input("Name (as it appears on legal documents): ").title()
    scholarship_info['Personal Information']['Preferred Name'] = input("Preferred name (if different): ").title()
    
    # Date of Birth Input Validation (MM/DD/YYYY)
    while True:
        dob = input("Date of Birth (MM/DD/YYYY): ")
        if re.match(r"^(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])\/\d{4}$", dob):
            scholarship_info['Personal Information']['Date of Birth (MM/DD/YYYY)'] = dob
            break
        else:
            print("Invalid date format. Please enter in MM/DD/YYYY format.")
    
    scholarship_info['Personal Information']['Contact Information'] = input("Contact information (email, phone number): ")

    # Gender Identity with Validation
    gender_map = {
        '1': 'Woman',
        '2': 'Man',
        '3': 'Non-binary',
        '4': 'Transgender',
        '5': 'Gender non-conforming',
        '6': 'Self-describe',
        '7': 'Prefer not to say'
    }

    while True:
        print("\nGender Identity Options:")
        for k, v in gender_map.items():
            print(f"{k}. {v}")
        gender_choice = get_valid_input("Select your gender identity (1-7): ", valid_options=gender_map.keys())
        
        if gender_choice == '6':
            scholarship_info['Personal Information']['Gender Identity'] = input("Please self-describe your gender: ")
        else:
            scholarship_info['Personal Information']['Gender Identity'] = gender_map[gender_choice]

    # Sex Assigned at Birth with Validation
    sex_map = {
        '1': 'Female',
        '2': 'Male',
        '3': 'Intersex',
        '4': 'Prefer not to say'
    }

    while True:
        print("\nSex Assigned at Birth Options:")
        for k, v in sex_map.items():
            print(f"{k}. {v}")
        sex_choice = get_valid_input("Select your sex assigned at birth (1-4): ", valid_options=sex_map.keys())
        scholarship_info['Personal Information']['Sex Assigned at Birth'] = sex_map[sex_choice]

    # Additional Demographics with Validation (Yes/No)
    scholarship_info['Demographics'] = {}
    scholarship_info['Demographics']['Florida Resident'] = get_valid_input("Are you a Florida resident? (yes/no): ", valid_options=['yes', 'no'])
    scholarship_info['Demographics']['First-Generation College Student'] = get_valid_input("Are you a first-generation college student? (yes/no): ", valid_options=['yes', 'no'])

    # Race/Ethnicity with Validation
    ethnicity_map = {
        '1': 'Asian',
        '2': 'Black or African American',
        '3': 'Hispanic or Latino',
        '4': 'Native American or Alaska Native',
        '5': 'Native Hawaiian or Other Pacific Islander',
        '6': 'White',
        '7': 'Self-describe',
        '8': 'Prefer not to say'
    }

    while True:
        print("\nRace/Ethnicity Options:")
        for k, v in ethnicity_map.items():
            print(f"{k}. {v}")
        ethnicity_choice = get_valid_input("Select your race/ethnicity (1-8): ", valid_options=ethnicity_map.keys())
        
        if ethnicity_choice == '7':
            scholarship_info['Demographics']['Race/Ethnicity'] = input("Please self-describe your race/ethnicity: ")
        else:
            scholarship_info['Demographics']['Race/Ethnicity'] = ethnicity_map[ethnicity_choice]

    return scholarship_info


if __name__ == "__main__":
    scholarship_data = collect_scholarship_info()
    print("\nScholarship Application Data Collected:")
    for section, data in scholarship_data.items():
        print(f"\n{section}:")
        for key, value in data.items():
            print(f"  {key}: {value}")

# app.py

from flask import (
    render_template,
    redirect,
    url_for,
    flash,
)
from flask import Blueprint
from datetime import datetime
from frontend.flask.Forms import ScholarshipApplicationForm  # Ensure correct import path

assesment_bp = Blueprint("lp", __name__, url_prefix="/assessment")  # Corrected spelling to "assessment"



@assesment_bp.route('/', methods=['GET', 'POST'])
def scholarship_application():
    form = ScholarshipApplicationForm()

    # Dynamically populate expected_graduation choices
    if not form.expected_graduation.choices:
        seasons = ['Fall', 'Spring', 'Summer']
        current_year = 2024
        end_year = 2034
        graduation_choices = []
        for year in range(current_year, end_year + 1):
            for season in seasons:
                label = f"{season} {year}"
                value = f"{season} {year}"
                graduation_choices.append((value.lower().replace(' ', '-'), label))
        form.expected_graduation.choices = graduation_choices

    if form.validate_on_submit():
        # Process the form data
        scholarship_data = {
            'Education': {
                'Years in College': form.years_in_college.data.title(),
                'Field of Study/Major/Program': dict(form.field_of_study.choices).get(form.field_of_study.data),
                'Expected Graduation Date (Season Year)': form.expected_graduation.data.replace('-', ' ').title(),
                'GPA (if applicable)': f"{form.gpa.data:.2f}" if form.gpa.data is not None else 'N/A'
            },
            'Personal Information': {
                'Name': form.legal_name.data.title(),
                'Preferred Name': form.preferred_name.data.title() if form.preferred_name.data else 'N/A',
                'Date of Birth (MM/DD/YYYY)': form.date_of_birth.data,
                'Contact Information': {
                    'Email': form.contact_email.data,
                    'Phone Number': form.contact_phone.data
                }
            },
            'Demographics': {
                'Gender Identity': form.gender_self_describe.data.title() if form.gender_identity.data == 'self-describe' else form.gender_identity.data.title(),
                'Florida Resident': form.florida_resident.data.title(),
                'First-Generation College Student': form.first_gen_college_student.data.title(),
                'Race/Ethnicity': form.race_self_describe.data.title() if form.race_ethnicity.data == 'self-describe' else form.race_ethnicity.data.title()
            },
            'Financial Information': {
                'Mean Yearly Income': f"${form.mean_yearly_income.data:,.2f}",
                'Expected Yearly Scholarships': f"${form.expected_yearly_scholarships.data:,.2f}",
                'Housing': form.housing.data.replace('-', ' ').title()
            }
        }
        # For demonstration, just print the data
        print("\nScholarship Application Data Collected:")
        for section, data in scholarship_data.items():
            print(f"\n{section}:")
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, dict):
                        print(f"  {key}:")
                        for subkey, subvalue in value.items():
                            print(f"    {subkey}: {subvalue}")
                    else:
                        print(f"  {key}: {value}")
            else:
                print(f"  {data}")

        flash('Application submitted successfully!', 'success')
        return redirect(url_for('lp.scholarship_application'))
    return render_template('scholarship_application.html', form=form)


# forms.py

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    RadioField,
    DecimalField,
    IntegerField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Optional,
    NumberRange,
    Email,
    ValidationError,
)
import re

class ScholarshipApplicationForm(FlaskForm):
    # List of majors
    majors = [
        ('accounting', 'Accounting'),
        ('anthropology', 'Anthropology'),
        ('art', 'Art'),
        ('biology', 'Biology'),
        ('business', 'Business Administration'),
        ('chemistry', 'Chemistry'),
        ('computer-engineering', 'Computer Engineering'),
        ('computer-science', 'Computer Science'),
        ('economics', 'Economics'),
        ('education', 'Education'),
        ('electrical-engineering', 'Electrical Engineering'),
        ('engineering', 'Engineering'),
        ('english', 'English'),
        ('environmental-science', 'Environmental Science'),
        ('finance', 'Finance'),
        ('history', 'History'),
        ('international-relations', 'International Relations'),
        ('journalism', 'Journalism'),
        ('marketing', 'Marketing'),
        ('mathematics', 'Mathematics'),
        ('mechanical-engineering', 'Mechanical Engineering'),
        ('music', 'Music'),
        ('nursing', 'Nursing'),
        ('philosophy', 'Philosophy'),
        ('physics', 'Physics'),
        ('political-science', 'Political Science'),
        ('psychology', 'Psychology'),
        ('sociology', 'Sociology'),
        ('software-engineering', 'Software Engineering'),
        ('statistics', 'Statistics'),
    ]
    # 'other' input option ^ if major is not listed ***

    # Education Information
    year_in_college = SelectField(
        'Year in College',
        choices=[
            ('1', '1st Year'),
            ('2', '2nd Year'),
            ('3', '3rd Year'),
            ('4', '4th Year'),
            ('5', '5th Year'),
            ('6', '6th Year'),
        ],
        validators=[DataRequired()]
    )

    # Field of Study/Major/Program - Now a searchable dropdown
    field_of_study = SelectField(
        'Field of Study/Major/Program',
        choices=majors,
        validators=[DataRequired()]
    )

    # Expected Graduation Date (Season Year) - dropdown
    expected_graduation = SelectField(
        'Expected Graduation Date (Season Year)',
        choices=[],  # To be populated dynamically
        validators=[DataRequired()]
    )

gpa = DecimalField(
        'GPA (if applicable)',
        validators=[Optional(), NumberRange(min=0.0, max=4.0)],
        places=2
    )

gender_identity = SelectField(
        'Gender Identity',
        choices=[
            ('woman', 'Woman'),
            ('man', 'Man'),
            ('non-binary', 'Non-binary'),
            ('transgender', 'Transgender'),
            ('gender-non-conforming', 'Gender non-conforming'),
            ('self-describe', 'Self-describe'),
            ('prefer-not-to-say', 'Prefer not to say')
        ],
        validators=[DataRequired()]
    )
gender_self_describe = StringField(
        'Please self-describe your gender',
        validators=[Optional()]
    )

    # Additional Demographics
florida_resident = RadioField(
        'Are you a Florida resident?',
        choices=[('yes', 'Yes'), ('no', 'No')],
        validators=[DataRequired()]
    )
first_gen_college_student = RadioField(
        'Are you a first-generation college student?',
        choices=[('yes', 'Yes'), ('no', 'No')],
        validators=[DataRequired()]
    )

citizenship_status = SelectField(
        'Citizenship/Residency Status',
        choices=[
            ('us_citizen', 'U.S. Citizen'),
            ('permanent_resident', 'U.S. Permanent Resident'),
            ('international_f1', 'International Student (F-1 Visa)'),
            ('international_j1', 'International Student (J-1 Visa)')
        ],
        validators=[DataRequired()]
    )

race_ethnicity = SelectField(
        'Race/Ethnicity',
        choices=[
            ('asian', 'Asian'),
            ('black', 'Black or African American'),
            ('hispanic', 'Hispanic or Latino'),
            ('native-american', 'Native American or Alaska Native'),
            ('pacific-islander', 'Native Hawaiian or Other Pacific Islander'),
            ('white', 'White'),
            ('self-describe', 'Self-describe'),
            ('prefer-not-to-say', 'Prefer not to say')
        ],
        validators=[DataRequired()]
    )
race_self_describe = StringField(
        'Please self-describe your race/ethnicity',
        validators=[Optional()]
    )

    # 3. Financial Qs

employed_or_nah = RadioField(
        'Are you currently employed?',
        choices=[('yes', 'Yes'), ('no', 'No')],
        validators=[DataRequired()]
    )

housing = SelectField(
        'Current Housing Circumstance',
        choices=[
            ('on-campus', 'On-campus'),
            ('off-campus', 'Off-campus'),
            ('at-home', 'At home')
        ],
        validators=[DataRequired()]
    )

is_financially_independent = RadioField(
        'Are you financially independent?',
        choices=[('yes', 'Yes'), ('no', 'No')],
        validators=[DataRequired()]
    )

    # Household Income
household_income = SelectField(
        'What is your annual household income?',
        choices=[
            ('', 'Select household income range'),
            ('less_than_25k', 'Less than $25,000'),
            ('25k_to_49k', '$25,000 - $49,999'),
            ('50k_to_74k', '$50,000 - $74,999'),
            ('75k_to_99k', '$75,000 - $99,999'),
            ('100k_or_more', '$100,000 or more')
        ],
        validators=[DataRequired()]
    )

    # Dependents
dependents = IntegerField(
        'Number of dependents in household (including yourself)',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=20, message="Please enter a number between 1 and 20")
        ],
        render_kw={"placeholder": "Enter number between 1 and 20"}
    )

 # Educational Expenses - Based on FIU Tuition Calculator *can link in question*
est_expenses = DecimalField(
        'Estimated annual educational expenses at FIU',
        validators=[
            DataRequired(),
            NumberRange(min=0, max=100000, message="Please enter an amount between $0 and $100,000")
        ],
        render_kw={"placeholder": "Enter amount in USD (max $100,000)"}
    )

 # FAFSA Eligibility *can link below in question*
fafsa = RadioField(
        'Are you eligible to file a FAFSA (Free Application for Federal Student Aid)?',
        choices=[
            ('yes', 'Yes'),
            ('no', 'No'),
            ('unsure', 'I\'m not sure')
        ],
        validators=[DataRequired()]
    )

submit = SubmitField('Submit')

    # Custom Validators
def validate_gpa(self, field):
        if field.data is not None:
            if field.data < 0.0 or field.data > 4.0:
                raise ValidationError("GPA must be between 0.0 and 4.0")
            if len(str(field.data).split('.')[-1]) > 2:
                raise ValidationError("GPA should have at most 2 decimal places")
            
def validate_estimated_educational_expenses(self, field):
        if field.data > 100000:
            raise ValidationError("Please contact the financial aid office for expenses exceeding $100,000")

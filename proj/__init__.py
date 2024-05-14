

UPLOAD_FOLDER = '../static/uploads/users_profile/'

SITUATION = ['Single', 'Engaged', 'Married', 'Divorced', 'Complicated', 'In a relationship', 'Other/Not Listed']

LEVEL = ['High School Diploma/GED',
         "Associate's Degree",
         "Bachelor's Degree",
         "Master's Degree",
         "Doctorate/Ph.D.",
         "Professional Degree (MD, JD, etc.)",
         "Other/Not Listed"]

DISEASES = [
    "COVID-19",
    "Influenza (Flu)",
    "Diabetes",
    "Hypertension (High Blood Pressure)",
    "Asthma",
    "Arthritis",
    "Depression",
    "Cancer",
    "Alzheimer's Disease",
    "Heart Disease",
    "Stroke",
    "Kidney Disease",
    "Liver Disease",
    "Osteoporosis",
    "Allergies",
    "HIV/AIDS",
    "Obesity",
    "Mental Health Disorders",
    "Other/Not Listed"
]

JOBS = [
    "I don't work !",
    "Software Developer/Engineer",
    "Registered Nurse",
    "Medical Doctor/Physician",
    "Accountant/Financial Analyst",
    "Teacher/Educator",
    "Marketing Manager/Digital Marketer",
    "Sales Representative",
    "Human Resources Specialist",
    "Project Manager",
    "Customer Service Representative",
    "Data Analyst/Scientist",
    "Mechanical Engineer",
    "Electrical Engineer",
    "Civil Engineer",
    "Lawyer/Attorney",
    "Pharmacist",
    "Operations Manager",
    "IT Support Specialist",
    "Graphic Designer",
    "Social Media Manager",
    "Other/Not Listed"
]

ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
DEFAULT_IMG = 'default.jpg'
INFO = ['name', 'age', 'gender', 'country','level', 'job','weight','height','situation','disease','img']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
COUNTRIES = ['Moldova', 'United States', 'Mayotte', 'Nauru', 'Mozambique', 'Brazil', 'Cape Verde', 'Equatorial Guinea', 'Albania', 'United States Virgin Islands', 'Niue', 'Palau', 'Nigeria', 'British Virgin Islands', 'Gambia', 'Somalia', 'Yemen', 'Malaysia', 'Dominica', 'United Kingdom', 'Madagascar', 'Western Sahara', 'Cyprus', 'Antigua and Barbuda', 'Ireland', 'Paraguay', 'Sri Lanka', 'South Africa', 'Kuwait', 'Algeria', 'Croatia', 'Martinique', 'Sierra Leone', 'Northern Mariana Islands', 'Rwanda', 'Syria', 'Saint Vincent and the Grenadines', 'Kosovo', 'Saint Lucia', 'Honduras', 'Jordan', 'Tuvalu', 'Nepal', 'Liberia', 'Heard Island and McDonald Islands', 'Austria', 'Guernsey', 'Central African Republic', 'Mauritania', 'Djibouti', 'Fiji', 'Norway', 'Latvia', 'Falkland Islands', 'Kazakhstan', 'Åland Islands', 'Turkmenistan', 'Cocos (Keeling) Islands', 'Bulgaria', 'Tokelau', 'New Caledonia', 'Barbados', 'São Tomé and Príncipe', 'Antarctica', 'Brunei', 'Bhutan', 'Cameroon', 'Argentina', 'Azerbaijan', 'Mexico', 'Morocco', 'Guatemala', 'Kenya', 'Malta', 'Czechia', 'Gibraltar', 'Aruba', 'Saint Barthélemy', 'Monaco', 'United Arab Emirates', 'South Sudan', 'Puerto Rico', 'El Salvador', 'France', 'Niger', 'Ivory Coast', 'South Georgia', 'Botswana', 'British Indian Ocean Territory', 'Uzbekistan', 'Tunisia', 'Hong Kong', 'North Macedonia', 'Suriname', 'Belgium', 'American Samoa', 'Solomon Islands', 'Ukraine', 'Finland', 'Burkina Faso', 'Bosnia and Herzegovina', 'Iran', 'Cuba', 'Eritrea', 'Slovakia', 'Lithuania', 'Saint Martin', 'Pitcairn Islands', 'Guinea-Bissau', 'Montserrat', 'Turkey', 'Philippines', 'Vanuatu', 'Bolivia', 'Saint Kitts and Nevis', 'Romania', 'Cambodia', 'Zimbabwe', 'Jersey', 'Kyrgyzstan', 'Caribbean Netherlands', 'Guyana', 'United States Minor Outlying Islands', 'Armenia', 'Lebanon', 'Montenegro', 'Greenland', 'Papua New Guinea', 'Zambia', 'Trinidad and Tobago', 'French Southern and Antarctic Lands', 'Peru', 'Sweden', 'Sudan', 'Saint Pierre and Miquelon', 'Oman', 'India', 'Taiwan', 'Mongolia', 'Senegal', 'Tanzania', 'Canada', 'Costa Rica', 'China', 'Colombia', 'Myanmar', 'Russia', 'North Korea', 'Cayman Islands', 'Bouvet Island', 'Belarus', 'Portugal', 'Eswatini', 'Poland', 'Switzerland', 'Republic of the Congo', 'Venezuela', 'Panama', 'Netherlands', 'Samoa', 'Denmark', 'Luxembourg', 'Faroe Islands', 'Slovenia', 'Togo', 'Thailand', 'Wallis and Futuna', 'Bahamas', 'Tonga', 'Greece', 'San Marino', 'Réunion', 'Vatican City', 'Burundi', 'Bahrain', 'Marshall Islands', 'Turks and Caicos Islands', 'Isle of Man', 'Haiti', 'Afghanistan', 'Israel', 'Libya', 'Uruguay',
             'Norfolk Island', 'Nicaragua', 'Cook Islands', 'Laos', 'Christmas Island', 'Saint Helena, Ascension and Tristan da Cunha', 'Anguilla', 'Micronesia', 'Germany', 'Guam', 'Kiribati', 'Sint Maarten', 'Spain', 'Jamaica', 'Palestine', 'French Guiana', 'Andorra', 'Chile', 'Lesotho', 'Australia', 'Grenada', 'Ghana', 'Seychelles', 'Angola', 'Bermuda', 'Pakistan', 'Mali', 'Saudi Arabia', 'Curaçao', 'South Korea', 'Ethiopia', 'Guadeloupe', 'Bangladesh', 'New Zealand', 'Comoros', 'Belize', 'Uganda', 'Singapore', 'Liechtenstein', 'Hungary', 'Iceland', 'Tajikistan', 'Namibia', 'Timor-Leste', 'Egypt', 'Serbia', 'Mauritius', 'Macau', 'French Polynesia', 'Maldives', 'Indonesia', 'DR Congo', 'Estonia', 'Vietnam', 'Italy', 'Guinea', 'Chad', 'Ecuador', 'Georgia', 'Malawi', 'Iraq', 'Svalbard and Jan Mayen', 'Benin', 'Japan', 'Dominican Republic', 'Qatar', 'Gabon']

ALL_INFO = {'gender' : ['Male', 'Female'],
            'job': JOBS,
            'situation': SITUATION,
            'disease': DISEASES,
            'level': LEVEL,
            'country': COUNTRIES}
"""
Created on Fri Nov 22 09:25:35 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches

import math
import boto3
import io
import json
# import reusable_functions as 
from django.conf import settings
# from .reusable_functions import *


#Change these global variables to your corresponding filename and institution name
# filename = '1figr_U_Virginia_Original (1) (1).xlsx'
# your_institution = 'UVA'

def getData():
	# data_AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
	# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
	# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
	# AWS_DATA_LOCATION = config('AWS_DATA_LOCATION')

	client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
			aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
	

	object_key = 'JournalsPerProvider_withoutQuotes.xls'
	obj = client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=object_key)
	data = obj['Body'].read()
	df = pd.read_excel(io.BytesIO(data), encoding='utf-8', skiprows=8)
	# print(df)
	return df

journalsByDisciplineData = getData()
# print(journalsByDisciplineData)

def make_disciplines_column():
	"""This generates the disciplines column on the fly for each journal. The disciplines column in a combination of various permutations of each journal's
	domain, field, subfield columns. The discipline column is meant to be something more analagous to departments at the university. The disciplines column does
	not currently exist in the original 1figr dataset and therefore must be generated upon running this function."""

	# original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
	original_1figr_dataset = journalsByDisciplineData

	#logic for every permutation of domain, field, subfield column with the end result defined in the "disciplines" column    

	#Applied Sciences Domain
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Agronomy & Agriculture'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Dairy & Animal Science'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Fisheries'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Food Science'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Forestry'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Horticulture'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Veterinary Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Built Environment & Design') & (original_1figr_dataset['Subfield'] == 'Architecture'), 'Discipline'] = 'Architecture'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Built Environment & Design') & (original_1figr_dataset['Subfield'] == 'Building & Construction'), 'Discipline'] = 'Architecture'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Built Environment & Design') & (original_1figr_dataset['Subfield'] == 'Design Practice & Management'), 'Discipline'] = 'Architecture'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Built Environment & Design') & (original_1figr_dataset['Subfield'] == 'Urban & Regional Planning'), 'Discipline'] = 'Architecture'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Bioinformatics'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Biotechnology'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Energy'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Materials'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Nanoscience & Nanotechnology'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Optoelectronics & Photonics'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Strategic, Defence & Security Studies'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Aerospace & Aeronautics'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Automobile Design & Engineering'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Biomedical Engineering'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Chemical Engineering'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Civil Engineering'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Electrical & Electronic Engineering'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Environmental Engineering'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Geological & Geomatics Engineering'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Industrial Engineering & Automation'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Mechanical Engineering & Transports'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Mining & Metallurgy'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Operations Research'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Artificial Intelligence & Image Processing'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Computation Theory & Mathematics'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Computer Hardware & Architecture'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Distributed Computing'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Information Systems'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Medical Informatics'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Networking & Telecommunications'), 'Discipline'] = 'Engineering'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Software Engineering'), 'Discipline'] = 'Engineering'

	#Arts & Humanities Domain
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Communication & Textual Studies') & (original_1figr_dataset['Subfield'] == 'Communication & Media Studies'), 'Discipline'] = 'Communication & Textual Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Communication & Textual Studies') & (original_1figr_dataset['Subfield'] == 'Languages & Linguistics'), 'Discipline'] = 'Communication & Textual Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Communication & Textual Studies') & (original_1figr_dataset['Subfield'] == 'Literary Studies'), 'Discipline'] = 'Communication & Textual Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'Anthropology'), 'Discipline'] = 'Historical Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'Archaeology'), 'Discipline'] = 'Historical Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'Classics'), 'Discipline'] = 'Historical Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'History'), 'Discipline'] = 'Historical Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'History of Science, Technology & Medicine'), 'Discipline'] = 'Historical Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'History of Social Sciences'), 'Discipline'] = 'Historical Studies'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Philosophy & Theology') & (original_1figr_dataset['Subfield'] == 'Applied Ethics'), 'Discipline'] = 'Philosophy & Theology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Philosophy & Theology') & (original_1figr_dataset['Subfield'] == 'Philosophy'), 'Discipline'] = 'Philosophy & Theology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Philosophy & Theology') & (original_1figr_dataset['Subfield'] == 'Religions & Theology'), 'Discipline'] = 'Philosophy & Theology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Visual & Performing Arts') & (original_1figr_dataset['Subfield'] == 'Art Practice, History & Theory'), 'Discipline'] = 'Visual & Performing Arts'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Visual & Performing Arts') & (original_1figr_dataset['Subfield'] == 'Drama & Theater'), 'Discipline'] = 'Visual & Performing Arts'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Visual & Performing Arts') & (original_1figr_dataset['Subfield'] == 'Folklore'), 'Discipline'] = 'Visual & Performing Arts'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Visual & Performing Arts') & (original_1figr_dataset['Subfield'] == 'Music'), 'Discipline'] = 'Visual & Performing Arts'
	
	#Economic & Social Sciences Domain
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Accounting'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Agricultural Economics & Policy'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Business & Management'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Development Studies'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Econometrics'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Economic Theory'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Economics'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Finance'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Industrial Relations'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Logistics & Transportation'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Marketing'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Sport, Leisure & Tourism'), 'Discipline'] = 'Economics & Business'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Criminology'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Cultural Studies'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Demography'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Education'), 'Discipline'] = 'Education'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Family Studies'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Gender Studies'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Geography'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Information & Library Sciences'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'International Relations'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Law'), 'Discipline'] = 'Law'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Political Science & Public Administration'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Science Studies'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Social Sciences Methods'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Social Work'), 'Discipline'] = 'Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Sociology'), 'Discipline'] = 'Social Sciences'

	#General Domain
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'General') & (original_1figr_dataset['Field'] == 'General Arts, Humanities & Social Sciences') & (original_1figr_dataset['Subfield'] == 'General Arts, Humanities & Social Sciences'), 'Discipline'] = 'General Arts, Humanities & Social Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'General') & (original_1figr_dataset['Field'] == 'General Science & Technology') & (original_1figr_dataset['Subfield'] == 'General Science & Technology'), 'Discipline'] = 'General Science & Technology'

	#Health Sciences Domain
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Anatomy & Morphology'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Biochemistry & Molecular Biology'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Biophysics'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Developmental Biology'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Genetics & Heredity'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Microbiology'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Microscopy'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Mycology & Parasitology'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Nutrition & Dietetics'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Physiology'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Toxicology'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Virology'), 'Discipline'] = 'Biomedical Research'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Allergy'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Anesthesiology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Arthritis & Rheumatology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Cardiovascular System & Hematology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Complementary & Alternative Medicine'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Dentistry'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Dermatology & Venereal Diseases'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Emergency & Critical Care Medicine'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Endocrinology & Metabolism'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Environmental & Occupational Health'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Gastroenterology & Hepatology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'General & Internal Medicine'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'General Clinical Medicine'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Geriatrics'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Immunology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Legal & Forensic Medicine'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Neurology & Neurosurgery'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Nuclear Medicine & Medical Imaging'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Obstetrics & Reproductive Medicine'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Oncology & Carcinogenesis'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Ophthalmology & Optometry'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Orthopedics'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Otorhinolaryngology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Pathology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Pediatrics'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Pharmacology & Pharmacy'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Psychiatry'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Respiratory System'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Sport Sciences'), 'Discipline'] = 'Education'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Surgery'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Tropical Medicine'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Urology & Nephrology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Behavioral Science & Comparative Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Clinical Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Developmental & Child Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Experimental Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'General Psychology & Cognitive Sciences'), 'Discipline'] = 'Psychology & Cognitive Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Human Factors'), 'Discipline'] = 'Psychology & Cognitive Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Psychoanalysis'), 'Discipline'] = 'Psychology & Cognitive Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Social Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Epidemiology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Gerontology'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Health Policy & Services'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Nursing'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Public Health'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Rehabilitation'), 'Discipline'] = 'Health Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Speech-Language Pathology & Audiology'), 'Discipline'] = 'Education'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Substance Abuse'), 'Discipline'] = 'Health Sciences'

	#Natural Sciences Domain
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Ecology'), 'Discipline'] = 'Biology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Entomology'), 'Discipline'] = 'Biology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Evolutionary Biology'), 'Discipline'] = 'Biology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Marine Biology & Hydrobiology'), 'Discipline'] = 'Biology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Ornithology'), 'Discipline'] = 'Biology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Plant Biology & Botany'), 'Discipline'] = 'Biology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Zoology'), 'Discipline'] = 'Biology'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Analytical Chemistry'), 'Discipline'] = 'Chemistry'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'General Chemistry'), 'Discipline'] = 'Chemistry'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Inorganic & Nuclear Chemistry'), 'Discipline'] = 'Chemistry'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Medicinal & Biomolecular Chemistry'), 'Discipline'] = 'Chemistry'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Organic Chemistry'), 'Discipline'] = 'Chemistry'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Physical Chemistry'), 'Discipline'] = 'Chemistry'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Polymers'), 'Discipline'] = 'Chemistry'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Environmental Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Geochemistry & Geophysics'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Geology'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Meteorology & Atmospheric Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Oceanography'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Paleontology'), 'Discipline'] = 'Earth & Environmental Sciences'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Mathematics & Statistics') & (original_1figr_dataset['Subfield'] == 'Applied Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Mathematics & Statistics') & (original_1figr_dataset['Subfield'] == 'General Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Mathematics & Statistics') & (original_1figr_dataset['Subfield'] == 'Numerical & Computational Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Mathematics & Statistics') & (original_1figr_dataset['Subfield'] == 'Statistics & Probability'), 'Discipline'] = 'Mathematics & Statistics'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Acoustics'), 'Discipline'] = 'Physics & Astronomy'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Applied Physics'), 'Discipline'] = 'Physics & Astronomy'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Astronomy & Astrophysics'), 'Discipline'] = 'Physics & Astronomy'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Chemical Physics'), 'Discipline'] = 'Physics & Astronomy'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Fluids & Plasmas'), 'Discipline'] = 'Physics & Astronomy'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'General Physics'), 'Discipline'] = 'Physics & Astronomy'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Mathematical Physics'), 'Discipline'] = 'Physics & Astronomy'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Nuclear & Particle Physics'), 'Discipline'] = 'Physics & Astronomy'
	original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Optics'), 'Discipline'] = 'Physics & Astronomy'

	# print(original_1figr_dataset['Discipline'])

	# prints count of number of journals in each discipline
	# print(original_1figr_dataset['Discipline'].value_counts())  #23873 total
	
	return original_1figr_dataset

def get_disciplines_list():
	original_1figr_data_with_disciplines = make_disciplines_column()
	disciplines_data = original_1figr_data_with_disciplines.groupby(['Discipline'], as_index=False)
	disciplines_list = []
	for key, item in disciplines_data:
		disciplines_list.append(key)

	return disciplines_list

def journals_by_discipline():
	"""Shows distribution of current year article downloads (JR5) by discipline for the specified provider.
	'Disciplines' is a column we derived from the pre-existing 'fields' column in the 1figr data.
	Disciplines has mapped those field categories into more UVA specific language
	
	Chart Type: Line
	Y-Axis: Discipline 
	Y-Axis Data Source: Original 1Figr Dataset, reusable_functions.py
	
	X-Axis: Number of JR1 Downloads
	X-Axis Data Source: Original 1Figr Dataset, reusable_functions.py
	"""
	
	necessary_columns = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers', 'Journal', 'Provider', 'Discipline']
	original_1figr_data_with_disciplines = make_disciplines_column()[necessary_columns]
	# print(original_1figr_data_with_disciplines.columns)

	journals_by_discipline_df = original_1figr_data_with_disciplines.groupby(['Discipline'], as_index=False)
	# print(journalsByDisciplineData.sort_values(by='References', ascending=False)[['References', 'Journal']].values.tolist())
	metrics = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers']

	ret = {}

	for metric in metrics:
		journals_by_discipline_by_metric_dict = {}

		for key, item in journals_by_discipline_df:
			# sort_values(by=[metric], ascending=False, kind='mergesort').fillna(0)
			group = journals_by_discipline_df.get_group(key)[['Journal','Provider', metric]].groupby(['Journal', metric])['Provider'].apply(', '.join).reset_index()
			group = group[['Journal','Provider', metric]].sort_values(by=[metric], ascending=False, kind='mergesort').fillna(0)
			# print(group)
			journals = group['Journal'].values.tolist()
			providers = group['Provider'].values.tolist()
			counts = group[metric].values.tolist()
			journals_and_provider_dict = dict(zip(journals, providers))
			# if metric == 'References':
			# 	print(journals)
			journals_by_discipline_dict = {}

			journals_by_discipline_dict = {
				'categories': journals,
				'providerMap': journals_and_provider_dict,
				'counts': counts
			}
			
			journals_by_discipline_by_metric_dict[key] = journals_by_discipline_dict

		ret[metric] = journals_by_discipline_by_metric_dict
		
	

	# print(ret)
	# with open('file.txt', 'w') as file:
	#     file.write(json.dumps(ret))
	return ret

# figure8('Downloads JR1 2017')

def get_provider_list():
	journals_by_provider_df = journalsByDisciplineData.groupby(['Provider'], as_index=False)
	provider_list = []
	for key, item in journals_by_provider_df:
		provider_list.append(key)

	return provider_list

def journals_by_provider():
	""" 
	Creates bar graph of the number of references in each field for input provider. 
	Chart Type: Bar Graph 
	Y-Axis: Field 
	Y-Axis Data Source: Journals Per Provider, Domain
	X-Axis: Number of References
	X-Axis Data Source: Journals Per Provider, References
	References are defined as the number of references made by researchers of your institution to an article from a given journal.'
	 """

	metrics = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers']
	journals_by_provider_df = journalsByDisciplineData.groupby(['Provider'], as_index=False).sum()
	# print(journals_by_provider_df)
	# print(journals_by_provider_df.columns)
	
	provider_list = get_provider_list()

	journals_by_provider_dict = { provider: {} for provider in  provider_list}
	
	for index, row in journals_by_provider_df.iterrows():
		for metric in metrics:
			journals_by_provider_dict[row['Provider']][metric] = row[metric] / 2
	
	# print(journals_by_provider_dict)

	ret = { provider: {} for provider in provider_list }
	
	for provider in provider_list:
		for k, v in sorted(journals_by_provider_dict[provider].items(), key=lambda item: float('-inf') if math.isnan(item[1]) else item[1], reverse=True):
			ret[provider][k] = 0.0 if math.isnan(v) else v

	return ret

# journals_by_provider()

# 
def providers_by_metric():
	""" 
	Creates bar graph of the number of references in each field for input provider. 
	Chart Type: Bar Graph 
	Y-Axis: Field 
	Y-Axis Data Source: Journals Per Provider, Domain
	X-Axis: Number of References
	X-Axis Data Source: Journals Per Provider, References
	References are defined as the number of references made by researchers of your institution to an article from a given journal.'
	 """

	metrics = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers']
	journals_by_provider_df = journalsByDisciplineData.groupby(['Provider'], as_index=False).sum()
	print(journals_by_provider_df)
	print(journals_by_provider_df.columns)
	
	journals_by_provider_dict = { metric: {} for metric in metrics }
	
	for index, row in journals_by_provider_df.iterrows():
		for metric in metrics:
			journals_by_provider_dict[metric][row['Provider']] = row[metric] / 2
	
	# print(journals_by_provider_dict)

	ret = { metric: {} for metric in metrics }
	
	for metric in metrics:
		for k, v in sorted(journals_by_provider_dict[metric].items(), key=lambda item: float('-inf') if math.isnan(item[1]) else item[1], reverse=True):
			ret[metric][k] = 0.0 if math.isnan(v) else v

	return ret

# providers_by_metric()
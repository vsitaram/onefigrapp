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

class Data():
    """Object to access all of the 1Figr data"""
    def __init__(self):
        self.original_onefigr_dataset = self._get_data()
        self.onefigr_dataset_with_disciplines = self._make_disciplines_column()
        

    def _get_data(self):
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

    def _make_disciplines_column(self):
        """This generates the disciplines column on the fly for each journal. The disciplines column in a combination of various permutations of each journal's
        domain, field, subfield columns. The discipline column is meant to be something more analagous to departments at the university. The disciplines column does
        not currently exist in the original 1figr dataset and therefore must be generated upon running this function."""

        onefigr_dataset_with_disciplines = self.original_onefigr_dataset.copy()

        #logic for every permutation of domain, field, subfield column with the end result defined in the "disciplines" column    

        #Applied Sciences Domain
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Agriculture, Fisheries & Forestry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Agronomy & Agriculture'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Agriculture, Fisheries & Forestry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Dairy & Animal Science'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Agriculture, Fisheries & Forestry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Fisheries'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Agriculture, Fisheries & Forestry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Food Science'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Agriculture, Fisheries & Forestry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Forestry'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Agriculture, Fisheries & Forestry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Horticulture'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Agriculture, Fisheries & Forestry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Veterinary Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Built Environment & Design') & (onefigr_dataset_with_disciplines['Subfield'] == 'Architecture'), 'Discipline'] = 'Architecture'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Built Environment & Design') & (onefigr_dataset_with_disciplines['Subfield'] == 'Building & Construction'), 'Discipline'] = 'Architecture'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Built Environment & Design') & (onefigr_dataset_with_disciplines['Subfield'] == 'Design Practice & Management'), 'Discipline'] = 'Architecture'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Built Environment & Design') & (onefigr_dataset_with_disciplines['Subfield'] == 'Urban & Regional Planning'), 'Discipline'] = 'Architecture'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Enabling & Strategic Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Bioinformatics'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Enabling & Strategic Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Biotechnology'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Enabling & Strategic Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Energy'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Enabling & Strategic Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Materials'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Enabling & Strategic Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Nanoscience & Nanotechnology'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Enabling & Strategic Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Optoelectronics & Photonics'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Enabling & Strategic Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Strategic, Defence & Security Studies'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Aerospace & Aeronautics'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Automobile Design & Engineering'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Biomedical Engineering'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Chemical Engineering'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Civil Engineering'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Electrical & Electronic Engineering'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Environmental Engineering'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Geological & Geomatics Engineering'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Industrial Engineering & Automation'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Mechanical Engineering & Transports'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Mining & Metallurgy'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Engineering') & (onefigr_dataset_with_disciplines['Subfield'] == 'Operations Research'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Information & Communication Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Artificial Intelligence & Image Processing'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Information & Communication Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Computation Theory & Mathematics'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Information & Communication Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Computer Hardware & Architecture'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Information & Communication Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Distributed Computing'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Information & Communication Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Information Systems'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Information & Communication Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Medical Informatics'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Information & Communication Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Networking & Telecommunications'), 'Discipline'] = 'Engineering'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Applied Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Information & Communication Technologies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Software Engineering'), 'Discipline'] = 'Engineering'

        #Arts & Humanities Domain
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Communication & Textual Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Communication & Media Studies'), 'Discipline'] = 'Communication & Textual Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Communication & Textual Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Languages & Linguistics'), 'Discipline'] = 'Communication & Textual Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Communication & Textual Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Literary Studies'), 'Discipline'] = 'Communication & Textual Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Historical Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Anthropology'), 'Discipline'] = 'Historical Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Historical Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Archaeology'), 'Discipline'] = 'Historical Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Historical Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'Classics'), 'Discipline'] = 'Historical Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Historical Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'History'), 'Discipline'] = 'Historical Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Historical Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'History of Science, Technology & Medicine'), 'Discipline'] = 'Historical Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Historical Studies') & (onefigr_dataset_with_disciplines['Subfield'] == 'History of Social Sciences'), 'Discipline'] = 'Historical Studies'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Philosophy & Theology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Applied Ethics'), 'Discipline'] = 'Philosophy & Theology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Philosophy & Theology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Philosophy'), 'Discipline'] = 'Philosophy & Theology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Philosophy & Theology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Religions & Theology'), 'Discipline'] = 'Philosophy & Theology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Visual & Performing Arts') & (onefigr_dataset_with_disciplines['Subfield'] == 'Art Practice, History & Theory'), 'Discipline'] = 'Visual & Performing Arts'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Visual & Performing Arts') & (onefigr_dataset_with_disciplines['Subfield'] == 'Drama & Theater'), 'Discipline'] = 'Visual & Performing Arts'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Visual & Performing Arts') & (onefigr_dataset_with_disciplines['Subfield'] == 'Folklore'), 'Discipline'] = 'Visual & Performing Arts'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Arts & Humanities') & (onefigr_dataset_with_disciplines['Field'] == 'Visual & Performing Arts') & (onefigr_dataset_with_disciplines['Subfield'] == 'Music'), 'Discipline'] = 'Visual & Performing Arts'
        
        #Economic & Social Sciences Domain
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Accounting'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Agricultural Economics & Policy'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Business & Management'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Development Studies'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Econometrics'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Economic Theory'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Economics'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Finance'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Industrial Relations'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Logistics & Transportation'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Marketing'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Economics & Business') & (onefigr_dataset_with_disciplines['Subfield'] == 'Sport, Leisure & Tourism'), 'Discipline'] = 'Economics & Business'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Criminology'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Cultural Studies'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Demography'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Education'), 'Discipline'] = 'Education'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Family Studies'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Gender Studies'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Geography'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Information & Library Sciences'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'International Relations'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Law'), 'Discipline'] = 'Law'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Political Science & Public Administration'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Science Studies'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Social Sciences Methods'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Social Work'), 'Discipline'] = 'Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Economic & Social Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Sociology'), 'Discipline'] = 'Social Sciences'

        #General Domain
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'General') & (onefigr_dataset_with_disciplines['Field'] == 'General Arts, Humanities & Social Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'General Arts, Humanities & Social Sciences'), 'Discipline'] = 'General Arts, Humanities & Social Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'General') & (onefigr_dataset_with_disciplines['Field'] == 'General Science & Technology') & (onefigr_dataset_with_disciplines['Subfield'] == 'General Science & Technology'), 'Discipline'] = 'General Science & Technology'

        #Health Sciences Domain
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Anatomy & Morphology'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Biochemistry & Molecular Biology'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Biophysics'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Developmental Biology'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Genetics & Heredity'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Microbiology'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Microscopy'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Mycology & Parasitology'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Nutrition & Dietetics'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Physiology'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Toxicology'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biomedical Research') & (onefigr_dataset_with_disciplines['Subfield'] == 'Virology'), 'Discipline'] = 'Biomedical Research'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Allergy'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Anesthesiology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Arthritis & Rheumatology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Cardiovascular System & Hematology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Complementary & Alternative Medicine'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Dentistry'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Dermatology & Venereal Diseases'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Emergency & Critical Care Medicine'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Endocrinology & Metabolism'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Environmental & Occupational Health'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Gastroenterology & Hepatology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'General & Internal Medicine'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'General Clinical Medicine'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Geriatrics'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Immunology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Legal & Forensic Medicine'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Neurology & Neurosurgery'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Nuclear Medicine & Medical Imaging'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Obstetrics & Reproductive Medicine'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Oncology & Carcinogenesis'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Ophthalmology & Optometry'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Orthopedics'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Otorhinolaryngology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Pathology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Pediatrics'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Pharmacology & Pharmacy'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Psychiatry'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Respiratory System'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Sport Sciences'), 'Discipline'] = 'Education'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Surgery'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Tropical Medicine'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Clinical Medicine') & (onefigr_dataset_with_disciplines['Subfield'] == 'Urology & Nephrology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Psychology & Cognitive Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Behavioral Science & Comparative Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Psychology & Cognitive Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Clinical Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Psychology & Cognitive Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Developmental & Child Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Psychology & Cognitive Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Experimental Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Psychology & Cognitive Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'General Psychology & Cognitive Sciences'), 'Discipline'] = 'Psychology & Cognitive Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Psychology & Cognitive Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Human Factors'), 'Discipline'] = 'Psychology & Cognitive Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Psychology & Cognitive Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Psychoanalysis'), 'Discipline'] = 'Psychology & Cognitive Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Psychology & Cognitive Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Social Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Public Health & Health Services') & (onefigr_dataset_with_disciplines['Subfield'] == 'Epidemiology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Public Health & Health Services') & (onefigr_dataset_with_disciplines['Subfield'] == 'Gerontology'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Public Health & Health Services') & (onefigr_dataset_with_disciplines['Subfield'] == 'Health Policy & Services'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Public Health & Health Services') & (onefigr_dataset_with_disciplines['Subfield'] == 'Nursing'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Public Health & Health Services') & (onefigr_dataset_with_disciplines['Subfield'] == 'Public Health'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Public Health & Health Services') & (onefigr_dataset_with_disciplines['Subfield'] == 'Rehabilitation'), 'Discipline'] = 'Health Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Public Health & Health Services') & (onefigr_dataset_with_disciplines['Subfield'] == 'Speech-Language Pathology & Audiology'), 'Discipline'] = 'Education'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Health Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Public Health & Health Services') & (onefigr_dataset_with_disciplines['Subfield'] == 'Substance Abuse'), 'Discipline'] = 'Health Sciences'

        #Natural Sciences Domain
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Ecology'), 'Discipline'] = 'Biology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Entomology'), 'Discipline'] = 'Biology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Evolutionary Biology'), 'Discipline'] = 'Biology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Marine Biology & Hydrobiology'), 'Discipline'] = 'Biology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Ornithology'), 'Discipline'] = 'Biology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Plant Biology & Botany'), 'Discipline'] = 'Biology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Biology') & (onefigr_dataset_with_disciplines['Subfield'] == 'Zoology'), 'Discipline'] = 'Biology'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Chemistry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Analytical Chemistry'), 'Discipline'] = 'Chemistry'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Chemistry') & (onefigr_dataset_with_disciplines['Subfield'] == 'General Chemistry'), 'Discipline'] = 'Chemistry'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Chemistry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Inorganic & Nuclear Chemistry'), 'Discipline'] = 'Chemistry'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Chemistry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Medicinal & Biomolecular Chemistry'), 'Discipline'] = 'Chemistry'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Chemistry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Organic Chemistry'), 'Discipline'] = 'Chemistry'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Chemistry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Physical Chemistry'), 'Discipline'] = 'Chemistry'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Chemistry') & (onefigr_dataset_with_disciplines['Subfield'] == 'Polymers'), 'Discipline'] = 'Chemistry'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Earth & Environmental Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Environmental Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Earth & Environmental Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Geochemistry & Geophysics'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Earth & Environmental Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Geology'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Earth & Environmental Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Meteorology & Atmospheric Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Earth & Environmental Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Oceanography'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Earth & Environmental Sciences') & (onefigr_dataset_with_disciplines['Subfield'] == 'Paleontology'), 'Discipline'] = 'Earth & Environmental Sciences'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Mathematics & Statistics') & (onefigr_dataset_with_disciplines['Subfield'] == 'Applied Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Mathematics & Statistics') & (onefigr_dataset_with_disciplines['Subfield'] == 'General Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Mathematics & Statistics') & (onefigr_dataset_with_disciplines['Subfield'] == 'Numerical & Computational Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Mathematics & Statistics') & (onefigr_dataset_with_disciplines['Subfield'] == 'Statistics & Probability'), 'Discipline'] = 'Mathematics & Statistics'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'Acoustics'), 'Discipline'] = 'Physics & Astronomy'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'Applied Physics'), 'Discipline'] = 'Physics & Astronomy'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'Astronomy & Astrophysics'), 'Discipline'] = 'Physics & Astronomy'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'Chemical Physics'), 'Discipline'] = 'Physics & Astronomy'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'Fluids & Plasmas'), 'Discipline'] = 'Physics & Astronomy'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'General Physics'), 'Discipline'] = 'Physics & Astronomy'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'Mathematical Physics'), 'Discipline'] = 'Physics & Astronomy'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'Nuclear & Particle Physics'), 'Discipline'] = 'Physics & Astronomy'
        onefigr_dataset_with_disciplines.loc[(onefigr_dataset_with_disciplines['Domain'] == 'Natural Sciences') & (onefigr_dataset_with_disciplines['Field'] == 'Physics & Astronomy') & (onefigr_dataset_with_disciplines['Subfield'] == 'Optics'), 'Discipline'] = 'Physics & Astronomy'

        # print(onefigr_dataset_with_disciplines['Discipline'])

        # prints count of number of journals in each discipline
        # print(onefigr_dataset_with_disciplines['Discipline'].value_counts())  #23873 total
        
        return onefigr_dataset_with_disciplines

    def get_disciplines_list(self):
        disciplines_data = self.onefigr_dataset_with_disciplines.groupby(['Discipline'], as_index=False)
        disciplines_list = []
        for key, item in disciplines_data:
            disciplines_list.append(key)

        return disciplines_list

    def journals_and_disciplines_map(self):
        necessary_columns = ['Journal', 'Discipline','Domain']
        figr_data = self.onefigr_dataset_with_disciplines[necessary_columns].dropna()
        # figr_data = figr_data.loc[figr_data['Domain'] != "N/A"]
        journals = figr_data['Journal'].values.tolist()
        disciplines = figr_data['Discipline'].values.tolist()
        journals_and_disciplines_dict = dict(zip(journals, disciplines))

        return journals_and_disciplines_dict

    def journals_by_discipline(self, discipline):
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
        original_1figr_data_with_disciplines = self._make_disciplines_column()[necessary_columns]

        journals_by_discipline_df = original_1figr_data_with_disciplines.groupby(['Discipline'], as_index=False)

        metrics = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers']
        ret = {}

        for metric in metrics:

            group = journals_by_discipline_df.get_group(discipline)[['Journal','Provider', metric]].groupby(['Journal']).agg({metric: 'sum', 'Provider': lambda x: ', '.join(x)})
            group_sorted = group.sort_values(by=[metric], ascending=False, kind='mergesort').fillna(0)
            # print(group_sorted.to_string())
            # print(group_sorted.columns)
            metric_map = group_sorted[metric].to_dict()
            provider_map = group_sorted['Provider'].to_dict()
            percentages = group_sorted[metric] / group_sorted[metric].sum() * 100
            percentages = percentages.apply(lambda x: '{0:.2f}'.format(x))
            percentage_map = percentages.to_dict()

            journals_by_discipline_dict = {
                'metricMap': metric_map,
                'providerMap': provider_map,
                'percentageMap': percentage_map,
                
            }
            
            ret[metric] = journals_by_discipline_dict
            
        return ret

    def get_providers_list(self):
        journals_by_provider_df = self.original_onefigr_dataset.groupby(['Provider'], as_index=False)
        providers_list = []
        for key, item in journals_by_provider_df:
            providers_list.append(key)

        return providers_list

    def journals_by_provider(self, provider):
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
        journals_by_provider_sums = self.original_onefigr_dataset.groupby(['Provider']).sum()
        journals_by_provider_df = journals_by_provider_sums[metrics].loc[provider] / 2
        # print(journals_by_provider_df)
        journals_by_provider_sorted = journals_by_provider_df.sort_values(ascending=False).fillna(0)

        return journals_by_provider_sorted.to_dict()


    def providers_by_metric(self):
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
        journals_by_provider_sums = self.original_onefigr_dataset.groupby(['Provider']).sum()        
        journals_by_provider_dict = { metric: {} for metric in metrics }
        
        for metric in metrics:
            journals_by_provider_df = journals_by_provider_sums[metric] / 2
            journals_by_provider_sorted = journals_by_provider_df.sort_values(ascending=False).fillna(0)
            journals_by_provider_dict[metric] = journals_by_provider_sorted.to_dict()

        return journals_by_provider_dict

            


import pandas as pd
import math
import boto3
import io
import json

from django.conf import settings


class Data():
    """Object to access all of the 1Figr data"""
    def __init__(self):
        # New Provider Names
        self.provider_names_corrections = {
            "AIP": "American Institute of Physics (AIP)",
            "American Chemical Society": "American Chemical Society (ACS)",
            "American Institute of Aeronautics and Astronautics": "American Institute of Aeronautics and Astronautics (AIAA)",
            "American Mathematical Society": "American Mathematical Society (AMS)",
            "American Physical Society": "American Physical Society (APS)",
            "American Psychological Association": "American Psychological Association (APA)",
            "American Society of Civil Engineers": "American Society of Civil Engineers (ASCE)",
            "American Society of Mechanical Engineers": "American Society of Mechanical Engineers (ASME)",
            "Annual Reviews": "Annual Reviews",
            "Association for Computing Machinery": "Association for Computing Machinery (ACM)",
            "BioOne": "BioOne",
            "Brill": "Brill",
            "Cambridge UP": "Cambridge University Press (CUP)",
            "DeGruyter": "DeGruyter",
            "Ebsco": "EBSCO",
            "Elsevier": "Elsevier",
            "Elsevier Freedom": "Elsevier Freedom",
            "Elsevier Subscribed": "Elsevier Subscribed",
            "Emerald": "Emerald",
            "Gale": "Gale",
            "IEEE": "IEEE",
            "IOPscience": "Institute of Physics (IOP)",
            "JSTOR": "JSTOR",
            "Karger": "Karger",
            "MIT Press": "MIT Press",
            "Modern Language Association": "Modern Language Association (MLA)",
            "Ovid": "Ovid",
            "Oxford UP": "Oxford University Press (OUP)",
            "Project MUSE": "Project MUSE",
            "ProQuest": "ProQuest",
            "Royal Society of Chemistry": "Royal Society of Chemistry (RSC)",
            "Sage": "Sage",
            "SPIE": "SPIE",
            "Springer": "Springer Nature",
            "Taylor & Francis": "Taylor & Francis",
            "U Chicago Press": "University of Chicago Press (UCP)",
            "Wiley": "Wiley"
        }
        # To be used for Journals By Discipline
        self.original_onefigr_dataset = self._get_data()
        # To be used by the other pages
        self.onefigr_dataset_with_disciplines = self._make_disciplines_column()
        
        #to be used to get supplemental dataset, which allows comparison for Elsevier journals UVA doesn't subscribe to anymore
        self.supplemental_data = self._get_supplemental_data()


    def _check_AWS_bucket(self):
        """
        Checks: available AWS s3 buckets in UVA library organization,
                name of current working AWS bucket,
                files inside current working AWS bucket
        """
        #print names of all AWS buckets in UVA library organization
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
           print(bucket.name)
        print()

        #print name of current AWS bucket
        print(settings.AWS_STORAGE_BUCKET_NAME)
        print()
        
        #print names of all files in AWS S3 bucket
        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket('onefigrappdev.lib.virginia.edu')
        for file in my_bucket.objects.all():
           print(file.key)



    def _get_data(self):
        """
        Fetches main dataset (JournalsPerProvider_withoutQuotes.xls) from AWS and imports as Pandas DataFrame.
        """
        client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    
        #this retrieves data from AWS 
        object_key = settings.AWS_PRIVATE_FILE_LOCATION + '/' + 'JournalsPerProvider_withoutQuotes.xls'
        obj = client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=object_key)
        data = obj['Body'].read()
        df = pd.read_excel(io.BytesIO(data), encoding='utf-8', skiprows=8)
        df['Provider'] = df['Provider'].apply(lambda x: self.provider_names_corrections[x])
        return df


    def _make_disciplines_column(self):
        """
        Returns Pandas DataFrame of the original dataset (JournalsPerProvider_withoutQuotes.xls) that includes the disciplines column. 

        The disciplines column in a combination of various permutations of each journal's domain, field, subfield columns. 
        The discipline column is meant to be something more analagous to departments at the university. The disciplines column does
        not currently exist in the original 1figr dataset and therefore must be generated upon running this function.
        """

        # Create a copy of original that will include disciplines column
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
        """
        Returns list of disciplines
        """
        disciplines_data = self.onefigr_dataset_with_disciplines.groupby(['Discipline'], as_index=False)
        disciplines_list = []
        for key, item in disciplines_data:
            disciplines_list.append(key)

        return disciplines_list

    def journals_disciplines_and_providers_map(self):
        """
        Returns a dictionary of journals and the associated discipline and provider in a list.
        ex: {New England Journal of Medicine: ['Health Sciences', 'Elsevier']}

        This will be used for the modal in 'Find My Journal' that users use to find the discipline of their journal.
        """
        necessary_columns = ['Journal', 'Discipline', 'Provider']
        figr_data = self.onefigr_dataset_with_disciplines[necessary_columns].dropna()

        journals_disciplines_and_providers_dict = dict(zip(figr_data['Journal'], zip(figr_data['Discipline'], figr_data['Provider'])))

        return journals_disciplines_and_providers_dict

    def journals_by_discipline_chart_data(self, discipline):
        """
        Given a discpline, this returns a dictionary of all of the data related to the discipline that's necessary for the charts in Journals by Disipline.

        For each metric, there are sorted (decreasing) dictionaries called metricMap, providerMap, and percentageMap. 
            metricMap is a dictionary of journal titles and the respective metric. metricMap is used for the frequencies and categories of the bar charts. 
            providerMap is a dictionary of journal titles and the respective providers. providerMap is used to show the provider for each journal in the bar charts. 
            Lastly, percentageMap is a dictionary of journal titles and the respective percentage of the total metric each journal represents. 
        """
        necessary_columns = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers', 'Journal', 'Provider', 'Discipline']
        original_1figr_data_with_disciplines = self._make_disciplines_column()[necessary_columns]

        journals_by_discipline_df = original_1figr_data_with_disciplines.groupby(['Discipline'], as_index=False)

        metrics = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers']
        
        ret = {}

        for metric in metrics:

            group = journals_by_discipline_df.get_group(discipline)[['Journal','Provider', metric]].groupby(['Journal']).agg({metric: 'sum', 'Provider': lambda x: ', '.join(x)})
            
            #For 'References' and 'Publications', for some reason the data was being multiplied by the number of providers.
            #these if statements devide the value by the number of providers
            if metric == 'References':
                group['References'] = group['References']/group['Provider'].str.split(",").str.len()

            if metric == 'Papers':
                group['Papers'] = group['Papers']/group['Provider'].str.split(",").str.len()

            group_sorted = group.sort_values(by=[metric], ascending=False, kind='mergesort').fillna(0)
            

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


    def journals_by_discipline_chart_data_elsevier(self, discipline):
        """
        Given a discpline, this returns a dictionary of all of the data related to the discipline that's necessary for the charts in Journals by Disipline.

        I am removing all journals that are not within the Elsevier provider

        For each metric, there are sorted (decreasing) dictionaries called metricMap, providerMap, and percentageMap. metricMap is a dictionary of journal titles and the respective
        metric. metricMap is used for the frequencies and categories of the bar charts. providerMap is a dictionary of journal titles and the respective 
        providers. providerMap is used to show the provider for each journal in the bar charts. Lastly, percentageMap is a dictionary of journal titles and the 
        respective percentage of the total metric each journal represents. 
        """
        necessary_columns = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers', 'Journal', 'Provider', 'Discipline']
        original_1figr_data_with_disciplines = self._make_disciplines_column()[necessary_columns]

        #this line actually filters the data only to include the Elsevier provider
        original_1figr_data_with_disciplines = original_1figr_data_with_disciplines[original_1figr_data_with_disciplines['Provider'] == 'Elsevier']

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
        """
        Returns a list of all providers.
        """
        journals_by_provider_df = self.original_onefigr_dataset.groupby(['Provider'], as_index=False)
        providers_list = []
        for key, item in journals_by_provider_df:
            providers_list.append(key)

        return providers_list



    def providers_by_metric_chart_data(self):
        """
        This returns a dictionary of all of the data that's necessary for the charts in Providers by Metric.

        There are two dictionaries called providersByMetric and journalCountMap. providersByMetric dictionary of metrics with sorted (decreasing)
        dictionaries of the providers and the respective values for each metric. providersByMetric is used for the categories and frequencies
        of the graphs. journalCountMap is a dictionary of providers and the respective number of journals in each provider.
        """
    
        metrics = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers']
        necessary_columns = ['Downloads JR5 2017 in 2017', 'Downloads JR1 2017', 'References', 'Papers', 'Provider']
        providers_by_metric_sums = self.original_onefigr_dataset[necessary_columns].groupby(['Provider']).sum()     
        providers_by_metric_dict = { metric: {} for metric in metrics }
        
        for metric in metrics:
            # divide by 2 to avoid double counting the provider for the journal group
            providers_by_metric_df = providers_by_metric_sums[metric] / 2 
            providers_by_metric_sorted = providers_by_metric_df.sort_values(ascending=False).fillna(0)
            providers_by_metric_dict[metric] = providers_by_metric_sorted.to_dict()

        # Subtract 1 to avoid counting the provider
        providers_by_journal_count = self.original_onefigr_dataset[['Journal', 'Provider']].groupby(['Provider']).count() - 1
        providers_by_journal_dict = providers_by_journal_count['Journal'].to_dict()
        # print(providers_by_journal_count)

        ret = {
            'providersByMetric': providers_by_metric_dict,
            'journalCountMap': providers_by_journal_dict
        }

        return ret



    def _get_supplemental_data(self):
        """
        Fetches datasets from AWS
        supplemental dataset = (ElsevierNotSubscribed.xls) 
        original dataset = (JournalsPerProvider_withoutQuotes.xls)
        
        The supplemental dataset is a list of Elsevier titles that UVA no longer subscribes to (as of Spring 2021)
        For records in the supplemental dataset, we have an ISSN number. The journal name column not completely correct.
        
        Using the ISSN of the supplemental dataset, we take the matching ISSN from the original dataset to construct the 'compare' column
        Then, using the 'compare' column in the supplemental dataset, we merge the original dataset, for the purposes of getting the original journal title

        We drop the unneeded columns after merging and finally return a list of journal titles (from the original dataset)
        """
        
        client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        #get original dataset
        object_key1 = settings.AWS_PRIVATE_FILE_LOCATION + '/' + 'JournalsPerProvider_withoutQuotes.xls'
        obj1 = client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=object_key1)
        data1 = obj1['Body'].read()
        df_original = pd.read_excel(io.BytesIO(data1), encoding='utf-8', skiprows=8)

        # #get supplemental dataset
        object_key2 = settings.AWS_PRIVATE_FILE_LOCATION + '/' + 'ElsevierNotSubscribed.xls'
        obj2 = client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=object_key2)
        data2 = obj2['Body'].read()
        df_supplemental = pd.read_excel(io.BytesIO(data2), encoding='utf-8')

        #iterate through ISSNs of df_supplemental to find their match in ISSNs of df_original
        match_col = df_original['ISSN/eISSN'].astype(str)
        partial_col = df_supplemental['issn'].astype(str)

        series = []
        for partial_str in partial_col:
            for match_str in match_col:
                if partial_str in match_str:
                    series.append(match_str)
                    break  #there should not be duplicates, but just in case this matches first value found in match_col
            else:   #for loop did not break = no match found
                series.append(None)

        #construct 'compare' column in df_supplemental from series of issns
        df_supplemental['compare'] = series

        #converts empty values to None value
        df_supplemental['compare'].replace('', None, inplace=True)

        #use original dataset ISSN to get journal title ['Journal'] into supplemental dataframe, via a merge
        df_supplemental = pd.merge(df_supplemental, df_original, how='left', left_on='compare', right_on='ISSN/eISSN')

        #for some reason the previous step produces a lot of duplicate results, which are dropped
        df_supplemental = df_supplemental.drop_duplicates(subset='issn', keep='last')

        #drop unneccessary columns from dataframe
        columns_to_drop = ['Unnamed: 0','Sort','Provider','Type','Downloads \nJR1 2014-2017','Downloads JR1 2017','Downloads JR5 2017 in 2017','References',
        'Papers','Synthetic \nUsage','Journal \nTier','Subfield \nTier','Duplicates (JR1 2017)','Papers.1','%','Trend','Papers.2','ARIF',
        'Domain','Field','Subfield',2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,'2008.1','2009.1','2010.1','2011.1','2012.1','2013.1',
        '2014.1','2015.1','2016.1','2017.1','2008.2','2009.2','2010.2','2011.2','2012.2','2013.2','2014.2','2015.2','2016.2','2017.2','2008.3',
        '2009.3','2010.3','2011.3','2012.3','2013.3','2014.3','2015.3','2016.3','2017.3','2008.4','2009.4','2010.4','2011.4','2012.4','2013.4',
        '2014.4','2015.4','2016.4','2017.4','2015.5','2016.5','2017.5',2018,'Unnamed: 77','Unnamed: 78']

        df_supplemental.drop(columns_to_drop, inplace=True, axis=1)

        #makes final list of journal titles for use later
        journal_titles_list = df_supplemental['Journal'].tolist()

        return journal_titles_list




    


    








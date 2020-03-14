import pandas as pd
from io import BytesIO, StringIO 
import requests, zipfile
from pandas_datareader import data as pdr
import numpy as np
from scipy import stats
import yfinance as yf
import datetime as datetime
import calendar
from dateutil.relativedelta import relativedelta
from dateutil import parser
from sklearn import linear_model
import holidays
import statsmodels.api as sm
import boto3
import json
from pytz import timezone
yf.pdr_override() # <== that's all it takes :-)

from decouple import config
import os
from django.conf import settings

def getAIFData():
	# data_AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
	# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
	# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
	# AWS_DATA_LOCATION = config('AWS_DATA_LOCATION')

	client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
	        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

	

	object_key = settings.AWS_PRIVATE_FILE_LOCATION + '/data.csv'
	csv_obj = client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=object_key)
	body = csv_obj['Body']
	csv_string = body.read().decode('utf-8')
	df = pd.read_csv(StringIO(csv_string), skiprows=2, usecols=['Date', 'NAV'], index_col='Date')
	df.drop(df.tail(1).index,inplace=True)
	# print(df.index)
	# df.index = df.index.apply(convertDateFormat)
	df.index = pd.to_datetime(df.index.map(lambda x : convertDateFormat(x)))
	# print(df)
	return df

aifNAVdata = getAIFData()

def AIFNAVDataForTemplate():
	# print(len(aifNAVdata.values.flatten().tolist()))
	return json.dumps(aifNAVdata.values.flatten().tolist())

def AIFIndexDataForTemplate():
	# print(aifNAVdata.index)
	index = pd.Series(aifNAVdata.index).map(lambda x : x.strftime('%m-%d-%Y'))
	# print(index.values.tolist())
	# print(json.dumps(index.values.tolist()))
	# print(len(index.values.tolist()))
	return json.dumps(index.values.tolist())
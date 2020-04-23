import numpy as np
import pandas as pd


df_2011 = pd.read_csv('2011 Stack Overflow Survey Responses.csv', encoding =  "ISO-8859-1", low_memory=False)
df_2012 = pd.read_csv('2012 Stack Overflow Survey Responses.csv', encoding =  "ISO-8859-1", low_memory=False)
df_2013 = pd.read_csv('2013 Stack Overflow Survey Responses.csv', encoding =  "ISO-8859-1", low_memory=False)
df_2014 = pd.read_csv('2014 Stack Overflow Survey Responses.csv', encoding =  "ISO-8859-1", low_memory=False)
df_2015 = pd.read_csv('2015 Stack Overflow Developer Survey Responses.csv', encoding =  "ISO-8859-1", low_memory=False)
df_2016 = pd.read_csv('2016 Stack Overflow Survey Responses.csv', encoding =  "ISO-8859-1", low_memory=False)
df_2017 = pd.read_csv('survey_results_public_2017.csv', encoding =  "ISO-8859-1", low_memory=False)
df_2018 = pd.read_csv('survey_results_public_2018.csv', encoding =  "ISO-8859-1", low_memory=False)
df_2019 = pd.read_csv('survey_results_public_2019.csv', encoding =  "ISO-8859-1", low_memory=False)

print(df_2011.info())
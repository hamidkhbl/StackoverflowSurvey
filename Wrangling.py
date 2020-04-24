import numpy as np
import pandas as pd

def clean():
    # read data
    df_2016 = pd.read_csv('2016 Stack Overflow Survey Responses.csv', encoding =  "ISO-8859-1", low_memory=False)
    df_2017 = pd.read_csv('survey_results_public_2017.csv', encoding =  "ISO-8859-1", low_memory=False)
    df_2019 = pd.read_csv('survey_results_public_2019.csv', encoding =  "ISO-8859-1", low_memory=False)

    # Add year
    df_2016['year'] = 2016
    df_2017['year'] = 2017
    df_2019['year'] = 2019

    # remove null
    df_2016 = df_2016[df_2016.remote.notna()]
    df_2017 = df_2017[df_2017.HomeRemote.notna()]
    df_2019 = df_2019[df_2019.WorkRemote.notna()]

    df_2016_lim = df_2016[['year','remote','job_satisfaction']]
    df_2016_lim.rename(columns = {'job_satisfaction':'CareerSat'}, inplace =True)

    df_2017_lim = df_2017[['year','HomeRemote','CareerSatisfaction']]
    df_2017_lim.rename(columns = {'HomeRemote':'remote', 'CareerSatisfaction':'CareerSat'}, inplace =True)

    df_2019_lim = df_2019[['year','WorkRemote','CareerSat']]
    df_2019_lim.rename(columns = {'WorkRemote':'remote'}, inplace =True)

    df = pd.concat([df_2016_lim,df_2017_lim, df_2019_lim])

    df['remote'].replace("Less than once per month / Never",'Rarely or Never', inplace = True)
    df['remote'].replace("Never",'Rarely or Never', inplace = True)
    df['remote'].replace("I rarely work remotely",'Rarely or Never', inplace = True)

    df['remote'].replace("Less than half the time, but at least one day each week",'Part-time remote', inplace = True)
    df['remote'].replace("About half the time",'Part-time remote', inplace = True)
    df['remote'].replace("More than half, but not all, the time",'Part-time remote', inplace = True)

    df['remote'].replace("All or almost all the time (I'm full-time remote)","Full-time remote", inplace = True)

    df['CareerSat'].replace('I love my job', 'Very satisfied', inplace = True)
    df['CareerSat'].replace("I'm somewhat satisfied with my job", 'Slightly satisfied', inplace = True)
    df['CareerSat'].replace("I'm neither satisfied nor dissatisfied", "Neither satisfied nor dissatisfied", inplace = True)
    df['CareerSat'].replace("I'm somewhat dissatisfied with my job", 'Slightly dissatisfied', inplace = True)
    df['CareerSat'].replace('I hate my job', 'Very dissatisfied', inplace = True)

    df['CareerSat'].replace([9,10], 'Very satisfied', inplace = True)
    df['CareerSat'].replace([8,7], 'Slightly satisfied', inplace = True)
    df['CareerSat'].replace([4,5,6], "Neither satisfied nor dissatisfied", inplace = True)
    df['CareerSat'].replace([3,2], 'Slightly dissatisfied', inplace = True)
    df['CareerSat'].replace([0,1], 'Very dissatisfied', inplace = True)

    df['CareerSat'].replace('Very satisfied',5, inplace = True)
    df['CareerSat'].replace('Slightly satisfied',4, inplace = True)
    df['CareerSat'].replace( "Neither satisfied nor dissatisfied",3, inplace = True)
    df['CareerSat'].replace( 'Slightly dissatisfied',2, inplace = True)
    df['CareerSat'].replace('Very dissatisfied',1, inplace = True)

    df['CareerSat'] = pd.to_numeric(df['CareerSat'], errors='coerce')
    df_careerSat = df.groupby(['remote']).mean()['CareerSat']
    return df_careerSat
print(clean())
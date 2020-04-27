import requests
import os
import zipfile
import datetime
from shutil import copyfile
import glob

survey_2019 = ['survey_2019_files','https://drive.google.com/u/0/uc?id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV&export=download']
survey_2017 = ['survey_2017_files','https://drive.google.com/uc?export=download&id=0B6ZlG_Eygdj-c1kzcmUxN05VUXM']
survey_2016 = ['survey_2016_files','https://drive.google.com/uc?export=download&id=0B0DL28AqnGsrV0VldnVIT1hyb0E']
def downloadCSV(path):
    """
    args: 
        path: path to the file (string)
        unzip: decompress the file if it is compressed

    Download a csv file from internet and return it as a dataframe

    """
    download = not os.path.isdir(path[0])
    # check if files exist
    if download:
        # download file
        r = requests.get(path[1])
        with open(os.path.join(path[0]+'.zip'), mode='wb') as file:
            file.write(r.content)
        # unzip file
        with zipfile.ZipFile(path[0]+'.zip', 'r') as zip_ref:
            zip_ref.extractall(path[0])
        print(datetime.datetime.now(),path[0],"Downloaded")

    else:
        print("Data is already there!")

downloadCSV(survey_2019)
downloadCSV(survey_2017)
downloadCSV(survey_2016)

# copy files to root
copyfile('survey_2019_files\\survey_results_public.csv', '2019_survey_results_public.csv')
copyfile('survey_2016_files\\2016 Stack Overflow Survey Results\\2016 Stack Overflow Survey Responses.csv', '2016_survey_results_public.csv')
copyfile('survey_2017_files\\survey_results_public.csv', '2017_survey_results_public.csv')

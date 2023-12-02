import requests
import pandas as pd
from io import BytesIO
from zipfile import ZipFile

class DataDownloader:
    def __init__(self, weighting='vw_cap', freq='monthly', factor='all_factors', range_='all_regions'):
        # self.url = url
        self.weighting = weighting
        self.freq = freq
        self.factor = factor
        self.range = range_

        self.url = "https://jkpfactors.com/data/["+self.range+"]_["+self.factor+"]_["+self.freq+"]_["+self.weighting+"].zip"

    def download_zip_file(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(self.weighting)

    def extract_csv_from_zip(self, zip_content):
        with ZipFile(BytesIO(zip_content)) as thezip:
            filename = thezip.namelist()[0]
            with thezip.open(filename) as csvfile:
                df = pd.read_csv(csvfile)
            return df

    def get_data(self):
        zip_content = self.download_zip_file()
        return self.extract_csv_from_zip(zip_content)


# Example Usage

downloader = DataDownloader()
try:
    df = downloader.get_data()
    print('Receive the file successfully')
    # Now you can use the DataFrame 'df' as needed
except Exception as e:
    print(e)

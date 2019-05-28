import urllib.request
import os

class DataProvider:

    def __init__(self):
        self._source_path = "data/data.csv"
        self._url = "https://www.dane.gov.pl/media/resources/20190520/Liczba_os%C3%B3b_kt%C3%B3re_przystapi%C5%82y_lub_zda%C5%82y_egzamin_maturalny.csv"  

    def download_data(self):
        if not os.path.isdir("./data"):
            os.mkdir("./data")
        urllib.request.urlretrieve(self._url, self._source_path)

    def get_source_path(self):
        return self._source_path
        

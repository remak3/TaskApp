import pytest
import os
from main.DataProvider import DataProvider

def test_method_download_data():
    data_provider = DataProvider()
    if not os.path.isdir("./data"):
        os.mkdir("./data")
    if os.path.exists("data\data.csv"):
        os.remove("data\data.csv")
    data_provider.download_data()
    assert os.path.exists("data\data.csv") == True, "Test failed."
    os.remove("data\data.csv")
    os.rmdir("./data")
    
def test_get_source_path():
    data_provider = DataProvider()
    data_provider_source_path = "data/data.csv"
    source_path = data_provider.get_source_path()
    assert source_path == data_provider_source_path, "Test failed."

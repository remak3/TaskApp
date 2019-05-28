import codecs
from MatureResult import MatureResult
from TaskManager import TaskManager
from DataProvider import DataProvider
from PerformanceModule import *
from GenderModule import *

class Application:
    
    def __init__(self):
        self._data_list = []
        self._region_set = set()
        self._year_set = set()
        self._data_provider = DataProvider()
        self._get_data()
        self._task_manager = TaskManager(self._data_list, self._region_set, self._year_set)

        
    def _get_data(self):
        self._data_provider.download_data()
        with codecs.open(self._data_provider.get_source_path(), 'r', 'windows-1250') as file:
            lines = file.readlines()
            for line in lines:
                if lines.index(line) != 0:
                    data_line_list = line.split(';')
                    region = data_line_list[0]
                    performance = get_performance(data_line_list[1])
                    gender = get_gender(data_line_list[2])
                    year = int(data_line_list[3])
                    quantity_of_people = int(data_line_list[4])
                    self._data_list.append(MatureResult(region, performance, gender, year, quantity_of_people))
                    if region != "Polska":
                        self._region_set.add(region)
                    self._year_set.add(year)
    def start(self):
        print("Witaj użytkowniku!\n"
              "Ta konsolowa aplikacja potrafi wykonać kilka zadań"
              " na podstawie danych dotyczących liczby osób, które "
              "przystąpiły oraz zdały maturę w latach 2010-2018.\n"
              "1) Oblicza średnią liczbę osób, które przystąpiły "
              "do matury dla danego województwa na przestrzeni lat, do "
              "danego roku włącznie.\n"
              "2) Oblicza zdawalność (w %) dla danego województwa na "
              "przestrzeni lat.\n"
              "3) Podaje województwo o najlepszej zdawalności "
              "w danym roku.\n"
              "4) Wypisuje wszystkie województwa i lata, w których"
              " zanotowano regresję.\n"
              "5) Dla podanych dwóch województw wypisuje, które "
              "z nich miało lepszą zdawalność na przestrzeni lat.")
        while True:
            print("Jeśli nie chcesz nic robić wpisz 0, aby wyjść.")
            user_task_input = input("Wykonaj zadanie: ")
            if user_task_input == "0":
                return
            elif user_task_input == "1":
                self._task_manager.perform_task_one()
            elif user_task_input == "2":
                self._task_manager.perform_task_two()
            elif user_task_input == "3":
                self._task_manager.perform_task_three()
            elif user_task_input == "4":
                self._task_manager.perform_task_four()
            elif user_task_input == "5":
                self._task_manager.perform_task_five()
            else:
                print("Invalid input.")
                return


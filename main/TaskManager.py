from PerformanceModule import *
from GenderModule import *
from YearRegionPassRate import YearRegionPassRate

class TaskManager:

    def __init__(self, data_list, region_set, year_set):
        self._data_list = data_list
        self._region_set = region_set
        self._year_set = year_set

    def perform_task_one(self):
        print("Lista województw: ", self._region_set)
        taskOne_region_input = input("Województwo: ")
        taskOne_year_input = int(input("Wybrany rok: "))
        taskOne_gender_input = get_gender(input("Płeć(M/K): "))
        self._task_one(taskOne_region_input, taskOne_year_input, taskOne_gender_input)

    def perform_task_two(self):
        print("Lista województw: ", self._region_set)
        taskTwo_region_input = input("Województwo: ")
        taskTwo_gender_input = get_gender(input("Płeć(M/K): "))
        self._task_two(taskTwo_region_input, taskTwo_gender_input)

    def perform_task_three(self):
        taskThree_year_input = int(input("Wybrany rok: "))
        taskThree_gender_input = get_gender(input("Płeć(M/K): "))
        self._task_three(taskThree_year_input, taskThree_gender_input)

    def perform_task_four(self):
        taskFour_gender_input = get_gender(input("Płeć(M/K): "))
        self._task_four(taskFour_gender_input)

    def perform_task_five(self):
        print("Lista województw: ", self._region_set)
        taskFive_regionA_input = input("Województwo I: ")
        taskFive_regionB_input = input("Województwo II: ")
        taskFive_gender_input = get_gender(input("Płeć(M/K): "))
        self._task_five(taskFive_regionA_input, taskFive_regionB_input, taskFive_gender_input)
        
    def _task_one(self, region, year, gender):
        if (year >= 2010 and year <= 2018 and region in self._region_set):
            quantity_of_people = [x.quantity_of_people for x in self._data_list if (x.region == region and x.performance == Performance.ATTENDED and x.year <= year and (gender == Gender.DEFAULT or x.gender == gender))]
            if year != 2010:
                print("2010 -", year, ":", round(sum(quantity_of_people)/len(quantity_of_people), 2))
            else:
                print("2010:", round(sum(quantity_of_people)/len(quantity_of_people), 2))
        else:
            print("Invalid input.")

    def _task_two(self, region, gender):
        if (region in self._region_set):
            for year in sorted(self._year_set):
                quantity_of_people_attended = [x.quantity_of_people for x in self._data_list if (x.region == region and x.performance == Performance.ATTENDED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)]
                quantity_of_people_passed = [x.quantity_of_people for x in self._data_list if (x.region == region and x.performance == Performance.PASSED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)]
                print("Rok: ", year, "-", int(round(sum(quantity_of_people_passed)/sum(quantity_of_people_attended), 2)*100), "%")
        else:
            print("Invalid input.")

    def _task_three(self, year, gender):
        year_region_pass_rate_list = []
        best_region_pass_rate_list = []
        if (year >= 2010 and year <= 2018):
            for region in self._region_set:
                pass_rate = sum([x.quantity_of_people for x in self._data_list if (x.region == region and x.performance == Performance.PASSED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)])/sum([x.quantity_of_people for x in self._data_list if (x.region == region and x.performance == Performance.ATTENDED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)])
                year_region_pass_rate_list.append(YearRegionPassRate(year, region, pass_rate))
            for i in range(0, len(year_region_pass_rate_list)):
                best_region_pass_rate_list.append(year_region_pass_rate_list[i].pass_rate)
            best_pass_rate = max(best_region_pass_rate_list)
            region = [x.region for x in year_region_pass_rate_list if (x.pass_rate == best_pass_rate)][0]
            print(region,":", int(round(best_pass_rate, 2)*100),"%")
        else:
            print("Invalid input.")

    def _task_four(self, gender):
        year_region_pass_rate_list = []
        for region in self._region_set:
            for year in sorted(self._year_set):
                pass_rate = sum([x.quantity_of_people for x in self._data_list if (x.region == region and x.performance == Performance.PASSED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)])/sum([x.quantity_of_people for x in self._data_list if (x.region == region and x.performance == Performance.ATTENDED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)])
                year_region_pass_rate_list.append(YearRegionPassRate(year, region, pass_rate))
        for i in range(1, len(year_region_pass_rate_list)):
            if (year_region_pass_rate_list[i].pass_rate < year_region_pass_rate_list[i-1].pass_rate and year_region_pass_rate_list[i].region == year_region_pass_rate_list[i-1].region):
                print(year_region_pass_rate_list[i].region,":", year_region_pass_rate_list[i-1].year,"->", year_region_pass_rate_list[i].year)

    def _task_five(self, regionA, regionB, gender):
        if ((regionA and regionB in self._region_set) and regionA != regionB):
            year_region_pass_rate_list = []
            for year in sorted(self._year_set):
                pass_rateA = sum([x.quantity_of_people for x in self._data_list if (x.region == regionA and x.performance == Performance.PASSED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)])/sum([x.quantity_of_people for x in self._data_list if (x.region == regionA and x.performance == Performance.ATTENDED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)])
                pass_rateB = sum([x.quantity_of_people for x in self._data_list if (x.region == regionB and x.performance == Performance.PASSED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)])/sum([x.quantity_of_people for x in self._data_list if (x.region == regionB and x.performance == Performance.ATTENDED) and x.year == year and (gender == Gender.DEFAULT or x.gender == gender)])
                if pass_rateA >= pass_rateB:
                    year_region_pass_rate_list.append(YearRegionPassRate(year, regionA, pass_rateA))
                if pass_rateA <= pass_rateB:
                    year_region_pass_rate_list.append(YearRegionPassRate(year, regionB, pass_rateB))
            for i in range(0, len(year_region_pass_rate_list)):
                print(year_region_pass_rate_list[i].year,"-", year_region_pass_rate_list[i].region)
        else:
            print("Invalid input.")


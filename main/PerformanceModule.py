from enum import Enum
class Performance(Enum):
     ATTENDED = 0
     PASSED = 1

ATTENDED = "przystąpiło"
PASSED = "zdało"

def get_performance(performance):
   if performance == ATTENDED:
       return Performance.ATTENDED
   elif performance == PASSED:
       return Performance.PASSED

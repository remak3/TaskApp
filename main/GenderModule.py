from enum import Enum
class Gender(Enum):
    MALE = 0
    FEMALE = 1
    DEFAULT = 2

MALE = "mężczyźni"
FEMALE = "kobiety"

def get_gender(gender):
    if gender == MALE or gender == "M":
        return Gender.MALE
    elif gender == FEMALE or gender == "K":
        return Gender.FEMALE
    else:
        return Gender.DEFAULT

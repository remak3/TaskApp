import pytest
from main.GenderModule import *

def test_get_gender_returns_Gender_MALE_for_mezczyzni():
    gender = "mężczyźni"
    assert get_gender(gender) == Gender.MALE, "Test failed."

def test_get_gender_returns_Gender_MALE_for_M():
    gender = "M"
    assert get_gender(gender) == Gender.MALE, "Test failed."

def test_get_gender_returns_Gender_FEMALE_for_kobiety():
    gender = "kobiety"
    assert get_gender(gender) == Gender.FEMALE, "Test failed."

def test_get_gender_returns_Gender_FEMALE_for_K():
    gender = "K"
    assert get_gender(gender) == Gender.FEMALE, "Test failed."

def test_get_gender_returns_Gender_DEFAULT_for_empty_string():
    gender = ""
    assert get_gender(gender) == Gender.DEFAULT, "Test failed."

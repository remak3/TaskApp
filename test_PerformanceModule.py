import pytest
from main.PerformanceModule import *

def test_get_performance_returns_performance_ATTENDED_for_przystapilo():
    performance = "przystąpiło"
    assert get_performance(performance) == Performance.ATTENDED, "Test failed."

def test_get_performance_returns_performance_PASSED_for_zdalo():
    performance = "zdało"
    assert get_performance(performance) == Performance.PASSED, "Test failed."

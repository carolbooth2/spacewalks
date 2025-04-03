from eva_data_analysis import text_to_duration
from eva_data_analysis import (
    text_to_duration,
    calculate_crew_size
)

import pytest


def test_text_to_duration_float():
    """
    test that text to duration returns expected ground truth values for typical durations with a non-zero minutes component
    """
    actual_result = text_to_duration("10:20")
    expected_result = 10.333333333
    assert text_to_duration("10:20") == pytest.approx(10.333333333)

def test_text_to_duration_integer():
    """
    Test that the text_to_duration function returns expected ground truth values
    for typical whole hour durations
    """
    actual_result = text_to_duration("10:00")
    expected_result = 10
    assert text_to_duration("10:00") == 10

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valen;",1),
    ("one astronaut; another astronaut;",2)
])
def test_calculate_crew_size_(input_value):
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result


def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns ground truth values for edge cases
    where crew is empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None



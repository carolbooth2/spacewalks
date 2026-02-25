from eva_data_analyis import text_to_duration, calculate_crew_size
import pytest

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected values for typical
    durations with a zero minutes component
    """
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values for
    typical durations with non-zero minutes components
    """
    assert text_to_duration("10:20") == pytest.approx(10.333333) 

def test_calculate_crew_size():
    """
    Test that calculate_crew_size returns expected size for 
    typical crew values
    """
    actual_result = calculate_crew_size("Valentina Tereshkova;")
    expected_result = 1
    assert actual_result == expected_result

    actual_result = calculate_crew_size("Judith Smith; Sally Rider;")
    expected_result = 2
    assert actual_result == expected_result

def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected values for an edge 
    case where crew is an empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result == None
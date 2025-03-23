"""Tests for the data facade"""
import pytest
import os
import pandas as pd
from calculator.data_facade import CalculatorDataFacade

@pytest.fixture
def data_facade():
    """Create a data facade for testing"""
    facade = CalculatorDataFacade()
    facade.clear_all_history()
    return facade

def test_record_calculation(data_facade):
    """Test recording a calculation"""
    record_id = data_facade.record_calculation("add", 5, 3, 8)
    history = data_facade.get_calculation_history()
    
    assert len(history) == 1
    assert history.iloc[0]['operation'] == "add"
    assert history.iloc[0]['first_number'] == 5
    assert history.iloc[0]['second_number'] == 3
    assert history.iloc[0]['result'] == 8

def test_get_last_calculation(data_facade):
    """Test getting the last calculation"""
    data_facade.record_calculation("add", 5, 3, 8)
    data_facade.record_calculation("multiply", 4, 2, 8)
    
    last = data_facade.get_last_calculation()
    assert last['operation'] == "multiply"

def test_clear_all_history(data_facade):
    """Test clearing all history"""
    data_facade.record_calculation("add", 5, 3, 8)
    data_facade.clear_all_history()
    
    history = data_facade.get_calculation_history()
    assert len(history) == 0

def test_delete_calculation(data_facade):
    """Test deleting a specific calculation"""
    data_facade.record_calculation("add", 5, 3, 8)
    record_id = data_facade.record_calculation("multiply", 4, 2, 8)
    
    success = data_facade.delete_calculation(record_id)
    assert success is True
    
    history = data_facade.get_calculation_history()
    assert len(history) == 1
    assert history.iloc[0]['operation'] == "add"

def test_export_and_import_history(data_facade):
    """Test exporting and importing history"""
    # Add some test data
    data_facade.record_calculation("add", 5, 3, 8)
    data_facade.record_calculation("multiply", 4, 2, 8)
    
    # Export to a test file
    test_export_file = "test_export.csv"
    data_facade.export_history_to_csv(test_export_file)
    
    # Clear history
    data_facade.clear_all_history()
    assert len(data_facade.get_calculation_history()) == 0
    
    # Import from the test file
    data_facade.import_history_from_csv(test_export_file)
    
    # Verify data was imported
    history = data_facade.get_calculation_history()
    assert len(history) == 2
    
    # Clean up test file
    if os.path.exists(test_export_file):
        os.remove(test_export_file)
"""Tests for pandas history manager"""
import pytest
import pandas as pd
import os
from calculator.history_manager import HistoryManager

@pytest.fixture
def history_manager():
    """Create history manager for testing"""
    manager = HistoryManager()
    manager.clear_history()
    return manager

def test_add_calculation(history_manager):
    """Test adding a calculation to history"""
    index = history_manager.add_calculation("add", 5, 3, 8)
    history = history_manager.get_history()
    
    assert len(history) == 1
    assert history.iloc[0]['operation'] == "add"
    assert history.iloc[0]['first_number'] == 5
    assert history.iloc[0]['second_number'] == 3
    assert history.iloc[0]['result'] == 8

def test_get_last_calculation(history_manager):
    """Test retrieving last calculation"""
    history_manager.add_calculation("add", 5, 3, 8)
    history_manager.add_calculation("multiply", 4, 2, 8)
    
    last = history_manager.get_last_calculation()
    assert last['operation'] == "multiply"
    assert last['first_number'] == 4
    assert last['second_number'] == 2
    assert last['result'] == 8

def test_clear_history(history_manager):
    """Test clearing history"""
    history_manager.add_calculation("add", 5, 3, 8)
    history_manager.clear_history()
    
    history = history_manager.get_history()
    assert len(history) == 0

def test_delete_record(history_manager):
    """Test deleting specific record"""
    history_manager.add_calculation("add", 5, 3, 8)
    index = history_manager.add_calculation("multiply", 4, 2, 8)
    
    history_manager.delete_record(index)
    history = history_manager.get_history()
    
    assert len(history) == 1
    assert history.iloc[0]['operation'] == "add"

def test_save_and_load_history(history_manager):
    """Test saving and loading history"""
    # Add some test data
    history_manager.add_calculation("add", 5, 3, 8)
    history_manager.add_calculation("multiply", 4, 2, 8)
    
    # Save history
    history_manager.save_history()
    
    # Create a new instance which should load the saved history
    new_manager = HistoryManager()
    loaded_history = new_manager.get_history()
    
    assert len(loaded_history) == 2
    
    # Clean up
    os.remove(history_manager.history_file)
"""Tests for calculation strategies"""
import pytest
from calculator.strategies.basic_strategy import BasicStrategy
from calculator.strategies.advanced_strategy import AdvancedStrategy

@pytest.fixture
def basic_strategy():
    """Create basic strategy for testing"""
    return BasicStrategy()

@pytest.fixture
def advanced_strategy():
    """Create advanced strategy for testing"""
    return AdvancedStrategy()

# Basic Strategy Tests
def test_basic_add(basic_strategy):
    """Test basic addition"""
    result = basic_strategy.calculate("add", 5, 3)
    assert result == 8

def test_basic_subtract(basic_strategy):
    """Test basic subtraction"""
    result = basic_strategy.calculate("subtract", 5, 3)
    assert result == 2

def test_basic_multiply(basic_strategy):
    """Test basic multiplication"""
    result = basic_strategy.calculate("multiply", 5, 3)
    assert result == 15

def test_basic_divide(basic_strategy):
    """Test basic division"""
    result = basic_strategy.calculate("divide", 6, 3)
    assert result == 2

def test_basic_divide_by_zero(basic_strategy):
    """Test division by zero raises error"""
    with pytest.raises(ZeroDivisionError):
        basic_strategy.calculate("divide", 5, 0)

def test_basic_unknown_operation(basic_strategy):
    """Test unknown operation raises error"""
    with pytest.raises(ValueError):
        basic_strategy.calculate("unknown", 5, 3)

# Advanced Strategy Tests
def test_advanced_add(advanced_strategy):
    """Test advanced addition"""
    result = advanced_strategy.calculate("add", 5, 3)
    assert result == 8

def test_advanced_subtract(advanced_strategy):
    """Test advanced subtraction"""
    result = advanced_strategy.calculate("subtract", 5, 3)
    assert result == 2

def test_advanced_multiply(advanced_strategy):
    """Test advanced multiplication"""
    result = advanced_strategy.calculate("multiply", 5, 3)
    assert result == 15

def test_advanced_divide(advanced_strategy):
    """Test advanced division"""
    result = advanced_strategy.calculate("divide", 6, 3)
    assert result == 2

def test_advanced_power(advanced_strategy):
    """Test power operation"""
    result = advanced_strategy.calculate("power", 2, 3)
    assert result == 8

def test_advanced_root(advanced_strategy):
    """Test root operation"""
    result = advanced_strategy.calculate("root", 8, 3)
    assert pytest.approx(result, 0.001) == 2

def test_advanced_log(advanced_strategy):
    """Test logarithm operation"""
    result = advanced_strategy.calculate("log", 8, 2)
    assert pytest.approx(result, 0.001) == 3

def test_advanced_invalid_root(advanced_strategy):
    """Test invalid root raises error"""
    with pytest.raises(ValueError):
        advanced_strategy.calculate("root", -4, 2)

def test_advanced_invalid_log(advanced_strategy):
    """Test invalid logarithm raises error"""
    with pytest.raises(ValueError):
        advanced_strategy.calculate("log", -1, 2)
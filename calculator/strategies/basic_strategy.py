"""Basic calculation strategy implementation"""
from calculator.strategies.calculation_strategy import CalculationStrategy
from calculator.logger import logger

class BasicStrategy(CalculationStrategy):
    """Basic strategy for performing calculations"""
    
    def calculate(self, operation, a, b):
        """
        Execute basic calculation
        
        Args:
            operation (str): Operation name (add, subtract, multiply, divide)
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Result of calculation
        """
        logger.debug(f"BasicStrategy: Calculating {a} {operation} {b}")
        
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError(f"Unknown operation: {operation}")
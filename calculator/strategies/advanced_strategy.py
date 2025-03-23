"""Advanced calculation strategy with additional features"""
from calculator.strategies.calculation_strategy import CalculationStrategy
from calculator.logger import logger
import math

class AdvancedStrategy(CalculationStrategy):
    """Advanced strategy with additional mathematical operations"""
    
    def calculate(self, operation, a, b):
        """
        Execute advanced calculation
        
        Args:
            operation (str): Operation name
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Result of calculation
        """
        logger.debug(f"AdvancedStrategy: Calculating {a} {operation} {b}")
        
        # Support basic operations
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
            
        # Advanced operations
        elif operation == 'power':
            return math.pow(a, b)
        elif operation == 'root':
            if a < 0 and b % 2 == 0:
                raise ValueError("Cannot take even root of negative number")
            return math.pow(a, 1/b)
        elif operation == 'log':
            if a <= 0 or b <= 0 or b == 1:
                raise ValueError("Invalid values for logarithm")
            return math.log(a, b)
        else:
            raise ValueError(f"Unknown operation: {operation}")
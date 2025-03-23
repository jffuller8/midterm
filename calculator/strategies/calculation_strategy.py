"""Strategy pattern for calculation approaches"""
from abc import ABC, abstractmethod

class CalculationStrategy(ABC):
    """Abstract base class for calculation strategies"""
    
    @abstractmethod
    def calculate(self, operation, a, b):
        """
        Execute calculation using specific strategy
        
        Args:
            operation (str): Operation to perform
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Result of calculation
        """
        pass
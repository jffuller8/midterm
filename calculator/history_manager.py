"""History management using Pandas"""
import os
import pandas as pd
from datetime import datetime
from calculator.logger import logger
from calculator.singleton import Singleton

class HistoryManager(metaclass=Singleton):
    """Manages calculation history using pandas DataFrame"""
    
    def __init__(self):
        """Initialize history manager with empty DataFrame"""
        self.history_file = "calculation_history.csv"
        self.columns = ["timestamp", "operation", "first_number", "second_number", "result"]
        
        if os.path.exists(self.history_file):
            logger.info(f"Loading existing history from {self.history_file}")
            self.history = pd.read_csv(self.history_file)
        else:
            logger.info("Creating new history DataFrame")
            self.history = pd.DataFrame(columns=self.columns)
    
    def add_calculation(self, operation, a, b, result):
        """Add calculation to history"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_record = pd.DataFrame({
            "timestamp": [now],
            "operation": [operation],
            "first_number": [a],
            "second_number": [b],
            "result": [result]
        })
        
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        logger.info(f"Added calculation to history: {operation}({a}, {b}) = {result}")
        
        return self.history.index.max()  # Return index of new record
    
    def get_history(self):
        """Return full history DataFrame"""
        return self.history
    
    def get_last_calculation(self):
        """Return the most recent calculation"""
        if len(self.history) == 0:
            logger.warning("History is empty, no last calculation")
            return None
        
        return self.history.iloc[-1]
    
    def save_history(self):
        """Save history to CSV file"""
        self.history.to_csv(self.history_file, index=False)
        logger.info(f"History saved to {self.history_file}")
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = pd.DataFrame(columns=self.columns)
        logger.info("History cleared")
    
    def delete_record(self, index):
        """Delete specific record by index"""
        if index in self.history.index:
            self.history = self.history.drop(index)
            logger.info(f"Deleted record at index {index}")
            return True
        else:
            logger.warning(f"No record found at index {index}")
            return False
    
    def get_operations_summary(self):
        """Get summary of operations used"""
        if len(self.history) == 0:
            return pd.DataFrame()
        
        return self.history['operation'].value_counts().reset_index(
            name='count').rename(columns={'index': 'operation'})
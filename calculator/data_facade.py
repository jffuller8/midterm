"""Facade pattern implementation for data operations"""
from calculator.history_manager import HistoryManager
from calculator.logger import logger

class CalculatorDataFacade:
    """Facade that provides simplified interface for data operations"""
    
    def __init__(self):
        """Initialize the facade with a history manager"""
        self.history_manager = HistoryManager()
    
    def record_calculation(self, operation, a, b, result):
        """Record a calculation in history"""
        record_id = self.history_manager.add_calculation(operation, a, b, result)
        self.history_manager.save_history()
        return record_id
    
    def get_calculation_history(self):
        """Get full calculation history"""
        return self.history_manager.get_history()
    
    def get_last_calculation(self):
        """Get most recent calculation"""
        return self.history_manager.get_last_calculation()
    
    def clear_all_history(self):
        """Clear all calculation history"""
        self.history_manager.clear_history()
        self.history_manager.save_history()
        logger.info("All calculation history cleared")
    
    def delete_calculation(self, index):
        """Delete specific calculation by index"""
        success = self.history_manager.delete_record(index)
        if success:
            self.history_manager.save_history()
        return success
    
    def get_operation_statistics(self):
        """Get statistics about operation usage"""
        return self.history_manager.get_operations_summary()
    
    def export_history_to_csv(self, filename):
        """Export history to a specific CSV file"""
        history = self.history_manager.get_history()
        history.to_csv(filename, index=False)
        logger.info(f"History exported to {filename}")
        return True
    
    def import_history_from_csv(self, filename):
        """Import history from a specific CSV file"""
        try:
            import pandas as pd
            imported_data = pd.read_csv(filename)
            self.history_manager.history = imported_data
            self.history_manager.save_history()
            logger.info(f"History imported from {filename}")
            return True
        except Exception as e:
            logger.error(f"Error importing history: {str(e)}")
            return False
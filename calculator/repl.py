"""REPL Implementation with Pandas Integration"""
import os
from dotenv import load_dotenv
from calculator.plugin_loader import PluginLoader
from calculator.logger import logger
from calculator.data_facade import CalculatorDataFacade
from calculator.strategies.basic_strategy import BasicStrategy
from calculator.strategies.advanced_strategy import AdvancedStrategy

# Load environment variables
load_dotenv()

class CalculatorREPL:
    """Calculator REPL with pandas integration"""
    
    def __init__(self):
        """Initialize the REPL"""
        logger.debug("Initializing Calculator REPL")
        self.plugins = PluginLoader.load_plugins()
        self.data_facade = CalculatorDataFacade()
        
        # Load strategy based on environment variable
        strategy_name = os.getenv("CALCULATOR_STRATEGY", "basic")
        if strategy_name.lower() == "advanced":
            self.strategy = AdvancedStrategy()
            logger.info("Using advanced calculation strategy")
        else:
            self.strategy = BasicStrategy()
            logger.info("Using basic calculation strategy")
            
        logger.info(f"Loaded plugins: {list(self.plugins.keys())}")
        self.running = True
    
    def show_menu(self):
        """Display available commands"""
        logger.debug("Showing menu")
        print("\nAvailable Commands:")
        print("------------------")
        print("Calculations:")
        for command, plugin in self.plugins.items():
            print(f"  {command:<8} - {plugin.get_description()}")
        
        print("\nHistory Management:")
        print("  history  - Show calculation history")
        print("  last     - Show last calculation")
        print("  clear    - Clear calculation history")
        print("  export   - Export history to CSV")
        print("  import   - Import history from CSV")
        print("  stats    - Show operation statistics")
        
        print("\nSystem:")
        print("  menu     - Show this menu")
        print("  exit     - Quit the calculator")
    
    def exit_repl(self):
        """Exit the REPL"""
        logger.info("Exiting calculator")
        self.running = False
    
    def show_history(self):
        """Display calculation history"""
        history = self.data_facade.get_calculation_history()
        if len(history) == 0:
            print("No calculation history available")
        else:
            print("\nCalculation History:")
            print(history)
    
    def show_last_calculation(self):
        """Display last calculation"""
        last = self.data_facade.get_last_calculation()
        if last is None:
            print("No calculations in history")
        else:
            print("\nLast Calculation:")
            print(last)
    
    def clear_history(self):
        """Clear calculation history"""
        self.data_facade.clear_all_history()
        print("Calculation history cleared")
    
    def export_history(self):
        """Export history to CSV file"""
        filename = input("Enter filename for export: ")
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        success = self.data_facade.export_history_to_csv(filename)
        if success:
            print(f"History exported to {filename}")
    
    def import_history(self):
        """Import history from CSV file"""
        filename = input("Enter filename to import: ")
        if not os.path.exists(filename):
            print(f"File not found: {filename}")
            return
            
        success = self.data_facade.import_history_from_csv(filename)
        if success:
            print(f"History imported from {filename}")
        else:
            print("Error importing history")
    
    def show_statistics(self):
        """Show operation statistics"""
        stats = self.data_facade.get_operation_statistics()
        if len(stats) == 0:
            print("No statistics available (empty history)")
        else:
            print("\nOperation Statistics:")
            print(stats)
    
    def run(self):
        """Run the REPL"""
        logger.info("Starting REPL")
        print("Welcome to Calculator with Pandas Integration!")
        self.show_menu()
        
        while self.running:
            try:
                # Read
                command = input("\nEnter command: ").lower().strip()
                logger.debug(f"User entered command: {command}")
                
                # Handle system commands
                if command == 'exit':
                    self.exit_repl()
                    continue
                elif command == 'menu':
                    self.show_menu()
                    continue
                
                # Handle history commands
                elif command == 'history':
                    self.show_history()
                    continue
                elif command == 'last':
                    self.show_last_calculation()
                    continue
                elif command == 'clear':
                    self.clear_history()
                    continue
                elif command == 'export':
                    self.export_history()
                    continue
                elif command == 'import':
                    self.import_history()
                    continue
                elif command == 'stats':
                    self.show_statistics()
                    continue
                
                # Handle calculation commands
                if command not in self.plugins:
                    logger.warning(f"Unknown command: {command}")
                    print("Unknown command. Type 'menu' for available commands.")
                    continue
                
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                logger.debug(f"Operation: {command} {a} {b}")
                
                # Execute plugin
                try:
                    # Use strategy pattern for calculation
                    result = self.strategy.calculate(command, a, b)
                    
                    # Record in history using facade
                    self.data_facade.record_calculation(command, a, b, result)
                    
                    logger.info(f"Calculation result: {command}({a},{b}) = {result}")
                    print(f"Result: {result}")
                except Exception as e:
                    logger.error(f"Calculation error: {str(e)}")
                    print(f"Error: {str(e)}")
                
            except ValueError as e:
                logger.error(f"Invalid input: {str(e)}")
                print("Invalid number input. Please try again.")
            except Exception as e:
                logger.exception(f"Unexpected error: {str(e)}")
                print(f"An error occurred: {str(e)}")
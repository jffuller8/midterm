# Advanced Calculator Application

This calculator application features a robust architecture with pandas integration, multiple design patterns, and comprehensive logging.

## Features

### Core Calculator Functionality
- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced mathematical operations (power, root, logarithm)
- Comprehensive testing suite with pytest

### Calculation History Management
- Pandas-based history tracking and management
- Load, save, and export history to CSV files
- Operation statistics and summaries
- Delete individual records or clear entire history

### Design Patterns Implementation
- **Command Pattern**: Structured calculator operations as command objects
- **Strategy Pattern**: Different calculation approaches based on configuration
- **Facade Pattern**: Simplified interface for pandas data operations
- **Singleton Pattern**: Single instance for history management
- **Plugin Architecture**: Dynamically load calculator operations

### Logging and Configuration
- Comprehensive logging system with multiple severity levels (INFO, WARNING, ERROR)
- Dynamic log configuration through environment variables
- Both console and file logging capabilities

## Installation

```bash
# Clone the repository
git clone git@github.com:yourusername/midterm.git

# Or clone with HTTPS
git clone https://github.com/yourusername/midterm.git

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file with the following variables:
```
ENV_NAME=development
CALCULATOR_LOG_LEVEL=DEBUG  # Options: DEBUG, INFO, WARNING, ERROR
CALCULATOR_NAME="Advanced Calculator with Pandas"
CALCULATOR_STRATEGY=basic   # Options: basic, advanced
```

## Usage

Run the calculator:
```bash
python main.py
```

### Calculator Commands

**Calculation Operations:**
- `add` - Add two numbers
- `subtract` - Subtract second number from first
- `multiply` - Multiply two numbers
- `divide` - Divide first number by second
- `power` - Raise first number to power of second (advanced mode only)
- `root` - Calculate nth root (advanced mode only)
- `log` - Calculate logarithm with custom base (advanced mode only)

**History Management:**
- `history` - Show calculation history
- `last` - Show last calculation
- `clear` - Clear calculation history
- `export` - Export history to CSV
- `import` - Import history from CSV
- `stats` - Show operation statistics

**System Commands:**
- `menu` - Show available commands
- `exit` - Quit calculator

## Design Patterns Explained

### Command Pattern
The calculator uses the Command pattern to encapsulate operations as objects, allowing for:
- Uniform interface for different operations
- Separation of operation request from execution
- Easy addition of new operations

```python
# Example command implementation
class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return Calculator.add(self.a, self.b)
```

### Strategy Pattern
The Strategy pattern allows dynamic selection of calculation algorithms:
- Basic strategy for simple operations
- Advanced strategy for complex mathematical operations
- Configurable via environment variables

### Facade Pattern
A Facade pattern simplifies access to the complex Pandas operations:
- Hides complexity of data operations
- Provides a unified interface for history management
- Encapsulates data handling details

### Singleton Pattern
The Singleton ensures a single instance of the history manager:
- Consistent access to calculation history
- Prevents duplicate instances
- Centralized history management

### Plugin Architecture
The calculator implements a dynamic plugin system:
- Auto-discovery of operation plugins
- Easy extension with new operations
- Separation of operation implementations

## Testing

Run tests with coverage reporting:
```bash
pytest --cov=calculator tests/
```

## Logging

Logs are stored in `calculator.log` with configurable verbosity through the `CALCULATOR_LOG_LEVEL` environment variable.
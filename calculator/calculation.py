
    @classmethod
    def get_history(cls) -> list:
        """Get all calculations history"""
        return cls._history

    @classmethod
    def get_last_calculation(cls) -> str:
        """Get most recent calculation"""
        return cls._history[-1] if cls._history else None # pylint: disable=C0304
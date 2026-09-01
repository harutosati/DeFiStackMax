# test_defistackmax.py
"""
Tests for DeFiStackMax module.
"""

import unittest
from defistackmax import DeFiStackMax

class TestDeFiStackMax(unittest.TestCase):
    """Test cases for DeFiStackMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeFiStackMax()
        self.assertIsInstance(instance, DeFiStackMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeFiStackMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

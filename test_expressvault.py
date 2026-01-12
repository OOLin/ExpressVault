# test_expressvault.py
"""
Tests for ExpressVault module.
"""

import unittest
from expressvault import ExpressVault

class TestExpressVault(unittest.TestCase):
    """Test cases for ExpressVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ExpressVault()
        self.assertIsInstance(instance, ExpressVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ExpressVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

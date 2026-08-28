# test_blockapex.py
"""
Tests for BlockApex module.
"""

import unittest
from blockapex import BlockApex

class TestBlockApex(unittest.TestCase):
    """Test cases for BlockApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockApex()
        self.assertIsInstance(instance, BlockApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

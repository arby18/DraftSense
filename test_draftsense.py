# test_draftsense.py
"""
Tests for DraftSense module.
"""

import unittest
from draftsense import DraftSense

class TestDraftSense(unittest.TestCase):
    """Test cases for DraftSense class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftSense()
        self.assertIsInstance(instance, DraftSense)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftSense()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

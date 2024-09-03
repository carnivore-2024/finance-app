import unittest
from unittest.mock import patch, mock_open
import finance as bec

class TestBreakEvenCalculator(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data="item1#10.0@20.0\nitem2#15.0@25.0\n")
    def test_items(self, mock_file):
        item = []
        costPrice = []
        sellingPrice = []
        bec.items(item, costPrice, sellingPrice)
        
        self.assertEqual(item, ["item1", "item2"])
        self.assertEqual(costPrice, [10.0, 15.0])
        self.assertEqual(sellingPrice, [20.0, 25.0])
  
if __name__ == "__main__":
    unittest.main()

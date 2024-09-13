import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(price, (bid_price + ask_price) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(price, (bid_price + ask_price) / 2)

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_zeroValues(self):
    quotes = [
        {'top_ask': {'price': 0.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    ]
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(price, (bid_price + ask_price) / 2)

def test_getRatio_zeroValues(self):
    # Test ratio when price_b is zero
    with self.assertRaises(ValueError):
        getRatio(10, 0)
        
        
#case for very large value(Edge case)   
def test_getDataPoint_largeValues(self):
    quotes = [
        {'top_ask': {'price': 1e6, 'size': 10}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1e6 - 0.01, 'size': 10}, 'id': '0.109974697771', 'stock': 'ABC'}
    ]
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(price, (bid_price + ask_price) / 2)

def test_getRatio_largeValues(self):
    # Test ratio with large values
    ratio = getRatio(1e6, 1e5)
    self.assertAlmostEqual(ratio, 10)


#function to handle empty and malfomd data 

def test_getDataPoint_emptyQuotes(self):
    quotes = [{}]
    for quote in quotes:
        with self.assertRaises(KeyError):
            getDataPoint(quote)

def test_getRatio_emptyValues(self):
    # Test ratio with no values
    with self.assertRaises(TypeError):
        getRatio(None, None)





if __name__ == '__main__':
    unittest.main()

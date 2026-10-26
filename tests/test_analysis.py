import unittest

from src.analyze_sales import summarize_sales

class TestSalesAnalysis(unittest.TestCase):

def setUp(self):
    self.sales = [
        {"product": "Laptop", "region": "South", "quantity": 2,
         "unit_price": 450, "revenue": 900},
        {"product": "Mouse", "region": "East", "quantity": 10,
         "unit_price": 15, "revenue": 150},
        {"product": "Laptop", "region": "West", "quantity": 1,
         "unit_price": 450, "revenue": 450},
    ]

def test_total_orders(self):
    result = summarize_sales(self.sales)
    self.assertEqual(result["total_orders"], 3)

def test_total_revenue(self):
    result = summarize_sales(self.sales)
    self.assertEqual(result["total_revenue"], 1500)

def test_revenue_by_product(self):
    result = summarize_sales(self.sales)
    self.assertEqual(result["product_revenue"]["Laptop"], 1350)
    self.assertEqual(result["product_revenue"]["Mouse"], 150)

def test_revenue_by_region(self):
    result = summarize_sales(self.sales)
    self.assertEqual(result["region_revenue"]["South"], 900)
    self.assertEqual(result["region_revenue"]["East"], 150)
    self.assertEqual(result["region_revenue"]["West"], 450)

if name == "main":
unittest.main()

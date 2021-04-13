import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_price(self):
    prod = Product('Test Product')
    assert prod.price == 10
    
def test_default_product_weight(self):
    prod = Product('Test Weight')
    assert prod.weight == 20
    
def test_product_stealability(self):
    prod = Product(generate_products())
    assert (prod.stealability > 0) and (prod.stealability < 1)
    
def test_default_num_products(self):
    assert len(Product) == 30
    
def test_legal_names(self):
    assert Product.first_name in ADJECTIVES
    assert Product.last_name in NOUNS
    

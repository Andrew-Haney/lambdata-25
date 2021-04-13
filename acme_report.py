# from sprint_challenge.acme import Product
from random import randint, sample, uniform
import random
# from sprint_challenge.acme_report import generate_products, inventory_report

ADJECTIVES = ['Awesome', 'Shiny', 
              'Impressive', 'Portable', 
              'Improved']
NOUNS = ['Anvil', 'Catapult', 
         'Disguise', 'Mousetrap', 
         '???']

def generate_products(num_products = 30):
    """Can't seem to get this one for some reason"""
    rand_list = ADJECTIVES, NOUNS
    products = []
    # for i in range(len(rand_list)):
    first_name = random.sample(ADJECTIVES, k= 1)
    last_name = random.sample(NOUNS, k= 1)
    name = str(first_name + last_name).replace(',', ' ').replace('[', '').replace(']', '').replace("'", '').replace('  ', ' ')
    price = random.randint(5,101)
    weight = random.randint(5,101)
    flammability = random.uniform(0.0, 2.6)
    product_list = [name, price, weight, flammability]
    while len(products) < 30:
        products.append(product_list)
    if len(products) == 30:
        return products
                                     

def inventory_report(generate_products):
    print('Unique product names: ', generate_products(Product.name).nunique())
    print ('Average price: ', generate_products(Product.price).mean())
    print('Average weight: ', generate_products(Product.weight).mean())
    print ('Average flammability: ', generate_products(Product.flammability).mean())
    
    
if __name__ == '__main__':
    inventory_report(generate_products())
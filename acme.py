import random

class Product(object):
    def __init__(self, 
                 name, 
                 price= 10, 
                 weight= 20,
                 flammability= 0.5, 
                 identifier= random.randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def name(self):
        """Provides name of Product"""
        return self.name
    
    def price(self):
        """Provides price of Product"""
        return self.price
    
    def weight(self):
        """Provides weight of Product"""
        return self.weight
    
    def flammability(self):
        """Provides flammability level of product"""
        return self.flammability
    
    def identifier(self):
        """Provides identifier of Product"""
        random.randint(1000000, 10000000)
        return self.identifier
    
    
    def stealability(self):
        """Calculates the price divided by weight"""
        #stealability = float(self.price/self.weight)
        if (float(self.price/self.weight) < 0.5):
            return 'Not so stealable...'
        elif ((float(self.price/self.weight) >= 0.5) and 
              float(self.price/self.weight) < 1.0):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'
        
    def explode(self):
        """Calculates the flammability times weight"""
        if ((self.flammability*self.weight) < 10):
            return ('...fizzle')
        elif (((self.flammability*self.weight) >= 10) and
              (self.flammability*self.weight) < 50):
            return ('...boom!')
        else:
            return ('...BABOOM!!')
        
        
class BoxingGlove(Product):
    """Create subclass of Product"""
    def __init__(self, name, price= 10, weight= 10,
                 flammability= 0.5,
                 identifier= random.randint(1000000, 10000000)):
        super().__init__(name, price, weight, flammability, identifier)

    
    def explode(self):
        """Redefine explode"""
        return ('''...it's a glove''')
    
    def punch(self):
        """Define hurt level of punch based on glove weight"""
        if ((self.weight) < 5):
            return ('That tickles.')
        elif (((self.weight) >= 5) and
            (self.weight) < 15):
            return ('Hey that hurt!')
        else:
            return ('OUCH!')
        

        

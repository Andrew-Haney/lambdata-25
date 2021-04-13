class Wallet:
    """Define starting amount in wallet"""
    def __init__(self, start_amt = 0):
        self.balance = start_amt

        
    def spend(self, amount):
        """Define spending for wallet"""
        if self.balance < amount:
            print('Insufficient Funds')
        else: 
            self.balance -= amount
            return amount
        
    def add_cash(self, amount):
        """Define adding cash"""
        self.balance += amount
        return amount
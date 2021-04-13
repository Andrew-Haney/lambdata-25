import pytest
from lambdata.wallet_class import Wallet

@pytest.fixture
def empty_wallet():
    """Returns a wallet with a zero balance"""
    wallet = Wallet()
    return wallet

@pytest.fixture
def wallet():
    """Returns wallet with a balance of 500"""
    return Wallet(500)

def test_wallet_current_amt(empty_wallet):
    """Make sure current amount function is working properly"""
    assert empty_wallet.balance == 0
    
def test_setting_current_amt(wallet):
    """Make sure setting the current balance 
       function is working properly"""
    assert wallet.balance == 500
    
def test_wallet_spend(wallet):
    """Make sure the spend function is working properly"""
    wallet.spend(150)
    assert wallet.balance == 350
    
def test_wallet_add_cash(wallet):
    """Make sure the add cash function is working properly"""
    wallet.add_cash(70)
    assert wallet.balance == 570
    
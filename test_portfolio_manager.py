from portfolio_manager import *
# need to be commented out if not the unit test wont pass in github
# import alpaca_trade_api as tradeapi

x = TradeSession()

def test_connect_api():
    assert x.connect_api() != ""
    assert x.connect_api().trading_blocked == False

#def test_lookup_stock():
#    pass

def test_show_buying_power():
    y = TradeSession()
    assert y.show_buying_power() == x.show_buying_power()

def test_show_gain_loss():
    y = TradeSession()
    assert y.show_gain_loss() == x.show_gain_loss()

#def test_list_all_assets():
#    pass

def test_is_tradable():
    assert x.is_tradable(asset = 'AAPL') is True
    assert x.is_tradable(asset = 'BTCUSD') is True
    assert x.is_tradable(asset = 'ULBR') is False

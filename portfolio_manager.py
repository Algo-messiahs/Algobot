import alpaca_trade_api as tradeapi
#from simple_term_menu import TerminalMenu
import os
import config

class TradeSession:

    def __init__(self):
        self.api = tradeapi.REST(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY,
                            base_url=config.APCA_API_BASE_URL,api_version='v2')

    # Account Connectivity Test
    def connect_api(self):
        account = self.api.get_account()
        return account

    # Checking for stock testing
    def look_up_stock(self):
        userInput = input("Enter Stock Name Example Apple(AAPL)")
        aapl = self.api.get_barset(userInput, 'day')
        print(aapl.df)
        return aapl.df

    #ACCOUNT
    def show_buying_power(self):
        account = self.api.get_account()

        # Check if our account is restricted from trading.
        if account.trading_blocked:
            print('Account is currently restricted from trading.')

        # Check how much money we can use to open new positions.
        print('${} is available as buying power.'.format(account.buying_power))
        return account.buying_power

    def show_gain_loss(self):
        account = self.api.get_account()

        # Check our current balance vs. our balance at the last market close
        balance_change = float(account.equity) - float(account.last_equity)
        print(f'Today\'s portfolio balance change: ${balance_change}')
        return balance_change

    def list_all_assets(self):
        # Get a list of all active assets.
        active_assets =seld. api.list_assets(status='active')

        #Filter the assets down to just those on NASDAQ.
        nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
        print(nasdaq_assets)

        #check if stock market is open
        api = tradeapi.REST()
        # Check if the market is open now.
        clock = api.get_clock()
        print('The market is {}'.format('open.' if clock.is_open else 'closed.'))
        # Check when the market was open on Dec. 1, 2018
        date = '2018-12-01'
        calendar = api.get_calendar(start=date, end=date)[0]
        print('The market opened at {} and closed at {} on {}.'.format(
            calendar.open,
            calendar.close,
            date
        ))

    def is_tradable(self,asset):
        my_asset = self.api.get_asset(asset)
        if my_asset.tradable:
            return True
        return False

    # CLI that selects user bot options
print("--------------------------------------------------------------------------")
print("                     Welcome to AlgoBot Project                           ")
print("--------------------------------------------------------------------------")
print("               Please select opton you would like to do                   ")
def CLI():
    options = ["Account Connectivity", "Get Account Balance", "Look up Stock Price"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    # check account is connected
    # Get account Balance
    # Look up Stock
    # set stocks
    # Set buy price
    # set sell price


if __name__ == '__main__':
    x = TradeSession()
    x.show_buying_power()
    #CLI()

    #print("Current buying power: ",x.show_buying_power())
    #print("Gain/Loss: ",x.show_gain_loss())
    #x.list_assets()
    #x.list_all_assets(api)
    #print(x.is_tradable(api,"AAPL"))

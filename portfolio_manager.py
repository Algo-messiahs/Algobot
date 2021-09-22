import alpaca_trade_api as tradeapi
import os
import config
import sys

class TradeSession:

    def __init__(self):
        self.api = tradeapi.REST(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY,
                            base_url=config.APCA_API_BASE_URL,api_version='v2')

    # Account Connectivity Test
    def connect_api(self):
        account = self.api.get_account()
        print(account)
        return account
        

    # Checking for stock testing
    def look_up_stock(self):
        userInput = input("Enter Stock Name Example Apple(AAPL): ")
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
        active_assets =self. api.list_assets(status='active')

        #Filter the assets down to just those on NASDAQ.
        nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
        print(nasdaq_assets)

        # check if stock market is open
        # Was getting a error so made its own function for market is open
    def market_is_open(self):
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
    # It is used to call from the test 
    # It is connected to the Alpaca API as well 
def cli():
    print("--------------------------------------------------------------------------")
    print("                     Welcome to AlgoBot Project                           ")
    print("--------------------------------------------------------------------------")
    print("              Please select number opton you would like to do             ")
    print("                                                                          ")
    print("1. Account Information")
    print("2. Buying Power")
    print("3. List Assets")
    print("4. Show Gains and Losses")
    print("5. Look Up Stock Price")
    print("6. Exit AlgoBot Project") 
def menu():
    cli()
    ''' Main menu to choose an item ''' 
    chosen_element = 0
    chosen_element = input("Enter a selection from 1 to 6: ")
    if int(chosen_element) == 1:
        print('Account Information')
        x.connect_api()
        menu()
        # Call Account information Method
    elif int(chosen_element) == 2:
        # Call Stock Price Look up methond
        print('Your buying power is: ')
        x.show_buying_power()
        menu()
    elif int(chosen_element) == 3:
        # call List of Assets Method
        print('List of Assets')
        x.list_all_assets()
        menu()
    elif int(chosen_element) == 4:
        # Call Gains and Losses 
        print('Your Gains and Losses\n')
        print("Gain/Loss: ",x.show_gain_loss())
        menu() # keeps menu tab open to make next selection and not close
    elif int(chosen_element) == 5:
        # Look up stock price 
        # this has user input so the user will have to input stock they would like to look up 
        # example Tesla = TSLA, Apple = AAPL etc
        print('Look Up Stock Price')
        x.look_up_stock()
        menu()
        # exits the menu when 6 is selected. 
    elif int(chosen_element) == 6:
        print('Goodbye!')
        sys.exit() 
    else:
        print('Sorry, the value entered must be a number from 1 to 5, then try again!')


if __name__ == '__main__':
    x = TradeSession()
    menu()
    cli()
    # for testing purposes
    #x.show_buying_power()
    #print("Current buying power: ",x.show_buying_power())
    #print("Gain/Loss: ",x.show_gain_loss())
    #x.list_assets()
    #x.list_all_assets(api)
    #print(x.is_tradable(api,"AAPL"))
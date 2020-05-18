# Name of the file (without .py extension!) that contains the bot
bot_name = 'bots.bot_template'

# Datasource is poloniex or cryptocompare
datasource = 'binance'

revenyou_api_url = 'https://youhexpaper.revenyou.io/api/signal/v1/signal'

# Data settings real time data poloniex
data_settings_poloniex = {
    'pair': 'BTC_ETH',  # Use ETH pricing data on the BTC market
    'period': 1800,       # Use 1800 second candles
    'days_history': 10,  # Collect 10 days data
    'bot_function_interval': 1800 # the bot function is called every 1800 seconds (half an hour)
}

# Data settings real time data cryptocompare
data_settings_cryptocompare = {
    'pair': ['ETH', 'BTC'],  # Use ETH pricing data on the BTC market
    'days_history': 100,  # Collect 100 days data
    'exchange': 'Bitfinex', # Exchange that is used
    'bot_function_interval': 1800 # the bot function is called every 1800 seconds (half an hour)
}

# Data settings real time data binance
data_settings_binance = {
    'pair': 'ETHBTC',  # Use ETH pricing data on the BTC market
    'max_length_ticker_data_array': 20, # the bot function receives a maximum of 20 ticker data at a time (the most recent ones)
    'bot_function_interval': 5000 # the bot function is called every 5000 miliseconds (5 seconds)
}

buy_signal_settings = {
    'signal_provider': '[NAME OF BOT]',
    'signal_provider_key': '[KEY]',
    'exchange': datasource,
    'symbol': 'ETHBTC', # Must be in line with the data settings object pair value!  
    'price_limit': '100', # Buy BTC with a price limit of 100 ETH
    'buy_ttl_sec': 1800, # Time (in seconds) for buy order to live
    'take_profit_price_percentage_60': '5', # Take 60% profit when price of BTC goes up with 5%
    'take_profit_price_percentage_40': '10', # Take 40% profit when price of BTC goes up with 10%
    'stop_loss_price_percentage': '5', # Close position (stop loss) when price of BTC  goes down with 5%
    'panic_sell_price_percentage': '20',
    "panic_sell_price_deviation_percentage": '2'
}

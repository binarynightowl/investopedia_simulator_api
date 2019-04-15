from api_models import Portfolio
from parsers import Parsers, option_lookup, stock_quote
from trade_common import Duration, OrderType, TradeType, Trade, StockTrade, OptionTrade
from session_singleton import Session

class InvestopediaApi(object):
    def __init__(self,auth_cookie):
        Session.login(auth_cookie)
        self.portfolio = Parsers.get_portfolio()
        self.open_orders = self.portfolio.open_orders
    class Trade:
        class StockTrade(StockTrade):
            pass
        class OptionTrade(OptionTrade):
            pass
        class Duration(Duration):
            pass
        class OrderType(OrderType):
            pass
        class TradeType(TradeType):
            pass

    
    @staticmethod
    def get_option_chain(symbol,strike_price_proximity=3):
        return option_lookup(symbol,strike_price_proximity=strike_price_proximity)

    @staticmethod
    def get_stock_quote(symbol):
        return stock_quote(symbol)


    def refresh_portfolio():
        self.portfolio = Parsers.get_portfolio()
        self.open_orders = self.portfolio.open_orders




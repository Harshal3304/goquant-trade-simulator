from collections import defaultdict

class OrderBook:
    def __init__(self):
        self.bids={}
        self.asks={}

    def update(self,tick_data:dict):
        "Update order book using incoming L2 tick"
        new_bids = tick_data.get("bids",[])
        new_asks = tick_data.get("asks",[])

        for price,size in new_bids:
            price=float(price)
            size = float(size)
            if size==0:
                self.bids.pop(price,None)
            else:
                self.bids[price]=size
            
        for price, size in new_asks:
            price= float(price)
            size = float(size)
            if size == 0:
                self.asks.pop(price,None)
            else:
                self.asks[price]=size
        

    def get_top_of_book(self):
        """Return top bid and top ask"""
        top_bid = max(self.bids.items(), default=(None, None))
        top_ask = min(self.asks.items(), default=(None, None))
        return top_bid, top_ask

    def __str__(self):
        bid, ask = self.get_top_of_book()
        return f"Top Bid: {bid} | Top Ask: {ask}"
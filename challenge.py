import csv
filename = "mempool.csv"

class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight=int(weight)
        self.parents=int(parents)
        
# TODO: add code to parseself weight and parents fields
    def parse_mempool_csv():
        with open('mempool.csv') as f:
            
            return([MempoolTransaction(*line.strip().split(',')) for line in f.readlines()])
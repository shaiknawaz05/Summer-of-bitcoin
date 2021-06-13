import csv

'''
class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight=int(weight)
        self.parents=int(parents)              
'''


with open('mempool.csv',"r") as f: 
    #opening the csv file
    txid = csv.reader(f, delimiter =',')   
    #collecting the txid from the csv without ',' by using delimiter
    for row in txid:
        for cell in row:
            output = row[0]
          #  fee = row[1]

    #iterating the txid over rows and print it
        print(output)
       # print(fee)
        """
        
        Total txid are 5214
        Total fee 5696031
        weight total < 4000000
        Time complexity O(n^2)
        referred to
        https://www.geeksforgeeks.org/reading-csv-files-in-python/
        
        """
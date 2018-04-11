#!/usr/bin/env python3.6
#import urllib
import requests
import bs4 as bs

class Quote(object):

    def __init__(self,scrip):
        self.scrip = scrip

    def getQuote(self):
        if self.scrip == 'NSEI' or self.scrip == 'NSEBANK':
            QuotePage = 'https://in.finance.yahoo.com/quote/%5E'+ self.scrip +'?p=%5E'+ self.scrip
        else:
            QuotePage = 'https://in.finance.yahoo.com/quote/'+ self.scrip +'.NS/?p='+ self.scrip +'.NS'
        try:
            #Quote ='https://in.finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI'
            #Page = urllib.request.urlopen(Quote).read()
            page = requests.get(QuotePage).text
            Soup1 = bs.BeautifulSoup(page,'lxml')
            Data1 = Soup1.find(id="quote-header-info").prettify()

            Soup2 = bs.BeautifulSoup(Data1,'lxml')

            ScripData = []
            for string in Soup2.stripped_strings:
                ScripData.append(string)
            #print("ScripData"+ str(ScripData))
            S_Name = ScripData[0]
            S_LTP = float(ScripData[2].replace(',',''))
            S_PosNeg = ScripData[3]
            S_DIFF = ScripData[4]
            S_TIME = ScripData[5]
            return[S_Name, S_LTP, S_PosNeg, S_DIFF, S_TIME]
        except:
            return "Yahoo Quote Not available for " + self.scrip
    
    def __str__(self):
        return "Collects Quote from Yahoo site for : " + self.scrip
"""
    def display(S_Name,S_LTP,S_PosNeg,S_DIFF,S_TIME):
        print("SCRIP: "+ S_Name)
        print("LTP: "+ str(S_LTP))
        print("DIFF: "+ (S_PosNeg + S_DIFF))
        print(S_TIME)
"""

NSE = Quote('NSEI')
BPCL = Quote('BPCL')
TATASTEEL = Quote('TATASTEEL1')
print(NSE.getQuote())
print(BPCL.getQuote())
print(TATASTEEL.getQuote())
#print(TATASTEEL)


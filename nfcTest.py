from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import *

# a simple card observer that prints inserted/removed cards
class printobserver( CardObserver ):
    def update( self, observable, (addedcards, removedcards) ):
        for card in addedcards:
            print "+Inserted: ", toHexString( card.atr )
        for card in removedcards:
            print "-Removed: ", toHexString( card.atr )
            print card.atr

##try:
def main():
    print "Insert or remove a smartcard in the system."
    print "This program will exit in 10 seconds"
    print ""
    cardmonitor = CardMonitor()
    cardobserver = printobserver()
    cardmonitor.addObserver( cardobserver )

if __name__ == '__main__':
    main()

from bitcoin import *
# https://github.com/vbuterin/pybitcointools

class Wallet:
 
    priv = ""
    pub = ""
    address = ""
     
    def createWallet(self,brainwalletpassword):
        self.priv = sha256(brainwalletpassword)
        self.pub = privtopub(self.priv)
        self.address = pubtoaddr(self.pub)
 
        print("Address : " + self.address)
 
    def balance(self):
        print(unspent(self.address))

    def sendBTC(self,dst, amount):
        h = history(self.address)
        #print h
        outs = [{'value': amount, 'address': dst}]
        fee = 1000
        tx = mksend(h,outs, self.address, fee)
        tx2 = sign(tx,0,self.priv)
        pushtx(tx2)
 
    def multisendBTC(self,dst1, dst2, amount):
        h = history(self.address)
        #print h
        h = unspent(self.address)
        outs = [{'value': amount, 'address': dst1},{'value': amount, 'address': dst2}]
        fee = 1000
        tx = mksend(h,outs, self.address, fee)
        tx2 = sign(tx,0,self.priv)
        pushtx(tx2)

txamount=2000
print("Send 2000 + 1000 + 1000 to this address :")
gatheringWallet = Wallet()
gatheringWallet.createWallet("gathering wallet password")
bci = "https://blockchain.info/address/"
print(bci+gatheringWallet.address)
gatheringWallet.balance()
print(multiaccess(unspent(gatheringWallet.address),'output'))
#print history(gatheringWallet.address)
 
print("Each of the following address will receive 1000 :")
recipientWalletA = Wallet()
recipientWalletA.createWallet("recipient wallet A")
recipientWalletA.balance()
recipientWalletB = Wallet()
recipientWalletB.createWallet("recipient wallet B")
recipientWalletB.balance()

#split a transaction

equalsplit = txamount / 2
# must take txfees into account
print("Sending "+str(equalsplit)+" to "+recipientWalletA.address)
print("Sending "+str(equalsplit)+" to "+recipientWalletB.address)
#gatheringWallet.multisendBTC(recipientWalletA.address, recipientWalletB.address, equalsplit)
#gatheringWallet.multisendBTC(recipientWalletA.address, recipientWalletB.address, 2000)

#web interface
# https://docs.djangoproject.com/en/1.5/intro/tutorial01/#creating-models

#web interface AJAXified
# especially to show that the transaction has been broadacsted

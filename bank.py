import random


class bank:
    __accountNo = 994
    __holderName = "Anshuman M. Sharma"
    __password = 994
    __bal = 994
    __tokenLogin = False
    __tranID = 0

    def getAccountNo(self):
        return self.__accountNo

    def setAccountNo(self, accountNo):
        self.__accountNo = accountNo

    def getHolderName(self):
        return self.__holderName

    def setHolderName(self, holderName):
        self.__holderName = holderName

    def getBal(self):
        return self.__bal

    def setBal(self, bal):
        self.__bal = bal

    def genTransID(self):
        self.__tranID = random.randrange(12372, stop=99499, step=23)
        return self.__tranID


    def makeDeduction(self, itemAmount):
        total = self.__bal - itemAmount
        if total > 0:
            self.genTransID()
            return True
        else:
            self.__tranID = 0
            return False

    def checkLogin(self, accountNo, password):
        if self.__accountNo == accountNo:
            if self.__password == password:
                self.__tokenLogin = True
        else:
            self.__tokenLogin = False

    def getToken(self):
        return self.__tokenLogin;

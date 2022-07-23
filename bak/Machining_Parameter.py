
class Parameters:

    def __init__(self):
        #
        self.__ON = '0'
        self.__MA = '0'
        self.__SV = '0'
        self.__UP = '0'
        self.__C = '0'
        self.__S = '0'
        self.__LN = '0'
        self.__STEP = '0'
        self.__L = '0'
        self.__LP = '0'
    @property
    def ON(self):
        return self.__ON
    @property
    def MA(self):
        return self.__MA
    @property
    def SV(self):
        return self.__SV
    @property
    def UP(self):
        return self.__UP
    @property
    def C(self):
        return self.__C
    @property
    def S(self):
        return self.__S
    @property
    def LN(self):
        return self.__LN
    @property
    def STEP(self):
        return self.__STEP
    @property
    def L(self):
        return self.__L
    @property
    def LP(self):
        return self.__LP


    @ON.setter
    def ON(self, value):
        self.__ON = value
    @MA.setter
    def MA(self, value):
        self.__MA = value
    @SV.setter
    def SV(self, value):
        self.__SV = value
    @UP.setter
    def UP(self, value):
        self.__UP = value
    @C.setter
    def C(self, value):
        self.__C = value
    @S.setter
    def S(self, value):
        self.__S = value
    @LN.setter
    def LN(self, value):
        self.__LN = value
    @STEP.setter
    def STEP(self, value):
        self.__STEP = value
    @L.setter
    def L(self, value):
        self.__L = value
    @LP.setter
    def LP(self, value):
        self.__LP = value
    def Print_ALL_Propertys(self):
        print(self.LP)
        print(self.UP)
        print(self.SV)
        print(self.L)
        print(self.STEP)
        print(self.S)
        print(self.MA)
        print(self.ON)
        print(self.LN)
        print(self.C)
    def Load_Setting(self,ulist):
        i = 0
        self.__ON = ulist[i]
        i = i + 1
        self.__MA = ulist[i]
        i = i + 1
        self.__SV = ulist[i]
        i = i + 1
        self.__UP = ulist[i]
        i = i + 1
        self.__C = ulist[i]
        i = i + 1
        self.__S = ulist[i]
        i = i + 1
        self.__LN = ulist[i]
        i = i + 1
        self.__STEP = ulist[i]
        i = i + 1
        self.__L = ulist[i]
        i = i + 1
        self.__LP = ulist[i]
if __name__ == "__main__":
    n = Discharge_Codition()
    n.ON = '50'
    n.MA = '20'
    n.SV = '30'
    n.UP = '1'
    n.V = '500'
    n.S = '1'
    n.LN = '5'
    n.STEP = '3'
    n.L = '4'
    n.LP = '6'
    n.C = '3'
    n.Print_ALL_Propertys()

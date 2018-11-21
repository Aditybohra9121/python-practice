class LogicGate:
    def __init__(self,label):
        self.label=label
        self.output=None
    def getOutput():
        self.output=self.performGateLogic()
        return self.output
    def getName(self):
        return self.label
class Binary(LogicGate):
    def __init__(self,label):
        LogicGate.__init__(self,label)
        self.PinA=None
        self.PinB=None
    def getPinA(self):
        self.PinA=input("Enter Input PinA for"+self.getName()+"-->:")
    def getPinB(self):
        self.PinB=input("Enter Input PinB for"+self.getName()+"-->:")
class Unary(LogicGate):
    def __init__(self,label):
        LogicGate.__init__(self,label)
        self.Pin=None
    def getPin(self):
        self.Pin=input("Enter Input Pin for"+self.getName()+"-->:")
    
class OrGate(Binary):
    def __init__(self,label):
        Binary.__init__(self,label)
    def performGateLogic(self):
        if a==0 and b==0:
            return 0
        else:
            return 1
class AndGate(Binary):
    def __init__(self,label):
        Binary.__init__(self,label)
    def performGateLogic(self):
        if a==1 and b==1:
            return 1
        else:
            return 0
class Connector:
    def __init__(self,fgate,tgate):
        self.from_gate=fgate
        self.to_gate=tgate


org=OrGate("or")
print org.getName()
org.getPinA()
org.getPinB()

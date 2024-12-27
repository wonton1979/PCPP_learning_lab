class Scanner:
    @staticmethod
    def scan():
        print('scan() method from Scanner class')

class Printer:
    def print(self):
        print('print() method from Printer class')


class Fax():
    def send(self):
        print('send() method from Fax class')
    def print(self):
        print('print() method from Fax class')


class MFD_SPF(Scanner,Printer,Fax):
    pass

class MFD_SFP(Scanner,Fax,Printer):
    pass


MFD_SPF().scan()
MFD_SFP().scan()
MFD_SPF().print()
MFD_SFP().print()
MFD_SPF().send()
MFD_SFP().send()

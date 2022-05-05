class ATM(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def balanceEnquiry(self):
        print("Your Balance Is")

    def cashWithdrawal(self):
        print("The Amount You Want WithDraw")

    def EnterOTP(self):
        print("Enter OTP")

    def Language(self):
        print("Language")

    def transactionType(self):
        print("TransactionType")


print("WELCOME !!")

a = input("Select Your Language :")
print("Your Selected Language Is " + a)

b = input("Select Your TransactionType :")
print("Your Selected Transaction Type is " + b)

print("Enter Your CardNumber and PinNumber - ")
print("Your Entered CardNumber and PinNumber are :")
person1 = ATM("134","2586")
print(person1.cardNumber)
print(person1.pinNumber)

c = input("Enter the " + b + " Amount :")
d = input("Enter your OTP for "+ b + ":")

print("Your OTP Is Correct !!")
print(b + " Approved...")
print("Collect Your Money...")




import qrcode
import random
def deposit():
    print("*********************************************")
    amount=float(input("Enter amount to be deposited :" ))
    print("*********************************************")

    
    if amount<0:
        print("Thats Not a Valid Amount !")
        return 0
    else:
        return amount

def widthdraw():
    print("*********************************************")
    amount=float(input("Enter amount to be withdrawn :"))
    print("*********************************************")

    if amount>balance:
        print("Not having enough money")
    elif amount<0:
        print("Amount must be greater than 0")
    else:
         return amount
def showbalance():
      print("******************************")
      print(f"your balance is Rs{balance: .2f}")
      print("******************************")

def showQR():
    a=str(balance)
    qr1=qrcode.make("your available balance is :"+a + "/n" + "Thank you For Banking with Us !!!!!")
    qr1.save('balance.png')
    print("*******************************")
    print("Your QR Code has Been Generated Kindly Check it out !")
    print("*******************************")

       
balance=0
is_running=True
print("**********************************************")
print("-----------welcome to Sre's Bank--------------")
print("**********************************************")
while is_running:
    print("1.show balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.show QR CodeS For Details !")
    print("5.Exit")
    
    
    choice=input("Enter your choice(1-4): ")
    
    if choice=='1':
        showbalance()
        
    elif choice=='2':
        balance+=deposit()
        
    elif choice=='3':
        print("*********************************************")
        print("Security Verification OPT Required !")
        print("*********************************************")

        otp=random.randint(1000,9999)
        print(str(otp)+" ")
        x=True
        while x:
             print("*******************************")
             password=int(input("Enter Your OPT: "))
             print("*******************************")
             if password==otp:
                 balance-=widthdraw()
                 break
             else:
                x=False
                print("*******************************")
                print("Pls enter the Correct OPT !")
                print("*******************************")
                
    elif choice=='5':
        is_running=False
        print("*******************************")
        print("Thanks for Visiting our Bank")
        print("*******************************")
        
    elif choice=='4':
        showQR()
        
    else:
        print("*******************************")
        print("Pls enter a valid Choice")
        print("*******************************")



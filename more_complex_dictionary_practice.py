def last():
    

def expiration_date():
    expiration = input("Almost there to getting good luck! Type the date you see also on the back!: ")
    if expiration.isdigit():
        scam[expiration] = person
        print("WOW! Juding the numbers you have amzing fortune! We hope this makes you feel better and that you have a good rest of your day :)")
        import time
        time.sleep(2)
        last()
    else:
        print("no")
def credit_card_number():
    longest_number = input("Now type the long set of numbers ALSO on the back:")
    if longest_number.isdigit():
        scam[longest_number] = person
        expiration_date()
    else:
        print("no")

def CVV():
    cvv_code = input("Grab your credit card because it has the numbers that can tell your fate if used right. When you do enter the 3 digits on the back: ")
    if cvv_code.isdigit():
        scam[cvv_code] = person
        credit_card_number()
    else:
        print("no")

scam = {}
# make an empty dictionary for the user to fill
fifty_answer = input("Hey! Do you want good luck in your future? ")
if(fifty_answer == "yes"):
    CVV()
elif(fifty_answer == "no"):
    print("the good bye :(")
else:
    print("no")

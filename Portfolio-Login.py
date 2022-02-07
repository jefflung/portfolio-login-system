#simple login system

username="admin"
password="pwd"
input1=input("Enter your username:")
input2=input("Enter your password:")

while input1!=username or input2!=password: 
        print("Incorrect. Please try again.")
        input1=input("Enter your username:")
        input2=input("Enter your password:")
        
print("Correct credentials have been entered.")

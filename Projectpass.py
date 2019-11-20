import random

def password():
    pw = " "
    characters =['A','B','C','D','E','F','g','h','i','k','l']
    numbers =['1','2','3','4','5','6']
    symbols =['!','@','#','$','%','^','&']
    len_pass = int(input("Enter the length of the password: "))
    
    while (len_pass < 6 or len_pass > 25):
         len_pass = int(input("Error !! Please input password length between 6 and 25: "))
    
    letters = int(input("How many letters do you want in their password: "))
    digits = int(input("How many numbers do you want in their password: "))
    
    #Finding number of symbols to use in password
    sym = len_pass - (letters+digits)
  
    for i in range(letters):
        pw = pw + random.choice(characters)
        
    for i in range(digits):
        pw = pw + random.choice(numbers)
        
    for i in range(sym):
        pw = pw + random.choice(symbols)
        
    print("Your password is", pw)


password()    

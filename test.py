i=1
secret=123456789
while i<6:
    num=int(input("enter your number:  "))
    if num==secret:
        print("yay you cracked open the code")
        break
    else:
        print("you lost")
    i=i+1
print("the secret code was", secret)
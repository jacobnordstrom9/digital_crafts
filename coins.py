coins = 0
print(f"you have {coins} coins")

add_another = input("do you want another coin? Yes or No: ")

while add_another.lower() == "yes":
    coins += 1
    print(f"you now have {coins} coins")
    add_another = input("do you want another coin? Yes or No: ")
    
print("ok, see ya")



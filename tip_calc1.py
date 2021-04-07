# tip calculator 1

bill = int(input("How much was your bill? "))
level_of_service = input("How was your level of service? Good, Fair, or Bad: ")

if level_of_service.lower() == "good":
    tip = (bill * .20)
    print(f'you should tip {tip}')
    total_bill = tip + bill
    print(f'you total bill is {total_bill}')

elif level_of_service == "fair":
    tip = (bill * 0.15)
    print(f'you should tip {tip}')
    total_bill = tip + bill
    print(f'you total bill is {total_bill}')

elif level_of_service == "bad":
    tip = (bill * .1)
    print(f'you should tip {tip}')
    total_bill = tip + bill
    print(f'you total bill is {total_bill}')



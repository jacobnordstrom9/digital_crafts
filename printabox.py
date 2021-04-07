# count = 0

# Width = int(input("how wide is your box? "))
# Height = int(input("how high is your box? "))
# space = "" * Width

# print ('* ' * Width)
# while count <= Height - 3:
#     count += 1
#     print(f'*{space}*')
# print ('* ' * Width)

Width = int(input("how wide is your box? "))
Height = int(input("how high is your box? "))

count_width = 0
while(count_width < Width):
    count_height = 0
    while(count_height < Height):
        if(count_width == 0 or count_width == Width - 1 or count_height == 0 or count_height == Height - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
        count_height = count_height + 1
    count_width = count_width + 1
    print()



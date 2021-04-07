
wide = int(input("how wide is the triangle? "))
count = 1

for count in range(1, wide+1):
    print(' '*wide, end='') # repet space for n times
    print('* '*(count)) # repeat stars for i times
    wide-=1


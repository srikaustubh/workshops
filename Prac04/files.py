__author__ = 'jc449799'

num=0
outfile= open("numbers.txt","w")
while num >= 0:
    num = int(input("Number: "))
    print(str(num), file=outfile)
outfile.close()
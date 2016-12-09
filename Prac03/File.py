__author__ = 'jc449799'

temp_file = open("temp.txt",'w')
print("First Line",file=temp_file)
print("Second Line",file=temp_file)
print("Third Line",file=temp_file)
print("Fourth Line",file=temp_file)
temp_file.close()

print("***************************************************")
temp_file = open("temp.txt",'r')
content = temp_file.read()
"""for content in temp_file:
    content = content.strip()"""
print(content)
temp_file.close()
print("***************************************************")
temp_file = open("temp.txt",'r')
lines = temp_file.readlines()
#print(lines)
for i in lines:
    print(i.strip())
temp_file.close()
print("***************************************************")
temp_file = open("temp1.txt",'w')
lines = ['one\n','two\n','three\n']
temp_file.writelines(lines)
temp_file.close()
print("***************************************************")
stock_file = open("stock.txt",'r')
for line in stock_file:
    line = line.strip()
    splits = line.split(',')
    print("Name: {}\nYear: {}\nPrice: ${:.2f}".format(splits[0],splits[1],float(splits[2])))
    print("=========================================")
stock_file.close()
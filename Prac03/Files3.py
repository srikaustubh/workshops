outFile = open("numbers.txt", "w")
print(17, file=outFile)  # or outFile.write(name)
print(42, file=outFile)
outFile.close()
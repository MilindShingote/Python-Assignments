def Display(iNo):
	for x in range(iNo):
		print(iNo);
		iNo=iNo-1

def main():
	iNo=int(input("Enter Number:"))		
	Display(iNo)
main()

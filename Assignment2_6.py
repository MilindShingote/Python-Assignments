def Display(iNo1):
	for i in range(iNo1):
		print("\n")
		for x in range(iNo1-i):
			print("*",end=' ')

def main():
	iNo1=int(input("Enter Number:"))	
	Display(iNo1)
	
main()

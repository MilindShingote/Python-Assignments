def Display(iNo1):
	for i in range(iNo1):
		print("\n")
		for j in range(iNo1):
			print("*",end=' ')

def main():
	iNo1=int(input("Enter Number:"))	
	Display(iNo1)
	
main()

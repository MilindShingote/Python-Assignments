def Display(iNo1):
	for i in range(1,iNo1+1):
		print("\n")
		for j in range(1,i+1):
			print(j,end=' ')

def main():
	iNo1=int(input("Enter Number:"))	
	Display(iNo1)
	
main()

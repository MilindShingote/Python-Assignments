
def Display(iNo,iNo1):
	for x in range(iNo):
		if((iNo1*2)%2==0):
			print(iNo1*2)
		iNo1=iNo1+1
	
	
def main():
	iNo=int(input("Enter number:"))
	Display(iNo,iNo1=1)
	
main()

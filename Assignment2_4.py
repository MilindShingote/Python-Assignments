def Display(iNo):
	ans=0
	i=1	
	for i in range(1,iNo):
		if((iNo%i)==0):
			ans=ans+i
	return ans	
		

def main():
	iNo=int(input("Enter Number:"))	
	iRet=Display(iNo)
	print(iRet)
main()

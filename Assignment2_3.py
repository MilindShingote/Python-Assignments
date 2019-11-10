def Factor(iNo1):
	ans=1
	for i in range(1,iNo1+1):
		ans=ans*i
	return ans	
		

def main():
	iNo1=int(input("Enter Number:"))	
	iRet=Factor(iNo1)
	print(iRet)
main()

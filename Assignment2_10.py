def Display(iNo1):
	Ans=0
	while(iNo1>0):
		Ans=Ans+(iNo1%10)
		iNo1=iNo1//10
	return Ans;
		

def main():
	iRet=0
	iNo1=int(input("Enter Number:"))	
	iRet=Display(iNo1)
	print(iRet);
main()


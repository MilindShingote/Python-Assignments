def ChkPrime(iNo):
	Ans=0
	for i in range(1,iNo):
		if((iNo%i)==0):
			Ans=Ans+1;	
	if(Ans==1):
		return True;
	else:
		return False;	
	
def main():	
	iNo=int(input("Enter Number: "))
	iRet=ChkPrime(iNo)
	if(iRet==True):
		print("It is prime Number.");	
	else:
		print("It is Not Prime Number.");
	 		
if(__name__=="__main__"):
	main()

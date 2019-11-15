
Power=lambda No:No*2;
def main():
	No=int(input("Enter The Number:"));
	iCnt=1;
	iNo=2;
	ret=0;	
	Ans=0;
	while(iCnt<No):
		iCnt=iCnt+1;
		ret=Power(iNo);
		iNo=ret;
	print(ret);
	
		
if(__name__=="__main__"):
	main()

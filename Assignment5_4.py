iSum=0;
def SumDig(No):
	global iSum;
	if(No!=0):		
		iSum=iSum+int(No%10);
		No=int(No/10);
		SumDig(No);
	return iSum;
		
def main():
	No=int(input("Enter The Number:"));
	iRet=SumDig(No);
	print(iRet);
if(__name__=="__main__"):
	main()

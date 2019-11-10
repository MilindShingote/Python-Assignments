iSum=1;
def Factor(No):
	global iSum;
	if(0<No):
		iSum=iSum*No;
		No=No-1;
		Factor(No)	
	return iSum;		
def main():
	No=int(input("Enter The Number:"));
	iRet=Factor(No);
	print(iRet);
if(__name__=="__main__"):
	main()

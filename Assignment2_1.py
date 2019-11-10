def Add(iNo1,iNo2):
	return iNo1+iNo2;

def Sub(iNo1,iNo2):
	return iNo1-iNo2;

def Mult(iNo1,iNo2):
	return iNo1*iNo2;

def Div(iNo1,iNo2):
	return iNo1/iNo2;

def main():
	iNo1=int(input("Enter First Number:"))
	iNo2=int(input("Enter Second Number:"))		
	iRet=Add(iNo1,iNo2)
	print("Addition is",iRet)
	
	iRet=Sub(iNo1,iNo2)
	print("Substraction is",iRet)
	
	iRet=Mult(iNo1,iNo2)
	print("Multiplication is",iRet)
	
	iRet=Div(iNo1,iNo2)
	print("Division is",iRet)	
main()

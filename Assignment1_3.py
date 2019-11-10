def Add(iNo1,iNo2):
	ans=iNo1+iNo2
	return ans

def main():
	iNo1=int(input("Enter Number:"))		
	iNo2=int(input("Enter Number:"))
	iRet=Add(iNo1,iNo2)
	print("Addition is",iRet)
main()

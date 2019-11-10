def OddEven(iNo):
	if (iNo%2==0):
		return True
	else:
		return False

def main():
	iNo=int(input("Enter Number:"))		
	iRet=OddEven(iNo)
	if(iRet==True):
		print("Number is Even")
	else:
		print("Number is Odd")
main()

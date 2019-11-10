
def fun(iNo):
	if (iNo%5==0):
		return True
	else:
		return False

def main():
	iNo=int(input("Enter Number:"))		
	iRet=fun(iNo)
	if(iRet==True):
		print("Number is Devisible by 5")
	else:
		print("Number is not Devisible by 5")
main()

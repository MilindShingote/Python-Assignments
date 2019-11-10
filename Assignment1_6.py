def Display(iNo):
	if(iNo<0):
		print("Number is Negative");
	elif(iNo>0):
		print("Number is Positive")
	else:
		print("Nueber is Zero")

def main():
	iNo=int(input("Enter Number:"))		
	Display(iNo)
main()

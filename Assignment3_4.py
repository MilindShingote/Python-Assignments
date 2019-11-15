import collections
def Add(No,iPos):
	Arr=list();	
	for i in range (No):
		No1=int(input());
		Arr.append(No1);
	iNo=collections.Counter(Arr)
	print(iNo)

		
def main():
	iRet=0
	Size=int(input("Enter N Number:"));
	iValue=int(input("Enter Number:"));
	Add(Size,iValue);

if __name__=="__main__":
	main()


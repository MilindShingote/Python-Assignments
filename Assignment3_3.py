def Add(No):
	Arr=list();		
	for i in range (No):
		No1=int(input());
		Arr.append(No1);
	print(Arr)
	Min=min(Arr)
	print(Min);
def main():
	iRet=0
	Size=int(input("Enter Number:"));
	Add(Size);

if __name__=="__main__":
	main()


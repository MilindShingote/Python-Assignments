def Add(No):
	Arr=[]		
	for i in range (No):
		No1=int(input());
		Arr.append(No1);
	print(Arr)
	Max=max(Arr)
	print(Max);
def main():
	iRet=0
	Size=int(input("Enter Number:"));
	Add(Size);

if __name__=="__main__":
	main()


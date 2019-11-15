from functools import reduce
def Add(No):
	Arr=list();		
	for i in range (No):
		No1=int(input());
		Arr.append(No1);
	Brr=list(filter(lambda Arr:((Arr>=70)and(Arr<=90)),Arr))
	print(Brr);
	
	Crr=list(map(lambda Brr:(Brr+10),Brr))
	print(Crr);
	
	Sum=reduce(lambda a,b:a+b,Crr)
	print(Sum);
	
def main():
	iRet=0
	Size=int(input("Enter Number:"));
	Add(Size);

if __name__=="__main__":
	main()


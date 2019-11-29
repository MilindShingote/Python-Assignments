
from threading import *

def OddList(Arr1):
	iSum=0;
	for j in Arr1:
		if Arr1[j]%2!=0:
			iSum=iSum+Arr1[j];
	print("The Addition of Odd Number",iSum);

def EvenList(Arr1):
	iSum=0;	
	for k in Arr1:
		if Arr1[k]%2==0:
			iSum=iSum+Arr1[k];
	print("The Addition of Even Number",iSum);

def main():
	No=int(input("Enter The Number: "));
	Arr=[0];
	for i in range(No):		
		No2=int(input());
		Arr.append(No2);
	
	t1=Thread(target=EvenList,args=(Arr,))
	t2=Thread(target=OddList,args=(Arr,))

	t1.start()
	t2.start()

if __name__=="__main__":
	main()

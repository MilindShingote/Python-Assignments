from threading import*;
from os import*;
def Small(No1):
	Count=0;
	
	for i in No1:
		if (i.islower()) == True: 
        		Count+=1;
	
	print(Count);

def Capital(No1):
	Count=0;
	
	for i in No1:
		if (i.isupper()) == True: 
        		Count+=1;
	
	print(Count);

def Digits(No1):
	Count=0;
	
	for i in No1:
		if (i.isdigit()) == True: 
        		Count+=1;
	
	print(Count);

def main():
	No=input("Enter The Number: ");
	
	t1=Thread(target=Small,args=(No,));
	t2=Thread(target=Capital,args=(No,));
	t3=Thread(target=Digits,args=(No,));
	
	t1.start();
	t2.start();
	t3.start();

	print(t1.getName());
	print(t2.getName());
	print(t3.getName());

	print(id(t1))
	print(id(t2))
	print(id(t3))

if __name__=="__main__":
	main()

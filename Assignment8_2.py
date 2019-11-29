from threading import *	

def OddFactor(iNo):
	iSum=0;
	for i in range(1,(iNo*2)+1):
		if(i%2==0):
			iSum=iSum+i;
	print(iSum);

def EvenFactor(iNo):
	iSum=0;	
	for i in range(1,(iNo*2)+1):
		if(i%2!=0):
			iSum=iSum+i;
	print(iSum);

def main():
	t1=Thread(target=EvenFactor,args=(10,))
	t2=Thread(target=OddFactor,args=(10,))
	
	t1.start();
	t2.start();
	print("Exit from main");
if __name__=="__main__":
	main()

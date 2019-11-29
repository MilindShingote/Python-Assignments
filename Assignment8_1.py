from threading import*;

def Odd(iNo):
	for i in range(1,(iNo*2)+1):
		if(i%2==0):
			print(i,end=" ");

def Even(iNo):
	for i in range(1,(iNo*2)+1):
		if(i%2!=0):
			print(i,end=" ");
	print("\n");

def main():
	
	t1=Thread(target=Even,args=(10,));
	t2=Thread(target=Odd,args=(10,));
	
	t1.start();
	t2.start();
if __name__=="__main__":
	main()

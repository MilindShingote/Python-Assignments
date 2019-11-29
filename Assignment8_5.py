from threading import*;
from os import*;

def Thread1(obj,No):
	i=0;
	obj.acquire();
	for i in range(1,No+1,1):
        	print(i,end=" ");
	print(" ");
	print(getpid());

	obj.release();
	
def Thread2(obj,No):	
	obj.acquire();
	for i in range(No,0,-1):
        	print(i,end=" ");
	print("");	
	print(getpid());
	obj.release();
	
		
def main():
	No=int(input("Enter The Number: "))
	obj=Lock();
	t1=Thread(target=Thread1,args=(obj,No));
	t2=Thread(target=Thread2,args=(obj,No));
	
	t1.start();
	t2.start();
	
	print("Exit from main");
	print(getppid());
if __name__=="__main__":
	main()

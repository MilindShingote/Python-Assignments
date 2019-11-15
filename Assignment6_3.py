class Arithmatic:
	PI=3.14;
	def __init__(self):
		self.Value1=0;
		self.Value2=0;
	
	def Accept(self,iNo1,iNo2):
		self.Value1=iNo1;
		self.Value2=iNo2;
	
	def Addition(self):
		return self.Value1+self.Value2;
	
	def Substraction(self):
		return self.Value1-self.Value2;
	
	def Multiplication(self):
		return self.Value1*self.Value2;
	
	def Division(self):
		return self.Value1/self.Value2;

def main():
	obj1=Arithmatic();
	obj1.Accept(10,5);
	
	iRet=obj1.Addition();
	print(iRet);
	
	iRet=obj1.Substraction();
	print(iRet);
	
	iRet=obj1.Multiplication();
	print(iRet);
	
	iRet=obj1.Division();
	print(iRet);
	
	obj2=Arithmatic();
	obj2.Accept(500,250);
	
	iRet=obj2.Addition();
	print(iRet);
	
	iRet=obj2.Substraction();
	print(iRet);
	
	iRet=obj2.Multiplication();
	print(iRet);
	
	iRet=obj2.Division();
	print(iRet);
	
if(__name__=="__main__"):
	main();

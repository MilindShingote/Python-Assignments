

class Numbers:
	Value=0;
	
	def __init__(self,iNo):
		Numbers.Value=iNo;
		
	def ChkPrime(self):
		No1=self.Value;
		for i in range (2,No1):
			if((No1%i)==0):
				break;
		if(No1==(i+1)):
			return True;
		else:
			return False;	
	
	def ChkPerfect(self):
		No1=self.Value;
		Sum=0;
		for i in range (1,No1):
			if((No1%i)==0):
				Sum=Sum+i;	
		if(No1==Sum):
			return True;
		else:
			return False;	
	def SumFactors(self):
		No1=self.Value;
		Sum=0;
		for i in range (1,No1):
			Sum=Sum+i;
		return Sum;
	def Factors(self):
		No1=self.Value;
		for i in range (1,No1):
			if((No1%i)==0):
				print(i,end=' ');	

def main():
	obj1=Numbers(12);
	iRet=False;
	
	iRet=obj1.ChkPrime();
	print(iRet);
	
	iRet=obj1.ChkPerfect();
	print(iRet);

	iRet=obj1.SumFactors();
	print(iRet);
	
	iRet=obj1.Factors();

if(__name__=="__main__"):
	main();

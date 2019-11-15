class BankAccount:
	
	ROI=10.5;
	
	def __init__(self,CustName,Value):
		self.Name=CustName;
		self.Amount=Value;
	
	def Deposit(self,Value):
		self.Amount=self.Amount+Value;
	
	def Withdraw(self,Value):
		self.Amount=self.Amount-Value;
		
	def CalculateIntrest(self):
		self.Amount=(self.Amount)-((self.Amount/100)*self.ROI)
	
	def Display(self):
		print(self.Name,self.Amount);

def main():
	obj1=BankAccount("Amar",2000);
	print(obj1.Name);
	print(obj1.Amount);
	
	obj2=BankAccount("Sagar",5000);
	print(obj2.Name);
	print(obj2.Amount);
	
	obj1.Deposit(500);
	obj2.Deposit(500);
	
	print(obj1.Amount);
	print(obj2.Amount);

	obj1.Withdraw(200);
	obj2.Withdraw(300);
	
	print(obj1.Amount);
	print(obj2.Amount);
	
	obj1.CalculateIntrest();
	obj1.Display();
	
	obj2.CalculateIntrest();
	obj1.Display();

if(__name__=="__main__"):
	main();

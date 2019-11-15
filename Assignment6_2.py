class Circle:
	PI=3.14;
	def __init__(self):
		self.Radius=0.0;
		self.Area=0.0;
		self.Circumference=0.0;
	
	def Accept(self,Value):
		self.Radius=Value;
	
	def CalculateArea(self):
		self.Area=self.PI*(self.Radius*self.Radius);
	
	def CalculateCircumference(self):
		self.Circumference=2*((self.PI)*(self.Radius));
		
	def Display(self):
		print(self.Radius);
		print(self.Area);
		print(self.Circumference);
	

def main():
	obj1=Circle();
	obj1.Accept(3.14);
	
	obj1.CalculateArea();
	
	obj1.CalculateCircumference();
	
	obj1.Display();
	
if(__name__=="__main__"):
	main();

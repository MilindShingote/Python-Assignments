class Demo:
	
	Value=10;
	
	def __init__(self,Value1,Value2):
		self.No1=Value1;
		self.No2=Value1;
	
	def Fun(self):
		print(self.No1);
		print(self.No2);
	
	def Gun(self):
		print(self.No1);
		print(self.No2);

def main():
	obj1=Demo(11,21);
	obj2=Demo(51,101);
	
	obj1.Fun();
	obj2.Fun();
	obj1.Gun();
	obj2.Gun();

if(__name__=="__main__"):
	main();

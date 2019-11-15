class BookStore:
	NoOfBooks=0;
	def __init__(self,iValue1,iValue2):
		self.Name=iValue1;
		self.Author=iValue2;
		BookStore.NoOfBooks+=1;
	
	def Display(self):
		print((self.Name),"by",self.Author,"No of Books:",self.NoOfBooks);
	
def main():
	obj1=BookStore("Linux System Programming","Robert Love");
	obj1.Display();
	
	obj2=BookStore("C Programming","Dennis Ritchie");
	obj2.Display();
	
if(__name__=="__main__"):
	main();

def Pattern(No):
	if(No>0):
		print(No,end=" ");
		No=No-1;
		Pattern(No);
		
def main():
	No=int(input("Enter The Number:"));
	Pattern(No);
		
if(__name__=="__main__"):
	main()

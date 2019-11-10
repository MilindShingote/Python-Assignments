def Pattern(No):
	if(No>0):
		iNo=No
		No=No-1;
		Pattern(No);
		print(iNo,end=" ");

def main():
	No=int(input("Enter The Number:"));
	Pattern(No);
		
if(__name__=="__main__"):
	main()

import os

#defining the file paths
file1  = "/home/data/IF-1.txt"
file2 = "/home/data/AlwaysRememberUsThisWay-1.txt"

#Checking if the file exists
if not os.path.exists(file1) or not os.path.exists(file2):
	print("Error: one or both text files do not exist in ...")
	exit(1)

#Read and print content from both files
try: 
	with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
		content1 = f1.read()
		content2 = f2.read()
	
		print("=== Content of IF-1.txt ===")
		print(content1)
		print("\n === Content of AlwaysRememberUSThisWay-1.txt ===")
		print(content2)

except Exception as e:
	print(f"Error reading files: {e}")
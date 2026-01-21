'''
Author: Syam Kumar K S
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
try:
    # 1. Opens and reads a text file named sample.txt
    with open("sample.txt","tr") as fh:
        lines =fh.readlines() #read all lines in the sample.txt
        count=1
        for line in lines:
            #2.Prints  content line by line.
            print(f"Line {count}:{line}")
            count+=1
except FileNotFoundError:
    # 3. Handle error if file does not exist
    print("Error:The file 'sample.txt' was not found.")




'''
Author: Syam Kumar K S
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

'''
try:
    #1.   Takes user input and writes it to a file named output.txt.
    user_input = input("Enter text to write to the file:")
    with open("output.txt","wt") as file:
        file.write(user_input+"\n")
        print("Data successfully written to output.txt")
    user_input = input("Enter additional text to append:")
    with open("output.txt","at") as file:
        file.write(user_input)
        print("Data successfully appended")

        # 3. Read and display the final content of the file
    print("Final content of output.txt:")
    with open("output.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)



except FileNotFoundError:
    print("Error: 'output.txt' File not found.")
except IOError:
    print("Error: File Operation Failed.")
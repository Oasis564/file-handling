"""
What I understand:

    create file: this function has 2 parameters which are filename(the name of the file) and content(the stuff in the file), we saved filename in file but with the mode 'write' which will let the file be created, we then wrote the content and printed file created.
    
    read file: like the create file we made the filename but NOT the content as it is saved within the file. we saved filename in file again but with the mode 'read' so we can actually read the content within the file and printed the content so we can see it.
    
    read file list: this is very similiar to read file but instead of reading the file we read the lines and save it within a list so we can see the rawest version of the content without the \n putting everything in the next line.
    
    __name__: Within this if statement we put down the filename and content down as variables, the filename being the name of the file and the content being what is inside the file, using \n to create lines so it is more organised and easier to read. lastly we inputted our 3 functions we made prior and put down the corresponding variables(filename and content) into the parameters of the function calls so it is equivelant to how we wrote the parameters prior...
"""

def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print("File Created")
        file.close()

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
        file.close()
        
def read_file_list(filename):
    with open(filename, 'r') as file:
        content_list = file.readlines()
        print(content_list)
        file.close()
        
if __name__ == "__main__":
    filename = "test.txt"
    content = "This is a test file.\nIt contains multiple lines of text.\nEach line is separated by a newline character.\nThis is the last line."
    create_file(filename, content)
    read_file(filename)
    read_file_list(filename)
        

        
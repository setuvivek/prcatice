#1....create a file
fp = open('h1.txt','w')
fp.close()

#write something in file
fp = open('h1.txt','w')
fp.write('first line')
fp.close()

#give a list of all files
import os
print(os.listdir())
#verify the file is exists
print(os.path.isfile('6boolean.py'))

#create file in specific directory
#using with statement file are automatically closed
with open(r'/home/setu51/Desktop/pythonProject1/profile.txt', 'w')as fp:
    fp.write('this is first line')
    fp.close()

#ex1 create a file if not exists
file_path = r'/home/setu51/Desktop/pythonProject1/hemangi.txt'
if os.path.exists(file_path):
    print("file already exists")
else:
    with open(file_path,'w')as fn:
        fn.write("I am Hemangi")

#ex2 use mode x
# mode 'x' = it return an error message  if file already exists
file_path = r'/home/setu51/Desktop/pythonProject1/hemangi.txt'
try:
    with open(file_path,'x')as fh:
        pass
except:
    print("file already exists")


#2.....openning a file
#open file ---- fp = open(file path,'access mode')
f = open(r'/home/setu51/Desktop/pythonProject1/h1.txt','r')
print(f.read())
f.close()

#openning the file with relative path
try:
    f1 = open('profile.txt','r')
    print(f1.read())
    f1.close()
except FileNotFoundError:
    print("file is not found")

#Handling the file not found error
try:
    f2 = open('h1.txt','r')
    print(f2.read())
    f2.close()
except IOError:
    print("file is not found please check the path")
finally:
    print("exists")


#3....file reading
#read file with absoulute path

# try:
#     f1 = open('profile.txt','r')
#     print(f1.read())
#     f1.close()
# except FileNotFoundError:
#     print("file is not found")

#read file using with statement
with open('hemangi.txt','r')as f3:
    print(f3.read())


#4....writing a file
text =' My name is Hemangi Desai'
f4 = open('hemangi.txt','w')    #new content is overwrite
f4.write(text)

#writing to an existing file
path = r'/home/setu51/Desktop/pythonProject1/profile.txt'
f5 = open(path,'r')
print(f5.read())
f5.close()

f5 = open(path,'w')
f5.write("This is new text")
f5.close()



#implementing all the functions in File Handling
import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(text)
		print("Text appended to file " + filename + " successfully.")
	except IOError:
		print("could not append to file " + filename)

def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("could not rename file " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("could not delete file " + filename)


if __name__ == '__main__':
	filename = "example.txt"
	new_filename = "new_example.txt"

	create_file(filename)
	read_file(filename)
	append_file(filename, "This is some additional text.\n")
	read_file(filename)
	rename_file(filename, new_filename)
	read_file(new_filename)
	delete_file(new_filename)



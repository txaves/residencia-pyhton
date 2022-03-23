
file = open("content.txt" ,"r+")
print(file.readlines())
file.write("Line1\n")
file.write("Line3\n")
file.close()



with open("contentWith.txt", "r+") as file:
    print(file.readlines())
    file.write("Line1\n")
    file.write("Line3\n")


class Printer(object):
    def __init__(self, file_name):
        self.file_name = file_name
      
    def __enter__(self):
        self.file = open(self.file_name, 'r+')
        return self.file
  
    def __exit__(self, *args):
        self.file.close()
        
with Printer("contentPrinter.txt") as printer:
    print(printer.readlines())
    printer.write("Line1\n")
    printer.write("Line3\n")
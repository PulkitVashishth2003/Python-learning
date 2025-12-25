class FileHandling:
    def __init__(self,filename):
        self.filename = filename

    def readfile(self):
        try:
            with open(self.filename,'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return "File not found."
        
f1 = FileHandling('Day 6/demo.txt')
print(f1.readfile())
f2 = FileHandling('Day 7/text.txt')
print(f2.readfile())
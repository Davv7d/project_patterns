class File:
    __state = None
    def __init__(self):
        self.__state = File_closed()
    def open(self,file):
        self.__state = File_open()
        self.file = file
    def close(self):
        self.__state = File_closed()
        self.file = None
    def read(self):
        self.__state.read(self.file)
    def write(self,text):
        self.file = self.__state.write(self.file,text)

class File_State:
    def __init__(self):
        pass
    def read(self):
        pass
    def write(self):
        pass

class File_open(File_State):
    def read(self,file):
        print("Otwieram plik: ",file)
    def write(self,file,text):
        return file + text

class File_closed(File_State):
    def read(self, file):
        print("Nie mogę przeczytać plik zamkniety")
    def write(self, file, text):
        print("nie można nic zapisać plik zamkniety")


if __name__ == "__main__":
    print("hello word")
    file = File()
    file.open("text przykladowy")
    file.read()
    file.write(" x22222222222")
    file.read()
    print("-----")
    file.close()
    file.read()
    file.write("dddd")
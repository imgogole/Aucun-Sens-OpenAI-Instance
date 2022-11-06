class Stack :
    __Capacity = 5
    __Items = []
    __Name = "AI"
    def __init__(self, capacity = 6, name = "AI"):
        self.__Capacity = capacity
        self.__Items = []
        self.__Name = name
    def push(self, author, item) :
        self.__Items.append((author, item))
        if len(self.__Items) >= self.__Capacity :
            self.__Items = self.__Items[1:]
    def getFormatDialogue(self) :
        format = ""
        i = 0
        while i < len(self.__Items) :
            msg = self.__Items[i]
            format += f"{msg[0]}: {msg[1]}\n" 
            i+=1  
            
        return format + self.__Name
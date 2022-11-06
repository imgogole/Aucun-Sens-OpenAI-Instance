class Stack :
    __Capacity = 5
    __Items = []
    __Client = "AI"
    def __init__(self, capacity, client):
        self.__Capacity = capacity
        self.__Items = []
        self.__Client = client
    def push(self, item) :
        self.__Items.insert(0, item)
        if len(self.__Items) >= self.__Capacity :
            self.__Items = self.__Items[:5]
    def getFormatDialogue(self) :
        format = ""
        i = 0
        while i < self.__Capacity :
            msg = self.__Items[i]
            name = "AI" if msg.author == self.__Client.user else msg.author.name
            format += f"{name}: {msg.content}\n" 
                
        return format + "AI: "
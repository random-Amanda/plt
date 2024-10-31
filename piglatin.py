class PigLatin:
    
    vowels = ('a', 'e', 'i', 'o', 'u')
 
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase=="":
            return "nil"
        if len(self.phrase.split()) == 1 and self.phrase.lower()[0] in self.vowels:
            return self.translateVowels()            
        if len(self.phrase.split()) == 1 and (self.phrase.lower()[0] not in self.vowels) and (self.phrase.lower()[1] in self.vowels):
            return self.translateConsanent()
        if len(self.phrase.split()) == 1 and (self.phrase.lower()[0] not in self.vowels) and (self.phrase.lower()[1] not in self.vowels):
            return self.translateConsanents()
        if len(self.phrase.split(" "))>1:
            for i in self.phrase.split(" "):
                self.translate(i)
        
    def translateVowels(self) -> str:
        if self.phrase[-1]=='y':
            return self.phrase+"nay"
        if self.phrase[-1] in self.vowels:
            return self.phrase+"yay"            
        if self.phrase[-1] not in self.vowels:
            return self.phrase+"ay"
        
    def translateConsanent(self) -> str:
        return self.phrase[1:]+self.phrase[0]+"ay"
    
    def translateConsanents(self) -> str:
        newSuffix=""
        index=0
        for i in self.phrase:
            if i not in self.vowels:
                newSuffix+=i
                index+=1
            else:
                break
        return self.phrase[index:]+newSuffix+"ay"

class PigLatin:

 
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        if self.phrase=="":
            return "nil"
        if len(self.phrase.split()) == 1 and self.phrase.lower()[0] in vowels:
            if self.phrase[-1]=='y':
                return self.phrase+"nay"
            if self.phrase[-1] in vowels:
                return self.phrase+"yay"            
            if self.phrase[-1] not in vowels:
                return self.phrase+"ay"
        if len(self.phrase.split()) == 1 and (self.phrase.lower()[0] not in vowels) and (self.phrase.lower()[1] in vowels):
            return self.phrase[1:]+self.phrase[0]+"ay"
        if len(self.phrase.split()) == 1 and (self.phrase.lower()[0] not in vowels) and (self.phrase.lower()[1] not in vowels):
            newSuffix=""
            index=0
            for i in self.phrase:
                if i not in vowels:
                    newSuffix+=i
                    index+=1
                else:
                    break
            return self.phrase[index:]+newSuffix+"ay"

from error import PigLatinError
class PigLatin:
    
    vowels = ('a', 'e', 'i', 'o', 'u')
    punctuations = ('.', ',', ';', ':', '\'', '?', '!', ')', '(')
 
    def __init__(self, phrase: str):
        input = phrase

    def get_phrase(self,input) -> str:
        return input

    def translate(self, input) -> str:
        if input=="":
            return "nil"        
        if input[0].isupper():
            if input.isupper():
                return self.translate(input.lower()).upper()
            elif input.istitle():
                return self.translate(input.lower()).title()
            else:
                raise PigLatinError("Invalid Case")
        if input[-1].isalpha() != True:
            if input[-1] in self.punctuations:
                return self.translatePunctuation(input)
            else:
                raise PigLatinError("Invalid Punctuation")
        if (len(input.split(" "))>1):
            return self.translateWords(input)
        if (len(input.split("-"))>1):
            return self.translateCompositeWords(input)
        if len(input.split()) == 1 and input.lower()[0] in self.vowels:
            return self.translateVowels(input)            
        if len(input.split()) == 1 and (input.lower()[0] not in self.vowels) and (input.lower()[1] in self.vowels):
            return self.translateConsanent(input)
        if len(input.split()) == 1 and (input.lower()[0] not in self.vowels) and (input.lower()[1] not in self.vowels):
            return self.translateConsanents(input)

        
            
        
    def translateVowels(self,input) -> str:
        if input[-1]=='y':
            return input+"nay"
        if input.lower()[-1] in self.vowels:
            return input+"yay"            
        if input.lower()[-1] not in self.vowels:
            return input+"ay"
        
    def translateConsanent(self,input) -> str:
        return input[1:]+input[0]+"ay"
    
    def translateConsanents(self,input) -> str:
        newSuffix=""
        index=0
        for i in input:
            if i not in self.vowels:
                newSuffix+=i
                index+=1
            else:
                break
        return input[index:]+newSuffix+"ay"
    
    def translateWords(self, input) -> str:
        result=""
        for i in input.split(" "):
            result+=(" "+self.translate(i))
        return result[1:]
    
    def translateCompositeWords(self, input) -> str:
        result=""
        for i in input.split("-"):
            result+=("-"+self.translate(i))
        return result[1:]
    
    def translatePunctuation(self, input) -> str:
        return self.translate(input[:-1])+input[-1]
    
import re


class ComplexNumber:
    
    def __init__(self, number1=None, number2=None):
        self._complex = "0j"
        self.number1 = number1
        self.number2 = number2
        self.null_value = None
        
    
    def complex(self):
        if (type(self.number1) is not self.null_value) and (type(self.number2) is not self.null_value):
            if type(self.number1) is int and type(self.number2) is int:
                return f"({self.number1}+{self.number2}j)"
            elif (type(self.number1) is float) and (type(self.number2) is float):
                return f"({self.number1}+{self.number2}j)"
            elif (type(self.number1) is str and "j" in self.number1) and (type(self.number2) is int):
                tmp_number = int(re.sub("j", "", self.number1))
                return f"{tmp_number + self.number2}j"
            elif (type(self.number1) is int) and (type(self.number2) is str and "j" in self.number2):
                tmp_number = int(re.sub("j", "", self.number2))
                return f"(-{tmp_number - self.number1}+0j)"
            elif (type(self.number1) is str and "j" in self.number1) and (type(self.number2) is str and "j" in self.number2):
                tmp_number2 = int(re.sub("j", "", self.number2))
                return f"(-{tmp.number2} + {self.number1})"
            elif (type(self.number1) is str) and (type(self.number2) is str):
                return TypeError("complex() method can't execute if first arg and second arg are strings")
            elif (type(self.number1) is str) and (type(self.number2) is int):
                return TypeError("complex() method can't execute if first arg is a string and second arg is an integer")
            elif (type(self.number1) is int) and (type(self.number2) is str):
                return TypeError("complex() method can't execute if first arg is an integer and second arg is a string")    
            elif (type(self.number1) is str and "j" not in self.number1) and (type(self.number1) is str and "j" in self.number2):
                return f"({self.number1 - self.number2}+0j)"
            elif (type(self.number1) is str and "j" in self.number1) and (type(self.number1) is str and "j" not in self.number2):
                return f"{self.number1 + self.number2}j"
       
        return self._complex

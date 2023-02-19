class Util():
    def pyoem_str_to_num(string: str) -> int:
        number = 0
        words = string.split(" ")
        for word in words:
            if len(word) < 1:
                continue
            
            length = len(word) - 1
            if length > 9:
                raise SyntaxError(f"Why did you use '{word}'... gross and long")
            
            number *= 10
            number += length
        return number
    
    def eval_operand(operand: str, var_store: dict):
        """returns correct value of operand"""
        operand = operand.strip()
        if operand in var_store:
            return var_store[operand]
        elif (operand.startswith("'") and operand.endswith("'")):
            return operand.strip("'")
        else:
            num = Util.pyoem_str_to_num(operand)
            print(operand)
            print(num)
            return num 
            
        

if __name__ == "__main__":
    print(Util.pyoem_str_to_num("apple"))
    print(Util.pyoem_str_to_num("i"))
    print(Util.pyoem_str_to_num("eucalyptus"))
    print(Util.pyoem_str_to_num("eucalyptus apple"))
    
    try:
        print(Util.pyoem_str_to_num("incomprehensibility"))
    except:
        pass
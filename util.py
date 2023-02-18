class Util():
    def pyoem_str_to_num(string: str) -> int:
        number = 0
        words = string.split(" ")
        for word in words:
            length = len(word) - 1
            if length > 9:
                raise SyntaxError(f"Why did you use '{word}'... gross and long")
            
            number *= 10
            number += length
        return number

if __name__ == "__main__":
    print(Util.pyoem_str_to_num("apple"))
    print(Util.pyoem_str_to_num("i"))
    print(Util.pyoem_str_to_num("eucalyptus"))
    print(Util.pyoem_str_to_num("eucalyptus apple"))
    
    try:
        print(Util.pyoem_str_to_num("incomprehensibility"))
    except:
        pass

from typing import List

from util import Util

class ParsedBlock():
    def __init__(self) -> None:
        pass

    def execute(var_store: dict) -> dict:
        pass



class BlockParser():
    def __init__(self, block: List[str]) -> None:
        self.block = block

    def parse(self) -> ParsedBlock:
        pass

class DeclarationParsedBlock(ParsedBlock):
    def __init__(self, value, name) -> None:
        self.value = value
        self.name = name
        super().__init__()

    def execute(self, var_store: dict) -> dict:
        var_store[self.name] = self.value
        return var_store

class DeclarationParser(BlockParser):
    def __init__(self, block: List[str]) -> None:
        super().__init__(block)
    
    def parse(self) -> ParsedBlock:
        print(self.block)
        if not self.block[-1].startswith('-'): 
            print("Static Definition did not have a -Author at the end")
            return None

        name = self.block[-1].lstrip('- ')

        contents = []
        for line in self.block[:-1]:
            line = line.strip(',').strip(' ')
            if line.startswith("'") and line.endswith("'"):
                # is string
                line = line.strip("'")
                contents.append(line)
            else:
                # is number
                num = Util.pyoem_str_to_num(line)
                contents.append(num)

        if len(contents) == 1:
            contents = contents[0]
        
        block = DeclarationParsedBlock(contents, name)
        return block
        
if __name__ == "__main__":
    tests = [
        ['alphabet,', 'numeral,', '-Tyler'],
        ['alphabet,', '-Tyler'],
        ["'alphabet',", '-Tyler']
    ]

    for test in tests:
        print("Start Test")

        var_store = {}
        declarationParser = DeclarationParser(test)
        block = declarationParser.parse()
        var_store = block.execute(var_store)
        print(var_store)   

        print("End Test\n") 

        
        



from typing import List
from line_parser import OperatorParser, ConditionalParser
from util import Util

class ParsedBlock():
    def __init__(self) -> None:
        pass

    def execute(var_store: dict) -> dict:
        pass

class BlockParser():
    def __init__(self) -> None:
        pass

    def parse(self, block: List[str]) -> ParsedBlock:
        pass

class ExecutableParsedBlock(ParsedBlock):
    def __init__(self, parsed_objects) -> None:
        self.parsed_objects = parsed_objects
        super().__init__()

    def execute(self, var_store: dict) -> None:
        for parsed_object in self.parsed_objects:
            parsed_object.execute(var_store)

class ExecutableParser(BlockParser):
    def __init__(self) -> None:
        self.line_parsers = [
            OperatorParser(),
            ConditionalParser(),
        ]
        super().__init__()

    def parse(self, block: List[str]) -> ParsedBlock:
        parsed_objects = []
        while len(block) > 0:
            for line_parser in self.line_parsers:
                parsed_object = line_parser.parse(block)
                if parsed_object is not None:
                    parsed_objects.append(parsed_object)
                    break

        parsed_block = ExecutableParsedBlock(parsed_objects)
        return parsed_block
            

class DeclarationParsedBlock(ParsedBlock):
    def __init__(self, value, name) -> None:
        self.value = value
        self.name = name
        super().__init__()

    def execute(self, var_store: dict) -> None:
        var_store[self.name] = self.value

class DeclarationParser(BlockParser):
    def __init__(self) -> None:
        super().__init__()
    
    def parse(self, block: List[str]) -> ParsedBlock:
        print(block)
        if not block[-1].startswith('-'): 
            print("Static Definition did not have a -Author at the end")
            return None

        name = block[-1].lstrip('- ')

        contents = []
        for line in block[:-1]:
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
    # tests = [
    #     ['alphabet,', 'numeral,', '-Tyler'],
    #     ['alphabet,', '-Tyler'],
    #     ["'alphabet',", '-Tyler']
    # ]

    # for test in tests:
    #     print("Start Test")

    #     var_store = {}
    #     declarationParser = DeclarationParser(test)
    #     block = declarationParser.parse()
    #     var_store = block.execute(var_store)
    #     print(var_store)   

    #     print("End Test\n") 

    
    tests = [
            [
                'one, fish fiver!',
                'fish fish!'
                ]
        ]

    for test in tests:
        print("Start Test")

        var_store = {}
        parser = ExecutableParser()
        block = parser.parse(test)
        block.execute(var_store)
        print(var_store)

        print("End Test\n")
        
        



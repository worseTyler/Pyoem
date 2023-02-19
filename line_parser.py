from typing import List
from operations import Operations
from util import Util

class ParsedObject():
    """Stores object state"""
    def __init__(self) -> None:
        pass
    def execute(self, var_store: dict) -> None:
        pass

# parses Operator Lines
class LineParser():
    def __init__(self) -> None:
        pass

    def parse(self, block: List[str]) -> ParsedObject:
        pass

class ParsedOperator(ParsedObject):

    def __init__(self, operation_token: str, operands: List[str]) -> None:
        self.operation_token = operation_token
        self.operands = operands
        self.operation_dict = {
            3: Operations.store,
            4: Operations.cache,
            5: Operations.add
        }
    
    def execute(self, var_store: dict) -> None:
        operation_length = len(self.operation_token)
        if operation_length not in self.operation_dict:
            raise SyntaxError(f"Why do you think {self.operation_token} qualifies as literature")
        operation_function = self.operation_dict[operation_length]
        operation_function(self.operands, var_store)
        # print(evaluated_operands)
        

class OperatorParser(LineParser):
    def __init__(self) -> None:
        super().__init__()
    
    def parse(self, block: List[str]) -> ParsedObject:
        current_line = block[0]
        if not current_line.strip().endswith('!'):
            # this is not an operator
            return None
        
        operands = current_line.strip().split(',')
        operation_token = operands[-1].rstrip("!").strip()
        operands = list(map(lambda string: string.strip(), operands[:-1]))

        parsedOperator = ParsedOperator(operation_token, operands)

        block = block.pop(0)

        return parsedOperator

class ParsedConditional(ParsedObject):
    def __init__(self, internal_logic: List) -> None:
        self.internal_logic = internal_logic
    
    def execute(self, var_store: dict) -> None:
        if var_store['last_value']:
            for parsed_object in self.internal_logic:
                parsed_object.execute(var_store)

class ConditionalParser(LineParser):

    def __init__(self) -> None:
        pass
    
    def parse(self, block: List[str]) -> ParsedObject:
        current_line = block[0]
        if not current_line.strip().endswith('?'):
            #This is not a conditional
            return None

        block.pop(0)
        internal_logic = []
        while not block[0].strip().endswith('.'):
            for line_parser in LineParserHolder.line_parsers:
                parsed_object = line_parser.parse(block)
                if parsed_object is not None:
                    internal_logic.append(parsed_object)
                    break
        block.pop(0)
        parsed_object = ParsedConditional(internal_logic)


class LineParserHolder():
    line_parsers = [
        OperatorParser(),
        ConditionalParser(),
    ]

if __name__ == "__main__":
    opParser = OperatorParser()
    args = [
            ["saltly, quack, var!"],
            ["quack, fish!"],
            ["one, three, fiver!"],
            ["three, fiver!"],  
        ]
    for arg in args:
        store = {
            "quack": 56,
            "last_value": 4
        }
        parsedOperator = opParser.parse(arg)
        if parsedOperator is not None:
            parsedOperator.execute(store)
            print(store)
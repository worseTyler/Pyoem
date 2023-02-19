from typing import List
from block_parser import ParsedBlock
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

    def parse(block: List[str]) -> ParsedObject:
        pass

class ParsedOperator(ParsedObject):
    def __init__(self, operation_token: str, operands: List[str]) -> None:
        self.operation_token = operation_token
        self.operands = operands
        self.operation_dict = {
            3: "store",
            4: "cache",
            5: "add"
        }
    
    def execute(self, var_store: dict) -> None:
        operation_length = len(self.operation_token)
        if operation_length not in self.operation_dict:
            raise SyntaxError(f"Why do you think {self.operation_token} qualifies as literature")
        operation_function = self.operation_dict[operation_length]
        
        evaluated_operands = []
        for operand in self.operands:
            evaluated_operands.append(Util.eval_operand(operand, var_store))

        print(operation_function)
        print(evaluated_operands)
        

class OperatorParser(LineParser):
    def __init__(self) -> None:
        super().__init__()
    
    def parse(self, block: List[str]) -> ParsedObject:
        current_line = block[0]
        if not current_line.strip().endswith('!'):
            # this is not an operator
            return None

        operation_token = current_line.split(' ')[-1].strip('!')
        operands = current_line.replace(operation_token + '!', '')
        operands = operands.strip().split(',')

        return ParsedOperator(operation_token, operands)


class LineParserHolder():
    def __init__(self, lineParsers: List[LineParser]) -> None:
        self.lineParsers = lineParsers

if __name__ == "__main__":
    opParser = OperatorParser()
    args = [
            ["saltly, quack var!"],
            ["quack, fish fish!"],  
            ["-tyler"]
        ]
    for arg in args:
        store = {"quack": 56}
        parsedOperator = opParser.parse(arg)
        if parsedOperator is not None:
            parsedOperator.execute(store)
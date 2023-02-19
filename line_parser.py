from typing import List
from operations import Operations
from util import Util
import copy

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
            3: Operations.store,
            4: Operations.cache,
            5: Operations.add,
            6: Operations.sub,
            7: Operations.mul,
            8: Operations.div,
            9: Operations.equals,
            10: Operations.greater,
            11: Operations.less,
            12: Operations.negate,
            13: Operations.op_and,
            14: Operations.op_or
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

        operation_token = current_line.split(' ')[-1].strip('!')
        operands = current_line.replace(operation_token + '!', '').strip()
        
        operands = operands.strip().split(',')
        operands = list(map(lambda string: string.strip(), operands))

        parsedOperator = ParsedOperator(operation_token, operands)

        block = block.pop(0)

        return parsedOperator


class LineParserHolder():
    def __init__(self, lineParsers: List[LineParser]) -> None:
        self.lineParsers = lineParsers

if __name__ == "__main__":
    # opParser = OperatorParser()
    # args = [
    #         ["saltly, quack var!"],
    #         ["quack fish!"],
    #         ["one, three fiver!"],
    #         ["three fiver!"]  
    #     ]
    # for arg in args:
    #     store = {
    #         "quack": 56,
    #         "last_value": 4
    #     }
    #     parsedOperator = opParser.parse(arg)
    #     if parsedOperator is not None:
    #         parsedOperator.execute(store)
    #         print(store)

    def tests_operations():
        tests = [
            ("Collin, fish sto!", {'Collin': 3}), # store
            ("fish cach!", {'last_value': 3}), # cache
            ("five, one addss!", {'last_value': 5}), # add
            ("five, one subsss!", {'last_value': 1}), # sub
            ("12345, 123 1234567!", {'last_value': 8}), # mul
            ("012345678, 01234 12345678!", {'last_value': 2}), # div
            ("01234, 01235 123456789!", {'last_value': True}), # equals
            ("01234, 01 123456789!", {'last_value': False}), # equals
            ("Collin, fish 1234567890!", {'last_value': True}), # greater
            ("fish, Collin  1234567890!", {'last_value': False}), # greater
            ("Collin, fish 12345678901!", {'last_value': False}), # less
            ("fish, Collin  12345678901!", {'last_value': True}), # less
            # ("Collin, fish fiver!", {'last_value': 3}), # negate
            # ("Collin, fish fiver!", {'last_value': 3}), # or
            # ("Collin, fish fiver!", {'last_value': 3}), # and
        ]
        for test in tests:
            opParser = OperatorParser()
            parsedOperator = opParser.parse([test[0]])
            if parsedOperator is not None:
                expected = copy.deepcopy(test[1])
                parsedOperator.execute(test[1])

                print("START")
                print(test[1])
                print(f"Result: {expected == test[1]}\n\n")
    
    # tests_operations()

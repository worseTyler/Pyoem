from typing import List
from LineParsers.LineParser import LineParser
from ParsedObjects.ParsedObject import ParsedObject
from ParsedObjects.ParsedOperator import ParsedOperator


class OperatorParser(LineParser):
    def __init__(self) -> None:
        super().__init__()
    
    def parse(self, block: List[str], line_parsers: List) -> ParsedObject:
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
import re
from typing import List
from LineParsers.LineParser import LineParser
from ParsedObjects.ParsedFunctionCall import ParsedFunctionCall
from ParsedObjects.ParsedObject import ParsedObject
from ParsedObjects.ParsedOperator import ParsedOperator
from util import Util


class FunctionCallParser(LineParser):
    def __init__(self) -> None:
        super().__init__()
    
    def parse(self, block: List[str], line_parsers: List) -> ParsedObject:
        current_line = block[0]
        regex_result = re.match('".+".*((.+))', current_line)
        if regex_result == None:
            # this is not a function invocation
            return None
        
        current_line = current_line.replace('"', '')
        current_line = current_line.replace(')', '')
        current_line = current_line.replace('(', ',')
        operands = current_line.split(',')

        function_name = operands[-1].strip().upper()
        params = list(map(lambda x: x.strip(), operands[:-1]))

        block.pop(0)

        parsed_function_call = ParsedFunctionCall(function_name, params)
        return parsed_function_call
from typing import List
from LineParsers.LineParser import LineParser
from ParsedObjects.ParsedFor import ParsedFor
from ParsedObjects.ParsedObject import ParsedObject

class ForParser(LineParser):

    def __init__(self) -> None:
        pass
    
    def parse(self, block: List[str], line_parsers: List) -> ParsedObject:
        current_line = block[0]
        if not current_line.strip().endswith('...'):
            #This is not a for loop
            return None

        block.pop(0)

        for_operands = block[0].split(' ')
        if len(for_operands) not in [2,3]:
            raise SyntaxError("Clearly someone didn't major in English Lit")
        
        if len(for_operands) == 2:
            for_operands.insert(0, None)

        block.pop(0)

        internal_logic = []
        while not block[0].strip().endswith('.') or block[0].strip().endswith('...'):
            for line_parser in line_parsers:
                parsed_object = line_parser.parse(block, line_parsers)
                if parsed_object is not None:
                    internal_logic.append(parsed_object)
                    break
        block.pop(0)
        parsed_object = ParsedFor(for_operands, internal_logic)
        return parsed_object
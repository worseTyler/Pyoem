from typing import List
from LineParsers.LineParser import LineParser
from ParsedObjects.ParsedConditional import ParsedConditional
from ParsedObjects.ParsedObject import ParsedObject

class ConditionalParser(LineParser):

    def __init__(self) -> None:
        pass
    
    def parse(self, block: List[str], line_parsers: List) -> ParsedObject:
        current_line = block[0]
        if not current_line.strip().endswith('?'):
            #This is not a conditional
            return None

        block.pop(0)
        internal_logic = []
        while not block[0].strip().endswith('.') or block[0].strip().endswith('...'):
            for line_parser in line_parsers:
                parsed_object = line_parser.parse(block, line_parsers)
                if parsed_object is not None:
                    internal_logic.append(parsed_object)
                    break
        block.pop(0)
        parsed_object = ParsedConditional(internal_logic)
        return parsed_object
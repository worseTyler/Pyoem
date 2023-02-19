from typing import List
from LineParsers.LineParser import LineParser
from LineParsers.OperatorParser import OperatorParser
from ParsedObjects.ParsedConditional import ParsedConditional
from ParsedObjects.ParsedObject import ParsedObject

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
        return parsed_object

class LineParserHolder():
    line_parsers = [
        OperatorParser(),
        ConditionalParser(),
    ]
from typing import List
from BlockParsers.BlockParser import BlockParser
from LineParsers.ConditionalParser import ConditionalParser
from LineParsers.LineParser import LineParser
from LineParsers.OperatorParser import OperatorParser
from ParsedBlocks.ExecutableParsedBlock import ExecutableParsedBlock
from ParsedBlocks.FunctionParsedBlock import FunctionParsedBlock
from ParsedBlocks.ParsedBlock import ParsedBlock


class FunctionParser(BlockParser):
    def __init__(self, line_parsers: List[LineParser]) -> None:
        super().__init__(line_parsers)

    def parse(self, block: List[str]) -> ParsedBlock:
        if not block[0].isupper(): 
            # This block is not a function block
            return None

        parameters = block[0].strip().split(' ')
        function_identifier = block[0].strip()
        block.pop(0)

        parsed_objects = []
        while len(block) > 0:
            for line_parser in self.line_parsers:
                parsed_object = line_parser.parse(block, self.line_parsers)
                if parsed_object is not None:
                    parsed_objects.append(parsed_object)
                    break

        executable_block = ExecutableParsedBlock(parsed_objects)
        parsed_block = FunctionParsedBlock(function_identifier, parameters, executable_block)
        return parsed_block
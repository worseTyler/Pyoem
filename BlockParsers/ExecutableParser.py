from typing import List
from BlockParsers.BlockParser import BlockParser
from LineParsers.ConditionalParser import ConditionalParser
from LineParsers.OperatorParser import OperatorParser
from ParsedBlocks.ExecutableParsedBlock import ExecutableParsedBlock
from ParsedBlocks.ParsedBlock import ParsedBlock


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
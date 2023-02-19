from typing import List
from LineParsers.LineParser import LineParser
from ParsedBlocks.ParsedBlock import ParsedBlock


class BlockParser():
    def __init__(self, line_parsers: List[LineParser]) -> None:
        self.line_parsers = line_parsers

    def parse(self, block: List[str]) -> ParsedBlock:
        pass
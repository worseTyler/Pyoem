from typing import List
from BlockParsers.BlockParser import BlockParser
from LineParsers.LineParser import LineParser
from ParsedBlocks.DeclarationParsedBlock import DeclarationParsedBlock
from ParsedBlocks.ParsedBlock import ParsedBlock
from util import Util


class DeclarationParser(BlockParser):
    def __init__(self, line_parsers: List[LineParser]) -> None:
        super().__init__(line_parsers)
    
    def parse(self, block: List[str]) -> ParsedBlock:
        if not block[-1].startswith('-'): 
            # This block is not a static declaration
            return None

        name = block[-1].lstrip('- ')

        contents = []
        for line in block[:-1]:
            line = line.strip(',').strip(' ')
            if line.startswith("'") and line.endswith("'"):
                # is string
                line = line.strip("'")
                contents.append(line)
            else:
                # is number
                num = Util.pyoem_str_to_num(line)
                contents.append(num)

        if len(contents) == 1:
            contents = contents[0]
        
        block = DeclarationParsedBlock(contents, name)
        return block
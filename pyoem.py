

from BlockParsers.DeclarationParser import DeclarationParser
from BlockParsers.ExecutableParser import ExecutableParser
from BlockParsers.FunctionParser import FunctionParser
from LineParsers.ConditionalParser import ConditionalParser
from LineParsers.ForParser import ForParser
from LineParsers.FunctionCallParser import FunctionCallParser
from LineParsers.OperatorParser import OperatorParser


class Pyoem():
    def __init__(self) -> None:
        self.last = None
        self.var_store = {}
        self.raw_lines = []
        self.blocks = []
        self.parsed_blocks = []
        self.line_parsers = [
            OperatorParser(),
            ConditionalParser(),
            ForParser(),
            FunctionCallParser(),
        ]

        self.block_parsers = [
            DeclarationParser(self.line_parsers),
            FunctionParser(self.line_parsers),
            ExecutableParser(self.line_parsers),
        ]


    def load_file(self, file_name):
        with open(file_name, "r") as file:
            currentBlock = []
            for line in file.readlines():
                
                line = line.strip('\n')
                self.raw_lines.append(line)
                
                if line != '':
                    currentBlock.append(line)
                
                if line == '' and len(currentBlock) > 0:
                    self.blocks.append(currentBlock)
                    currentBlock = []
            
            self.blocks.append(currentBlock)

    def parse_blocks(self):
        for block in self.blocks:
            for parser in self.block_parsers:
                parsedBlock = parser.parse(block)
                if parsedBlock is not None:
                    self.parsed_blocks.append(parsedBlock)
                    break

    def execute_blocks(self):
        for parsedBlock in self.parsed_blocks:
            parsedBlock.execute(self.var_store)

    def printStore(self):
        print(self.var_store)

if __name__ == "__main__":
    pyoem = Pyoem()
    pyoem.load_file("./test.txt")
    pyoem.parse_blocks()
    pyoem.execute_blocks()
    pyoem.printStore()
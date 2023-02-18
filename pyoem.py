
from block_parser import DeclarationParser


class Pyoem():
    def __init__(self) -> None:
        self.last = None
        self.var_store = {}
        self.raw_lines = []
        self.blocks = []
        self.parsed_blocks = []


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
            print(self.blocks)

    def parse_blocks(self):
        for block in self.blocks:
            parser = DeclarationParser(block)
            parsedBlock = parser.parse()
            if parsedBlock is not None:
                self.parsed_blocks.append(parsedBlock)

    def execute_blocks(self):
        for parsedBlock in self.parsed_blocks:
            self.var_store = parsedBlock.execute(self.var_store)

    def printStore(self):
        print(self.var_store)

if __name__ == "__main__":
    pyoem = Pyoem()
    pyoem.load_file("./test.txt")
    pyoem.parse_blocks()
    pyoem.execute_blocks()
    pyoem.printStore()
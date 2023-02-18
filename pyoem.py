
class Pyoem():
    def __init__(self) -> None:
        self.last = None
        self.var_store = {}
        self.raw_lines = []
        self.blocks = []


    def load_file(self, file_name):
        with open(file_name, "r") as file:
            currentBlock = []
            for line in file.readlines():
                
                line = line.strip('\n')
                self.raw_lines.append(line)
                currentBlock.append(line)
                
                if line == '' and len(currentBlock) > 0:
                    self.blocks.append(currentBlock[:-1])
                    currentBlock = []
            self.blocks.append(currentBlock)

if __name__ == "__main__":
    pyoem = Pyoem()
    pyoem.load_file("./test.txt")
    print(pyoem.raw_lines)
    print(pyoem.blocks)
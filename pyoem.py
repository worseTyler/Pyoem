
class Pyoem():
    def __init__(self) -> None:
        self.last = None
        self.var_store = {}
        self.raw_lines = []
        self.blocks = []


    def load_file(self, file_name):
        with open(file_name, "r") as file:
            self.raw_lines = list(map(lambda x: x.replace('\n', ''), file.readlines()))


if __name__ == "__main__":
    pyoem = Pyoem()
    pyoem.load_file("./test.txt")
    print(pyoem.raw_lines)
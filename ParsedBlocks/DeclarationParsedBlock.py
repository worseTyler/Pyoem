from ParsedBlocks.ParsedBlock import ParsedBlock


class DeclarationParsedBlock(ParsedBlock):
    def __init__(self, value, name) -> None:
        self.value = value
        self.name = name
        super().__init__()

    def execute(self, var_store: dict) -> None:
        var_store[self.name] = self.value
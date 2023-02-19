from ParsedBlocks.ParsedBlock import ParsedBlock


class ExecutableParsedBlock(ParsedBlock):
    def __init__(self, parsed_objects) -> None:
        self.parsed_objects = parsed_objects
        super().__init__()

    def execute(self, var_store: dict) -> None:
        for parsed_object in self.parsed_objects:
            parsed_object.execute(var_store)
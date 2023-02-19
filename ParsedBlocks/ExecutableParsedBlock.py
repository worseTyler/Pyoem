import copy
from ParsedBlocks.ParsedBlock import ParsedBlock


class ExecutableParsedBlock(ParsedBlock):
    def __init__(self, parsed_objects) -> None:
        self.parsed_objects = parsed_objects
        super().__init__()

    def execute(self, var_store: dict) -> None:
        logic = copy.deepcopy(self.parsed_objects)
        for parsed_object in logic:
            parsed_object.execute(var_store)
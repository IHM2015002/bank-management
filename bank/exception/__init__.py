
class NotFoundException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class DuplicateFoundException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
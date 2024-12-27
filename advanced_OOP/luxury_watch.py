import re

class LuxuryWatch:
    __watches_created: int = 0
    def __init__(self):
        LuxuryWatch.__watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created

    @classmethod
    def create_watches_with_dedicated_engraving(cls,text):
        cls.text_validate(text)
        LuxuryWatch.__watches_created += 1

    @staticmethod
    def text_validate(text):
        validate_result = re.search(r"^[a-zA-Z0-9]+$", text)
        assert validate_result is not None and len(text) < 40, f"The text '{text}' is not valid"

try:
    LuxuryWatch.create_watches_with_dedicated_engraving("HelloWorld")
    LuxuryWatch()
    LuxuryWatch.create_watches_with_dedicated_engraving("Hello World")
except AssertionError as e:
    print(e)
finally:
    print(f"{LuxuryWatch.get_number_of_watches_created()} luxury watches created.")


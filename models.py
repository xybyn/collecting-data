class Year:
    def __init__(self, year):
        self.year = year
        self.areas = []

class Area:
    def __init__(self, name):
        self.name = name
        self.institutes = []

class Institute:
    def __init__(self, name):
        self.name = name
        self.indicators = []
        self.directions = []

class Indicator:
    def __init__(self, indicator, value):
        self.indicator = indicator
        self.value = value

class Direction:
    def __init__(self, direction):
        self.direction = direction

def my_default(obj):
    if isinstance(obj, Area):
        return {
            "name": obj.name,
            "institutes" : obj.institutes
        }
    if isinstance(obj, Institute):
        return {
            "name": obj.name,
            "indicators" : obj.indicators,
            "directions" : obj.directions
        }
    if isinstance(obj, Indicator):
        return {
            "indicator": obj.indicator,
            "value": obj.value,
        }
    if isinstance(obj, Direction):
        return {
            "direction": obj.direction,

        }
    if isinstance(obj, Year):
        return {
            "year": obj.year,
            "areas": obj.areas,

        }

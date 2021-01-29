class DataProcessingPipeline:
    def __init__(self, target_string):
        self.target_string = target_string

    def add(self, f):
        self.target_string = f(self.target_string)
        return self


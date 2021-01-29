class CollectionProcessingPipeline:
    def __init__(self, target_collection):
        self.target_collection = target_collection

    def add(self, f):
        self.target_collection = [f(item) for item in self.target_collection]
        return self

    def remove_nulls(self):
        self.target_collection = [item for item in self.target_collection if item]

    def remove_empty(self):
        self.target_collection = [item for item in self.target_collection if item != ' ' and item != '']

class PollListNodeFactory:
    """Model for Polllist Data Node"""

    def __init__(self, keys):
        self.keys = keys

    def create_node(self, args):
        response = {}

        if len(args) is not len(self.keys):
            print("Cannot create dictonary!")
            print(args)
            return response

        for i in range(0, len(args)):
            response[self.keys[i]] = args[i]
        return response

    def is_valid_node(self, args):
        if len(args) is not len(self.keys):
            return False
        else:
            return True

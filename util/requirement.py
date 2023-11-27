""" requirement class """

class Requirement:
    """requirement"""

    def __init__(self, level, index, key, value, parameter, relationreq):
        """init"""
        self.level = level
        self.index = index
        self.key = key
        self.value = value
        self.parameter = parameter
        self.relationreq = relationreq

    def get_level(self):
        """get level"""
        return self.level

    def get_index(self):
        """get index"""
        return self.index

    def get_key(self):
        """get key"""
        return self.key

    def get_value(self):
        """get value"""
        return self.value

    def get_parameter(self):
        """get parameter"""
        return self.parameter

    def get_relationreq(self):
        """get relation requirement"""
        return self.relationreq

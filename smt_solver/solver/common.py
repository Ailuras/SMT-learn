

class tp(object):
    def __init__(self):
        self.common_types = {
            "BOOL": "Bool",
            "INT": "Int",
            "REAL": "Real",
            "STRING": "String"
        }

    @property
    def BOOL(self):
        return self.common_types["BOOL"]

    @property
    def INT(self):
        return self.common_types["INT"]

    @property
    def REAL(self):
        return self.common_types["REAL"]

    @property
    def STRING(self):
        return self.common_types["STRING"]
    
types = tp()

class NotImplementError(Exception):
    pass
class Ion:
    def __init__(self, ion, count):
        self.ion = ion
        self.count = count
        pass

    def __str__(self):
        return str(self.__dict__)
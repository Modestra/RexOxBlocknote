class AppParams():
    _instance = None
    _params = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppParams, cls).__new__(cls)
        return cls._instance

params = AppParams()
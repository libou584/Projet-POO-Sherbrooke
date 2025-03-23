class Application:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            instance = super().__new__(cls)
            instance.__user_logged_in = None
            instance.__database_handler = None
            cls.__instance = instance
        return cls.__instance


class ApplicationState:
    _instance = None

    def __init__(self) -> None:
        if ApplicationState._instance is not None:
            raise Exception("This class is a singleton!")
        self.is_logged_in = False

    @classmethod
    def get_app_state(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

if __name__ == '__main__':
    app_state1 = ApplicationState.get_app_state()
    print(f"App State 1 - Logged In: {app_state1.is_logged_in}")

    app_state2 = ApplicationState.get_app_state()
    app_state1.is_logged_in = True

    print(f"App State 1 - Logged In: {app_state1.is_logged_in}")
    print(f"App State 2 - Logged In: {app_state2.is_logged_in}")
    print(f"app_state1 is app_state2: {app_state1 is app_state2}")

    app = ApplicationState() # Exception as this class is singleton
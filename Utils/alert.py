class Alert():
    def __init__(self, message: str, level: str = "info"):
        self.message = message
        self.level = level

    def display(self):
        print(f"[{self.level.upper()}] {self.message}")

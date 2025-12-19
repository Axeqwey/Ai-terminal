class TerminalUI:
    def system(self, text):
        print(f"[SYSTEM] {text}")

    def ai(self, text):
        print(f"[AI] {text}")

    def error(self, text):
        print(f"[ERROR] {text}")

ui = TerminalUI()

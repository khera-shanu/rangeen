class Util:
    @staticmethod
    def _bg(text, bg_color):
        return f"\u001b[{bg_color+10}m{text}\u001b[0m"

    @staticmethod
    def _fg(text, fg_color):
        return f"\u001b[{fg_color}m{text}\u001b[0m"

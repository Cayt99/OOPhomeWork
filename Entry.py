class Entry:
    def __init__(self, date, time, text):
        self.date = date
        self.time = time
        self.text = text

    def __str__(self):
        return f"{self.date} {self.time}: {self.text}"

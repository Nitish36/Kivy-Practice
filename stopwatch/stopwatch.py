from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from datetime import datetime


class StopWatchApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.running = False  # State of the stopwatch
        self.seconds = 0  # Counter for time in seconds

    def build(self):
        return Builder.load_file("stopwatch.kv")

    def start_time(self):
        if not self.running:
            self.running = True
            # Schedule the update_time method to run every second (for stopwatch)
            Clock.schedule_interval(self.update_time, 1)

    def reset_time(self):
        # Reset the stopwatch
        self.running = False
        Clock.unschedule(self.update_time)  # Stop the clock schedule
        self.seconds = 0
        self.update_labels()

    def update_time(self, dt):
        # Increment the stopwatch timer
        if self.running:
            self.seconds += 1
            self.update_labels()

    def update_labels(self):
        # Update the stopwatch label
        minutes, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        stopwatch_time_string = f"[b]{hours:02}[/b]:{minutes:02}:{seconds:02}"

        # Update the stopwatch label (ID: stopwatch)
        self.root.ids.stopwatch.text = stopwatch_time_string

        # Update the real-time clock label
        current_time = datetime.now().strftime("%H:%M:%S")
        self.root.ids.time.text = f"[b]{current_time}[/b]"

    def start_clock(self):
        # Ensure that the current time label keeps updating independently of the stopwatch
        Clock.schedule_interval(self.update_labels, 1)  # Update the current time every second


if __name__ == "__main__":
    StopWatchApp().run()

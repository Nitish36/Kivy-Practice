from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem, TwoLineListItem
# Make a note on dialog box


class Screen1(MDScreen):
    pass


class Screen2(MDScreen):
    pass


class DemoApp(MDApp):
    def build(self):
        # Load the KV file directly; it contains the ScreenManager
        self.theme_cls.primary_pallete = "Green"
        self.theme_cls.primary_hue = "500"
        self.helper_str = Builder.load_file("practice.kv")
        return self.helper_str  # Return the loaded KV file here

    def on_start(self):
        # Reference the second screen by its name ("Second Screen")
        second_screen = self.helper_str.get_screen("Second Screen")
        for i in range(20):
            second_screen.ids.ls.add_widget(
                OneLineListItem(text=f'Item {i}')
            )
            second_screen.ids.ls.add_widget(
                TwoLineListItem(text=f'Item {i}', secondary_text=f'text {i}')
            )

    def theme_change(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


DemoApp().run()

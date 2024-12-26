from kivymd.app import MDApp
from kivy.lang import Builder


class Login(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        login_page = Builder.load_file("login.kv")
        return login_page

    def next(self):
        self.root.ids.slide.load_next(mode="next")
        self.root.ids.Name.text_color = self.theme_cls.primary_color
        self.root.ids.name.text_color = self.theme_cls.primary_color
        self.root.ids.name.icon = "check-decagram"

    def next1(self):
        self.root.ids.slide.load_next(mode="next")
        self.root.ids.Contact.text_color = self.theme_cls.primary_color
        self.root.ids.contact.text_color = self.theme_cls.primary_color
        self.root.ids.contact.icon = "check-decagram"

    def previous(self):
        self.root.ids.slide.load_previous()
        self.root.ids.Name.text_color = 0, 0, 0, 1
        self.root.ids.name.text_color = 0, 0, 0, 1
        self.root.ids.name.icon = "numeric-1-circle"

    def previous1(self):
        self.root.ids.slide.load_previous()
        self.root.ids.Contact.text_color = 0, 0, 0, 1
        self.root.ids.contact.text_color = 0, 0, 0, 1
        self.root.ids.contact.icon = "numeric-2-circle"


if __name__ == "__main__":
    Login().run()

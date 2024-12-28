from kivymd.app import MDApp
from kivy.lang import Builder


class Login(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        login_page = Builder.load_file("modernlogin.kv")
        return login_page


if __name__ == "__main__":
    Login().run()

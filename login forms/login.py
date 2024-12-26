from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (450, 500)


class Login(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        login_page = Builder.load_file("login.kv")
        return login_page

    def verify(self, email, password):
        if email == "nitish@gmail.com" and password == "1234":
            print("Logged in as Nitish")


if __name__ == "__main__":
    Login().run()

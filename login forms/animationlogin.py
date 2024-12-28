from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation


class Login(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        self.theme_cls.primary_palette = "Purple"
        login_page = Builder.load_file("animationlogin.kv")
        screen_manager.add_widget(login_page)
        return screen_manager

    def change_screen(self, name):
        screen_manager.current = name

    def anim(self, widget):
        anim = Animation(pos_hint={"center_y": 1.16})
        anim.start(widget)

    def anim1(self, widget):
        anim = Animation(pos_hint={"center_y": .85})
        anim.start(widget)

    def icons(self, widget):
        anim = Animation(pos_hint={"center_y": .8})
        anim += Animation(pos_hint={"center_y": .85})
        anim.start(widget)

    def text(self, widget):
        anim = Animation(opacity=0, duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)


if __name__ == "__main__":
    Login().run()

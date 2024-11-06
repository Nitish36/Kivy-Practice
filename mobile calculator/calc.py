import kivymd
from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (260,430)
Builder.load_file("calc.kv")

class MobileLayout(MDWidget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self,button):
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'

        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'

    def diff(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'

    def prod(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}*'

    def div(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def posneg(self):
        prior = self.ids.calc_input.text
        if '-' in prior:
            self.ids.calc_input.text = f"{prior.replace('-','')}"
        else:
            self.ids.calc_input.text = f"-{prior}"

    def equal(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)

        except:
            self.ids.calc_input.text = "Error"


class CalculatorApp(MDApp):
    def build(self):
        return MobileLayout()

if __name__ == "__main__":
    CalculatorApp().run()
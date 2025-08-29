from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalculatorLayout(BoxLayout):
    def digit_button(self, digit):
        if self.reset_screen:
            self.current_number = digit
            self.reset_screen = False
        elif self.current_number == '0':
            self.current_number = digit
        else:
            self.current_number += digit

        self.ids.display.text = self.current_number

    def operstion_button(self, op):
        print(f'Number {op}')

    def clear_button(self):
        self.current_number = '0'
        self.stored_number = None
        self.operation = None
        self.reset_screen = False
        self.ids.display.text = self.current_number

    def equals_button(self):
        print('Equals')

    def decimal_button(self):
        if '.' not in self.current_number:
            self.current_number += '.'
            self.ids.display.text = self.current_number


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_number = '0'
        self.stored_number = None
        self.operation = None
        self.reset_screen = False

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()
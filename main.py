from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalculatorLayout(BoxLayout):
    def digit_button(self, digit):
        print(f'Number {digit}')

    def operstion_button(self, op):
        print(f'Number {op}')

    def clear_button(self):
        print('Clear')

    def equals_button(self):
        print('Equals')

    def decimal_button(self):
        print('Decimal point')

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()
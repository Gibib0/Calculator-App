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

    def operation_button(self, op):
        if self.operation and not self.reset_screen:
            self.equals_button()

        self.stored_number = self.current_number
        self.operation = op
        self.reset_screen = True

    def clear_button(self):
        self.current_number = '0'
        self.stored_number = None
        self.operation = None
        self.reset_screen = False
        self.ids.display.text = self.current_number

    def equals_button(self):
        if not self.stored_number or not self.operation:
           return
        num1 = float(self.stored_number)
        num2 = float(self.current_number)

        if self.operation == '+':
            result = num1 + num2
        elif self.operation == '-':
            result = num1 - num2
        elif self.operation == '*':
            result = num1 * num2
        elif self.operation == '/':
            if num2 == 0:
                self.show_error()
                return

        self.current_number = str(result)

        self.ids.display.text = self.current_number

        self.operation = None
        self.reset_screen = True

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
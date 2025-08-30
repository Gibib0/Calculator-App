from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader

class CalculatorLayout(BoxLayout):

    def play_click_sound(self):
        if self.click_sound:
            self.click_sound.play()

    def play_error_sound(self):
        if self.error_sound:
            self.error_sound.play()

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
            else:
                result = num1 / num2

        self.current_number = str(result)

        self.ids.display.text = self.current_number

        self.operation = None
        self.reset_screen = True

    def decimal_button(self):
        if '.' not in self.current_number:
            self.current_number += '.'
            self.ids.display.text = self.current_number

    def show_error(self):
        self.current_number = 'Error'
        self.ids.display.text = 'ERROR'

        popup = ErrorPopup()
        popup.bind(on_dismiss=self.stop_error_sound)
        popup.open()

        self.play_error_sound()

        self.stored_number = None
        self.operation = None
        self.reset_screen = True

    def stop_error_sound(self, instance=None):
        if self.error_sound and self.error_sound.state == 'play':
            self.error_sound.stop()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_number = '0'
        self.stored_number = None
        self.operation = None
        self.reset_screen = False

        self.click_sound = SoundLoader.load('assets/sounds/click_sound.wav')
        self.error_sound = SoundLoader.load('assets/sounds/error_sound.wav')

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

class ErrorPopup(Popup):
    pass

if __name__ == '__main__':
    CalculatorApp().run()
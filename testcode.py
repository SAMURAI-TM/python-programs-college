from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.metrics import dp

# Set a mobile-friendly window size (you can adjust this)
Window.size = (360, 640)  # Typical mobile resolution

class TemperatureConverter(BoxLayout):
    result_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(10)

        # Temperature input
        self.add_widget(Label(
            text='Enter Temperature:',
            font_size=dp(20),
            size_hint=(1, 0.1)
        ))
        self.temp_input = TextInput(
            multiline=False,
            font_size=dp(18),
            size_hint=(1, 0.1),
            input_filter='float'
        )
        self.add_widget(self.temp_input)

        # From unit selector
        self.add_widget(Label(
            text='From:',
            font_size=dp(20),
            size_hint=(1, 0.1)
        ))
        self.from_unit = Spinner(
            text='Celsius',
            values=('Celsius', 'Fahrenheit', 'Kelvin'),
            size_hint=(1, 0.1),
            font_size=dp(18)
        )
        self.add_widget(self.from_unit)

        # To unit selector
        self.add_widget(Label(
            text='To:',
            font_size=dp(20),
            size_hint=(1, 0.1)
        ))
        self.to_unit = Spinner(
            text='Fahrenheit',
            values=('Celsius', 'Fahrenheit', 'Kelvin'),
            size_hint=(1, 0.1),
            font_size=dp(18)
        )
        self.add_widget(self.to_unit)

        # Convert button
        self.convert_btn = Button(
            text='🚀 Convert Now',
            size_hint=(1, 0.1),
            font_size=dp(20),
            background_color=(0.09, 0.74, 0.52, 1),  # Green color
            background_normal=''
        )
        self.convert_btn.bind(on_press=self.convert_temperature)
        self.add_widget(self.convert_btn)

        # Result label
        self.result_label = Label(
            text='',
            font_size=dp(20),
            size_hint=(1, 0.2),
            color=(0, 1, 0, 1)  # Lime color
        )
        self.add_widget(self.result_label)

        # Creator credit
        self.add_widget(Label(
            text='Created by: TANMOY MITRA',
            font_size=dp(14),
            size_hint=(1, 0.1),
            italic=True
        ))

    def convert_temperature(self, instance):
        try:
            temp = float(self.temp_input.text.strip())
            from_unit = self.from_unit.text
            to_unit = self.to_unit.text

            if not self.temp_input.text.strip():
                raise ValueError("Temperature field cannot be empty!")

            if from_unit == to_unit:
                self.result_label.text = f"{temp:.2f} {to_unit}"
                return

            # Convert to Celsius first
            if from_unit == "Fahrenheit":
                temp = (temp - 32) * 5/9
            elif from_unit == "Kelvin":
                temp = temp - 273.15

            # Convert from Celsius to target unit
            if to_unit == "Fahrenheit":
                temp = (temp * 9/5) + 32
            elif to_unit == "Kelvin":
                temp = temp + 273.15

            # Validate temperature
            if (from_unit == "Kelvin" and temp < -273.15) or \
               (to_unit == "Kelvin" and temp < 0):
                raise ValueError("Temperature below absolute zero!")

            self.result_label.text = f"Converted: {temp:.2f} {to_unit}"

        except ValueError as e:
            self.result_label.text = str(e) if str(e) else "Invalid input!"
            self.result_label.color = (1, 0, 0, 1)  # Red for error
            # Reset color after 2 seconds
            from kivy.clock import Clock
            Clock.schedule_once(self.reset_result_color, 2)

    def reset_result_color(self, dt):
        self.result_label.color = (0, 1, 0, 1)  # Back to lime

class ConverterApp(App):
    def build(self):
        Window.clearcolor = (0.17, 0.24, 0.31, 1)  # Dark blue background
        return TemperatureConverter()

if __name__ == '__main__':
    ConverterApp().run()
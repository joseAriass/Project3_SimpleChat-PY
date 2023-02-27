import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class ChatApp(App):
    def build(self):
        self.chat_history = TextInput(multiline=True)
        self.msg_input = TextInput(multiline=False)
        self.send_button = Button(text="Enviar")
        self.send_button.bind(on_press=self.send_message)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.chat_history)
        layout.add_widget(self.msg_input)
        layout.add_widget(self.send_button)
        Clock.schedule_interval(self.update_chat_history, 1.0/30.0)
        return layout

    def send_message(self, instance):
        msg = self.msg_input.text
        self.chat_history.text += "[b]Yo:[/b] " + msg + "\n"
        self.msg_input.text = ""

    def update_chat_history(self, dt):
        pass # Aquí iría la lógica para obtener los mensajes de otros usuarios y mostrarlos en el chat

if __name__ == '__main__':
    ChatApp().run()

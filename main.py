from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

Window.clearcolor = (0.05, 0.05, 0.1, 1)

class CameraViewer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        title = Label(text="[b]AHMAD Camera Viewer[/b]", markup=True,
                       font_size='24sp', size_hint=(1, 0.1), color=(0.2, 0.8, 1, 1))
        self.add_widget(title)

        self.ip_input = TextInput(hint_text="IP Address (e.g. 192.168.1.10)",
                                   size_hint=(1, 0.08), multiline=False)
        self.add_widget(self.ip_input)

        self.port_input = TextInput(hint_text="Port (e.g. 8080)",
                                     size_hint=(1, 0.08), multiline=False)
        self.add_widget(self.port_input)

        connect_btn = Button(text="Connect Camera", size_hint=(1, 0.1),
                              background_color=(0.2, 0.6, 1, 1), font_size='18sp')
        connect_btn.bind(on_press=self.connect_camera)
        self.add_widget(connect_btn)

        self.status_label = Label(text="", size_hint=(1, 0.05), color=(1, 0.4, 0.4, 1))
        self.add_widget(self.status_label)

        preview_title = Label(text="Live Camera Preview", size_hint=(1, 0.08),
                               font_size='16sp', color=(0.7, 0.7, 0.7, 1))
        self.add_widget(preview_title)

        self.image_widget = AsyncImage(size_hint=(1, 0.5))
        self.add_widget(self.image_widget)

    def connect_camera(self, instance):
        ip = self.ip_input.text.strip()
        port = self.port_input.text.strip()
        if not ip or not port:
            self.status_label.text = "Pehle IP aur Port dono likho"
            return
        url = f"http://{ip}:{port}/video"
        self.status_label.text = f"Connecting to {url}..."
        self.image_widget.source = url
        self.image_widget.reload()

class CameraApp(App):
    def build(self):
        self.title = "AHMAD Camera Viewer"
        return CameraViewer()

if __name__ == '__main__':
    CameraApp().run()

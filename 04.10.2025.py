from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import filechooser

class GaleriApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.button = Button(text='Pilih Foto dari Galeri', size_hint=(1, 0.2))
        self.button.bind(on_press=self.buka_galeri)

        self.label = Label(text='Belum ada foto dipilih', size_hint=(1, 0.1))
        self.image = Image()

        self.layout.add_widget(self.button)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.image)

        return self.layout

    def buka_galeri(self, instance):
        filechooser.open_file(on_selection=self.tampilkan_foto)

    def tampilkan_foto(self, selection):
        if selection:
            foto_path = selection[0]
            self.image.source = foto_path
            self.image.reload()
            self.label.text = f'Foto: {foto_path.split("/")[-1]}'

if __name__ == '__main__':
    GaleriApp().run()
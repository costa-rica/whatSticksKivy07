from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('parentscreen1/ps1.kv')


class ParentScreen1(Screen):
  email_text = StringProperty()
  password_text = StringProperty()
  email_field = ObjectProperty()
  password_field = ObjectProperty()
  password_flag_text =ObjectProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen1 __init__')
    self.ps1_base_width=1
    self.ps1_base_height=1

  def get_heights(self):
    for i in self.children:
      print(i, i.height)

  def show_password(self, checkbox, value):
    if value:
      self.label_show_password.text="Hide password"
      self.md_txt_field_password.password=False
    else:
      self.label_show_password.text="Show password"
      self.md_txt_field_password.password = True

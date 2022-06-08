from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
import os
import parentscreen1.ps1

Builder.load_file('base.kv')

class BaseScreenManager(ScreenManager):
  controller = ObjectProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('BaseScreenManager __init__')
    self.bind(size=self.on_size)

  def on_size(self, *args):
    self.controller.base_scrn_manager_size(self)

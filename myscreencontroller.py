from base import BaseScreenManager

class MyScreenController():
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('MyScreenController __init__')
    self.view = BaseScreenManager(controller=self)
    self.ps1_size_count=0

  def base_scrn_manager_size(self, base_scrn_manger):
    if self.ps1_size_count==1:
      print('***base_scrn_manger size:', base_scrn_manger.children)
      ps1=base_scrn_manger.children[0]
      ps1.ps1_base_width,ps1.ps1_base_height=ps1.size
      print('ps1 base sizes:', ps1.ps1_base_width,ps1.ps1_base_height)

      #App Name Anchor
      ps1.anchor_app_name.size_hint=(1,None)
      ps1.anchor_app_name.height = ps1.ps1_base_height *.3
      ps1.label_app_name.font_size=ps1.ps1_base_width*.1

      #Email Anchor
      ps1.anchor_email.padding=(ps1.ps1_base_width * .06,
        0,ps1.ps1_base_width * .06,0)
      ps1.md_txt_field_email.font_size=ps1.ps1_base_width*.06

      #Password Anchor
      ps1.anchor_password.padding=(ps1.ps1_base_width * .06,
        0,ps1.ps1_base_width * .06,0)
      ps1.md_txt_field_password.font_size=ps1.ps1_base_width*.06
      ps1.md_txt_field_password.size_hint=(1,None)
      ps1.md_txt_field_password.height=ps1.ps1_base_height *.07
      #Show Password
      # ps1.md_checkbox_show_password.size_hint=(.2,None)
      # ps1.label_show_password.size_hint=(.8,None)



    self.ps1_size_count+=1

  def get_screen(self):
    return self.view

from ._anvil_designer import signupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import lu
from .. import mg
import datetime

class signup(signupTemplate):
    def __init__(self, **properties):
      # Set Form properties and Data Bindings.
      self.init_components(**properties)
      lx = mg.my_lang
      self.text_1.text = lu.sign_up_title[lx]
      self.text_1.text_color = "darkgreen"
      self.text_box_1.placeholder = lu.user_placeholder[lx]
      self.text_box_2.placeholder = lu.pwd_placeholder[lx]
      self.text_box_3.placeholder = lu.pwd_repeat_placeholder[lx]
      self.save_sign_up.text = lu.save_btn[lx]
      self.cancel_sign_up.text = lu.cancel_btn[lx]
      self.new_user = {"u": '', "p": ''}

    # Any code you write here will run before the form opens.

    def text_box_1_change(self, **event_args):
      lx = mg.my_lang
      if len(self.text_box_1.text) < 5:
        self.err_user_name.visible = True
        self.err_user_name.text = lu.err_username1[lx]
      elif len(self.text_box_1.text) > 10:
        self.err_user_name.visible = True
        self.err_user_name.text = lu.err_username2[lx]
      else:
        self.err_user_name.visible = False

    def text_box_3_change(self, **event_args):
      lx = mg.my_lang
      if not self.text_box_3.text == self.text_box_2.text:
        self.err_pwd.visible = True
        self.err_pwd.text = lu.err_pwd[lx]
      else:
        self.err_pwd.visible = False      

    def text_box_2_change(self, **event_args):
      lx = mg.my_lang
      if not self.text_box_3.text == self.text_box_2.text:
        self.err_pwd.visible = True
        self.err_pwd.text = lu.err_pwd[lx]
      else:
        self.err_pwd.visible = False      

    def save_sign_up_click(self, **event_args):
      """This method is called when the component is clicked."""
      lx = mg.my_lang
      if len(self.text_box_1.text) == 0:
        self.err_user_name.visible = True
        self.err_user_name.text = lu.err_username3[lx]
        return
      elif len(self.text_box_1.text) > 0 and len(self.text_box_1.text) < 5:
        self.err_user_name.visible = True
        self.err_user_name.text = lu.err_username1[lx]
        return
      elif len(self.text_box_1.text) > 10:
        self.err_user_name.visible = True
        self.err_user_name.text = lu.err_username2[lx]
        return
      else:
        n = any(c.isalpha() for c in self.text_box_1.text)
        if not n:
          self.err_user_name.visible = True
          self.err_user_name.text = lu.err_username_alpha[lx]
          return
        ## check against database
      usr = self.text_box_1.text
      row = app_tables.nutzer.get(email=usr)
      if row is None:
        pwd = self.text_box_2.text
        nuts_pwd = anvil.server.call('nuts_pwd', usr, pwd)
        if nuts_pwd == 27:
          self.new_user['u'] = self.text_box_1.text
          self.new_user['p'] = nuts_pwd
          mg.signup_cancel = False 
          self.raise_event("x-close-alert", value=self.new_user)
        else:
          alert("smothing went wrong with sign_up")
      else:
        self.err_user_name.visible = True
        self.err_user_name.text = lu.err_username_exists[lx]

    def cancel_sign_up_click(self, **event_args):
      lx = mg.my_lang
      self.raise_event("x-close-alert", value=42)
      n = Notification(lu.sorry[lx], style="warning")
      n.show()
      """This method is called when the component is clicked."""

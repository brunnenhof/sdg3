from ._anvil_designer import log_signTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import lu
from .. import mg

class log_sign(log_signTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    lx = mg.my_lang
    lx = 4
    self.regi_title.text = lu.sign_up_title[lx]
    self.regi_user.placeholder = lu.user_placeholder[lx]
    self.regi_pwd.placeholder = lu.pwd_placeholder[lx]
    self.regi_pwd2.placeholder = lu.pwd_repeat_placeholder[lx]
    self.regi_save.text = lu.save_btn[lx]
    self.regi_cancel.text = lu.cancel_btn[lx]
    self.new_user = {"ur": '', "pr": ''}
    self.login_title.text = lu.login_title_tx[lx]
    self.login_u.placeholder = lu.login_u_tx[lx]
    self.login_p.placeholder = lu.login_p_tx[lx]
    self.login_save.text = lu.login_title_tx[lx]
    self.login_cancel.text = lu.cancel_btn[lx]
    self.login_first.text = lu.login_first_btn[lx]
    self.log_in.visible = False 

  def login_u_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    pass

  def login_p_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    self.login_err.visible = False
    pass

  def login_save_click(self, **event_args):
    self.login_err.visible = False
    lx = mg.my_lang
    lx = 4
    usr = self.login_u.text
    rows = app_tables.nutzer.search(email=usr)
    if len(rows) == 1:
      pwd = self.login_p.text
      nuts = anvil.server.call('check_nuts', usr, pwd, rows[0]['pwd_hash'])
      if nuts:
        self.new_user['u'] = self.login_u.text
        self.new_user['p'] = pwd
        mg.signup_cancel = False 
        n = Notification(lu.loggedin[lx], style="success")
        n.show()
        self.raise_event("x-close-alert", value=self.new_user)
      else:
        self.login_err.visible = True
        self.login_err.text = lu.err_pwd_wrong[lx]
    else:
      self.login_err.visible = True
      self.login_err.text = lu.err_username_enter[lx]

  def login_cancel_click(self, **event_args):
    self.login_err.visible = False
    lx = mg.my_lang
    lx = 3
    self.raise_event("x-close-alert", value=342)
    n = Notification(lu.sorry[lx], style="warning")
    n.show()

  def login_first_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.log_in.visible = True 
    self.register.visible = False

  def regi_user_change(self, **event_args):
    self.regi_user_err.visible = False
    lx = mg.my_lang
    lx = 4
    if len(self.regi_user.text) < 5:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username1[lx]
    elif len(self.regi_user.text) > 10:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username2[lx]
    else:
      self.regi_user_err.visible = False

  def regi_pwd_change(self, **event_args):
    lx = mg.my_lang
    lx = 4
    if not self.regi_pwd.text == self.regi_pwd2.text:
      self.regi_pwd_err.visible = True
      self.regi_pwd_err.text = lu.err_pwd[lx]
    else:
      self.regi_pwd_err.visible = False      

  def regi_pwd2_change(self, **event_args):
    lx = mg.my_lang
    lx = 4
    if not self.regi_pwd.text == self.regi_pwd2.text:
      self.regi_pwd_err.visible = True
      self.regi_pwd_err.text = lu.err_pwd[lx]
    else:
      self.regi_pwd_err.visible = False      

  def regi_save_click(self, **event_args):
    """This method is called when the component is clicked."""
    lx = mg.my_lang
    lx = 4
    if len(self.regi_user.text) == 0:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username3[lx]
      return
    elif len(self.regi_user.text) > 0 and len(self.regi_user.text) < 5:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username1[lx]
      return
    elif len(self.regi_user.text) > 10:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username2[lx]
      return
    else:
      n = any(c.isalpha() for c in self.regi_user.text)
      if not n:
        self.regi_user_err.visible = True
        self.regi_user_err.text = lu.err_username_alpha[lx]
        return
        ## check against database
    usr = self.regi_user.text
    row = app_tables.nutzer.get(email=usr)
    if row is None:
      pwd = self.regi_pwd.text
      nuts_pwd = anvil.server.call('nuts_pwd', usr, pwd)
      if nuts_pwd == 27:
        self.new_user['u'] = usr
        self.new_user['p'] = nuts_pwd
        mg.signup_cancel = False 
        n = Notification(lu.saved[lx], style="success")
        n.show()
        self.raise_event("x-close-alert", value=self.new_user)
      else:
        alert("smothing went wrong with sign_up")
    else:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username_exists[lx]

  def regi_cancel_click(self, **event_args):
    lx = mg.my_lang
    lx = 3
    self.raise_event("x-close-alert", value=42)
    n = Notification(lu.sorry[lx], style="warning")
    n.show()
    """This method is called when the component is clicked."""

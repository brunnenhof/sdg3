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
#    lx = 4
    self.regi_title.text = lu.sign_up_title[lx]
    self.regi_user.placeholder = lu.user_placeholder[lx]
    self.regi_save.text = lu.save_btn[lx]
    self.regi_cancel.text = lu.cancel_btn[lx]
    self.regi_first.text = lu.regi_first_tx[lx]
#    self.regi_user.tooltip = lu.regi_user_tt[lx]
    self.new_user = {"ur": '', "pr": ''}
    self.login_title.text = lu.login_title_tx[lx]
    self.login_u.placeholder = lu.login_u_tx[lx]
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
#    lx = 4
    usr = self.login_u.text
    rows = app_tables.nutzer.search(email=usr)
    lenrows = len(rows)
    if len(rows) == 1:
      self.new_user['u'] = self.login_u.text
      mg.signup_cancel = False 
      mg.my_email = self.login_u.text
      self.raise_event("x-close-alert", value=self.new_user)
    elif lenrows == 0:
      self.login_err.visible = True
      self.login_err.text = lu.err_user_not_exits[lx]
      self.login_u.focus()

  def login_cancel_click(self, **event_args):
    self.login_err.visible = False
    lx = mg.my_lang
#    lx = 3
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
#    lx = 4
    if len(self.regi_user.text) < 3:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username1[lx]
    elif len(self.regi_user.text) > 15:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username2[lx]
    else:
      self.regi_user_err.visible = False

  def regi_save_click(self, **event_args):
    """This method is called when the component is clicked."""
    lx = mg.my_lang
#    lx = 4
    if len(self.regi_user.text) == 0:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username3[lx]
      self.regi_user.focus()
      return
    elif len(self.regi_user.text) > 0 and len(self.regi_user.text) < 3:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username1[lx]
      return
    elif len(self.regi_user.text) > 15:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username2[lx]
      return
        ## check against database
    usr = self.regi_user.text
    row = app_tables.nutzer.get(email=usr)
    if row is None:
      res = anvil.server.call('nuts_pwd', usr)
      self.new_user['u'] = usr
      mg.signup_cancel = False 
      self.raise_event("x-close-alert", value=self.new_user)
    else:
      self.regi_user_err.visible = True
      self.regi_user_err.text = lu.err_username_exists[lx]

  def regi_cancel_click(self, **event_args):
    lx = mg.my_lang
#    lx = 3
    self.raise_event("x-close-alert", value=42)
    n = Notification(lu.sorry[lx], style="warning")
    n.show()
    """This method is called when the component is clicked."""

  def regi_first_click(self, **event_args):
    self.log_in.visible = False 
    self.register.visible = True
    """This method is called when the component is clicked."""
    pass

  def regi_user_show(self, **event_args):
    self.regi_user.focus()
    pass

  def login_u_show(self, **event_args):
    self.login_u.focus()
    pass

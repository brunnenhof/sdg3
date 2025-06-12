from ._anvil_designer import adminTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class admin(adminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def adm_pw_pressed_enter(self, **event_args):
    """This method is called when the user presses enter in this component."""
    pass

  def adm_login_click(self, **event_args):
    """This method is called when the component is clicked."""
    pass

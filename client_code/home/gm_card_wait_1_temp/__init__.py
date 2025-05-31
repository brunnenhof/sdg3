from ._anvil_designer import gm_card_wait_1_tempTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import mg

class gm_card_wait_1_temp(gm_card_wait_1_tempTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.gm_card_wait_1_temp_reg.text = self.item['reg']
    self.gm_card_wait_1_temp_ta.text = self.item['ta']

from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.gaum_rp_reg.text = self.item['gmau_rp_reg']
    self.gaum_rp_role.text = self.item['gmau_rp_role']
    self.gaum_rp_login.text = self.item['gmau_rp_login']
    # Any code you write here will run before the form opens.

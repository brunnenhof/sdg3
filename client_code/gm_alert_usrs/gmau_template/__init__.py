from ._anvil_designer import gmau_templateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class gmau_template(gmau_templateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.gmau_rp_reg.text = self.item['gmau_rp_reg']
    self.gmau_rp_role.text = self.item['gmau_rp_role']
    self.gmau_rp_login.text = self.item['gmau_rp_login']

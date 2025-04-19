from ._anvil_designer import dec_rp_templateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class dec_rp_template(dec_rp_templateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.dec_rp_expl.text = self.item['dexpl']
    self.dec_rp_value.text = self.item['dvalue']


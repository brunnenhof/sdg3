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
    self.pol_expl.text = self.item['pol_expl']
    self.pol_name.text = self.item['pol_name']
    self.slide_min.text = self.item['pol_tltl']
    self.slide_max.text = self.item['pol_gl']
    self.slide_val.text = self.item['slide_val']


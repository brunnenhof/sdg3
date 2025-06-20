from ._anvil_designer import gm_graf_card_rp_tempTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class gm_graf_card_rp_temp(gm_graf_card_rp_tempTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.title.text = self.item['title']
    self.sub_title.text = self.item['subtitle']
    self.cap.text = self.item['cap']
    self.fig.source = self.item['fig']

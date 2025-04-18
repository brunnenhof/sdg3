from ._anvil_designer import pcgd_plot_card_rp_tempTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class pcgd_plot_card_rp_temp(pcgd_plot_card_rp_tempTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

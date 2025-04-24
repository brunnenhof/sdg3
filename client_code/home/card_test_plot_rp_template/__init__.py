from ._anvil_designer import card_test_plot_rp_templateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class card_test_plot_rp_template(card_test_plot_rp_templateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.ctp_rp_img1.source = self.item['fig1']
    self.ctp_rp_img2.source = self.item['fig2']

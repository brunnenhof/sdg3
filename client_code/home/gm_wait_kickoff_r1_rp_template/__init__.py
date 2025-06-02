from ._anvil_designer import gm_wait_kickoff_r1_rp_templateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class gm_wait_kickoff_r1_rp_template(gm_wait_kickoff_r1_rp_templateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.gm_wait_kickoff_r1_rp_reg.text = self.item['reg']
    self.gm_wait_kickoff_r1_rp_role.text = self.item['ta']

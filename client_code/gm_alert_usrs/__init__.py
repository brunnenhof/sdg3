from ._anvil_designer import gm_alert_usrsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import lu
from .. import mg
from .. import make_long

class gm_alert_usrs(gm_alert_usrsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    cid = 'TKP-90'
    lx = 1
#    lx = mg.lx
#    cid = mg.cid
    self.gmau_reg.text = lu.gmau_reg_tx[lx]
    self.gmau_role.text = lu.gmau_role_tx[lx]
    self.gmau_login.text = lu.gmau_login_tx[lx]
    rows = app_tables.nutzer.search(tables.order_by('reg'), tables.order_by('role'), game_id=cid, reg=q.not_('00'), role=q.not_('00'))
    slots = []
    for ro in rows:
      long_reg = make_long.do_reg_to_longreg(ro['reg'], lx)
      long_min = make_long.do_ta_to_longmini(ro['role'], lx)
      email = ro['email']
      slot = {'gmau_rp_reg' : long_reg, 'gmau_rp_role' : long_min, 'gmau_rp_login' : '<'+ro['email']+'>'}
      slots.append(slot)
    self.gmau_rp.items = slots

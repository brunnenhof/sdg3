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

  def get_budget_for_region(self, reg, cid, yr):
    lb = app_tables.budget.search(reg=reg, game_id=cid, yr=yr)
    print(lb)
    a = 2

  def calc_cost(self, pct, tltl, gl, maxc):
    cost = 0
    for i in range(0, len(pct)):
      nw = pct[i] - tltl[i]
      nb = 0
      nt = gl[i] - tltl[i]
      pct_of_range = nw / (nt - nb)
      cost += maxc * pct_of_range
    return cost

  def slider_1_change_end(self, **event_args):
    global budget
    row = app_tables.globs.get()
    cid = row['game_id']
    ta = row['ta'].capitalize()
    reg = row['reg']
    # update the games DB
    # need game_id, reg, pol, runde, to
    # set wert
    pol = self.pol_abbr.text
    runde = 1
    if runde==1:
      yr = 2025
    else:
      alert("OOPS in slider_1_change_end: forgot to set YEAR")
    row = app_tables.games.get(game_id=cid, pol=pol, runde=runde, ta=ta, reg=reg)
    print (row)
    row['wert'] = float(self.slider_1.value)
    self.slide_val.text = self.slider_1.value



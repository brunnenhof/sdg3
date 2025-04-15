from ._anvil_designer import homeTemplate
from anvil import *
from .. import mg
import webbrowser
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
import datetime

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.top_title.text = mg.top_title
    self.top_btn_help.text = mg.top_btn_help
    self.top_btn_thanks.text = mg.top_btn_thanks
    self.top_btn_poc.text = 'PoC'
    self.top_join_game.text = mg.top_join_game
    self.top_start_game.text = mg.top_start_game
    self.p_lb_choose_game.text = mg.p_lb_choose_game
    self.p_btn_select_game.text = mg.p_btn_select_game
    self.gm_board.text = mg.msg_gm_board
    self.gm_board_info.content = mg.msg_gm_board_info
    self.cb_af.text = mg.cb_af_tx
    self.cb_us.text = mg.cb_us_tx
    self.cb_cn.text = mg.cb_cn_tx
    self.cb_me.text = mg.cb_me_tx
    self.cb_sa.text = mg.cb_sa_tx
    self.cb_la.text = mg.cb_la_tx
    self.cb_pa.text = mg.cb_pa_tx
    self.cb_ec.text = mg.cb_ec_tx
    self.cb_eu.text = mg.cb_eu_tx
    self.cb_se.text = mg.cb_se_tx
    self.gm_reg_npbp.text = mg.gm_reg_npbp_tx
    self.gm_card_wait_1_info.content = mg.gm_card_wait_1_info_tx
    self.gm_card_wait_1_btn_check.text = mg.gm_card_wait_1_btn_check_tx
    self.gm_card_wait_1_btn_kick_off_round_1.text = mg.gm_card_wait_1_btn_kick_off_round_1_tx
    self.setup_npbp_label.text = mg.setup_npbp_label_tx

  def top_btn_thanks_click(self, **event_args):
    alert(content=mg.top_thanks_msg, title=mg.top_thanks_title, large=True)

  def top_btn_poc_click(self, **event_args):
    alert("Neither the user interface nor the server code is elegant nor efficient. Contact us if you can help making either or all better.",
         title="So far, this app is a Proof of Concept")

  def top_btn_help_click(self, **event_args):
    webbrowser.open_new("http://sdggamehelp.blue-way.net")

  def top_start_game_click(self, **event_args):
    game_id = anvil.server.call('generate_id')
    mg.my_game_id = game_id
    app_tables.status.add_row(game_id=game_id, game_status=0, gm_status=0, p_status=0, roles_avail=4)
    msg = mg.gm_id_msg1 + game_id + mg.gm_id_msg2
    alert(msg, title=mg.gm_id_title)
    anfang = time.time()
    self.task = anvil.server.call('launch_set_roles', game_id)
    self.top_entry_label.visible = True
    while not self.task.is_completed():
      self.top_entry_label.text = mg.top_entry_label_tx
    else:
      ende = time.time()
      dauer = round(ende - anfang, 1)
      alert('it took '+str(dauer)+' sec')
      self.top_entry.visible = False
      self.gm_board.text = mg.msg_gm_board + '  for '+game_id
      self.gm_role_reg.visible = True

  def top_join_game_click(self, **event_args):
    self.top_entry.visible = False
    how_many_new = len(app_tables.status.search(game_status=1, p_status=0))
    print(how_many_new)
    if how_many_new > 1:
      self.p_cp_choose_game.visible = True
      self.p_dd_select_game.items = [(row["game_id"], row) for row in app_tables.status.search(game_status=1, p_status=0)]
#      cid = self.p_dd_select_game.selected_value["game_id"]
#      alert(cid)
    elif how_many_new == 1:
      row = app_tables.status.get(game_status=1, p_status=0)
      alert(row['game_id'], title=mg.title_you_are_joining)
      mg.my_game_id = row['game_id']
      row.update(p_status=1)
      self.show_roles(row['game_id'])
    else:
      alert(mg.msg_game_not_started)
      self.top_entry.visible = True
      self.p_cp_choose_game.visible = False

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
#    print(f"The file's name is: {file.name}")
#    print(f"The number of bytes in the file is: {file.length}")
#    print(f"The file's content type is: {file.content_type}")
#    print(f"The file's contents are: '{file.get_bytes()}'")
    print(file)
    b = file.get_bytes()
    bb = b.decode("utf-8")
    bbb = bb.splitlines()
#    print(bbb)
    anvil.server.call('upload_csv_pols', bbb, 'regs')

  def p_btn_select_game_click(self, **event_args):
    alert(self.p_dd_select_game.selected_value['game_id'], title=mg.title_you_are_joining)
    game_id_chosen = self.p_dd_select_game.selected_value['game_id']
    mg.my_game_id = game_id_chosen
    row = app_tables.status.get(game_id=game_id_chosen)
    row.update(p_status=1) # he / she chose a game
    self.show_roles(game_id_chosen)
    self.p_cp_choose_game.visible = False
    self.card_select_reg_role.visible = True

  def gm_reg_npbp_click(self, **event_args):
    cid = mg.my_game_id
    self.setup_npbp_label.visible = False
    npbp = [] # not played by human players
    if self.cb_us.checked:
      npbp.append('us')
    if self.cb_af.checked:
      npbp.append('af')
    if self.cb_cn.checked:
      npbp.append('cn')
    if self.cb_me.checked:
      npbp.append('me')
    if self.cb_sa.checked:
      npbp.append('sa')
    if self.cb_la.checked:
      npbp.append('la')
    if self.cb_pa.checked:
      npbp.append('pa')
    if self.cb_ec.checked:
      npbp.append('ec')
    if self.cb_eu.checked:
      npbp.append('eu')
    if self.cb_se.checked:
      npbp.append('se')
    self.gm_cp_not_played.visible = False
    self.gm_board_info.visible = False
    anfang = time.time()
    self.task = anvil.server.call('launch_set_npbp', cid, npbp)
    while not self.task.is_completed():
      self.setup_npbp_label.visible = True
    else:
      self.setup_npbp_label.visible = False
      ende = time.time()
      dauer = round(ende - anfang, 1)
      alert('it took '+str(dauer)+' sec')
    
    self.gm_card_wait_1.visible = True

  def show_roles(self, cid):
    
    alert("show roles not yet coded")
    pass
    
  def gm_card_wait_1_btn_check_click(self, runde):
    cid = mg.my_game_id
    runde = mg.game_runde
    rows = app_tables.roles_assign.search(game_id=cid, round=runde, taken=0)
    slots = []
    for row in rows:
      slot = {'reg' : names[i], 'ta': cost}
      
    for i in range(0, len(pct)):
        nw = pct[i] - tltl[i]
        nb = 0
        nt = gl[i] - tltl[i]
        pct_of_range = nw / (nt - nb)
        cost = round(maxc * pct_of_range, 2)
        slot = {'pol_name' : names[i], 'pol_amount': cost}
        slots.append(slot)
    return slots

    slots = [{key: r[key] for key in ["reg", "ta"]} for r in app_tables.roles_assign.search(game_id=cid, round=runde, taken=0)]
    self.gm_card_wait_1_rp.items = slots
    pass

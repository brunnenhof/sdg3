from ._anvil_designer import homeTemplate
from anvil import *
from .. import mg
import webbrowser
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time

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

  def top_btn_thanks_click(self, **event_args):
    alert(content=mg.top_thanks_msg, title=mg.top_thanks_title, large=True)

  def top_btn_poc_click(self, **event_args):
    alert("Neither the user interface nor the server code is elegant nor efficient. Contact us if you can help making either or all better.",
         title="So far, this app is a Proof of Concept")

  def top_btn_help_click(self, **event_args):
    webbrowser.open_new("http://sdggamehelp.blue-way.net")

  def top_start_game_click(self, **event_args):
    game_id = anvil.server.call('generate_id')
    app_tables.status.add_row(game_id=game_id, closed=0, current_gm=0, current_p=0, roles_avail=4)
    msg = mg.gm_id_msg1 + game_id + mg.gm_id_msg2
    alert(msg, title=mg.gm_id_title)
    anfang = time.time()
    self.task = anvil.server.call('launch_set_roles', game_id)
    self.top_entry_label.visible = True
#      make something visible
    while not self.task.is_completed():
      self.top_entry_label.text = mg.top_entry_label_tx
    else:
      ende = time.time()
      dauer = ende - anfang
      alert('it took '+str(dauer))
      self.top_entry.visible = False
      self.gm_board.text = mg.msg_gm_board + '  for '+game_id
      self.gm_role_reg.visible = True

  def top_join_game_click(self, **event_args):
    self.top_entry.visible = False
    self.p_cp_choose_game.visible = True
    how_many_new = len(app_tables.status.search(closed=0, current_gm =0))
    if how_many_new > 1:
      self.p_cp_choose_game.visible = True
      self.p_dd_select_game.items = [(row["game_id"], row) for row in app_tables.status.search(closed=0, current_gm =0, roles_avail=1)]
    elif how_many_new == 1:
      row = app_tables.status.get(closed=0)
      alert(row['game_id'], title=mg.title_you_are_joining)
      mg.my_game_id = row['game_id']
      #### 
      #### xy must be replaced with the chosen region
      #### 
#      self.show_roles(row['game_id'], 'xy')
#      self.card_select_reg_role.visible = True
    else:
      alert(mg.msg_game_not_started)

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
    game_id_chosen = self.select_game.selected_value['game_id']
    mg.my_game_id = game_id_chosen
    self.show_roles(game_id_chosen, 'xy')
#    alert(my_globs.my_game_id,"stored globally")
    self.p_cp_choose_game.visible = False
#    self.card_select_reg_role.visible = True

  def gm_reg_npbp_click(self, **event_args):
    global cid
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
    set_up_gi, npbhp_str = anvil.server.call('start_new_game', cid, npbp, 1)
    if set_up_gi:
      self.label_set_up_game_info.visible = True
      temp, regions = anvil.server.call('set_up_game_db', 1, cid, npbp)
      if temp:
        self.label_rd1_setup1.visible = True
      anvil.server.call('set_up_game_db', 2, cid, npbp)
      self.label_rd2_setup.visible = True
      anvil.server.call('set_up_game_db', 3, cid, npbp)
      self.label_rd3_setup.visible = True
      anvil.server.call('set_up_role_assignments', cid, npbp, regions)
      txt = 'Role assignments are set up ... Now tell your players to join game ' + cid + ' and log in to their roles. You need to wait until all players have submitted their decisions for round 1, 2025 to 2040'
      self.label_role_assign.text = txt
      self.label_role_assign.visible = True

      self.card_all_logged_in.visible = True
      fdz = anvil.server.call('all_logged_in', cid)
      self.rep_nli.items = fdz
      while fdz:
        time.sleep(20)
        fdz = anvil.server.call('all_logged_in', cid)
        if fdz:
          self.rep_nli.items = fdz
          
      if not fdz:  #  meaning all players have logged in, the game mistress is now waiting for the decisions to be submitted
        self.card_all_logged_in.visible = False
        self.card_waiting_for_all_pol_submissions.visible = True
        fdz2 = anvil.server.call('dec_sub', cid)
        self.rep_wait_decisions.items = fdz2
        while fdz2:
          time.sleep(60)
          fdz2 = anvil.server.call('dec_sub', cid)  # # DECisions SUBmitted
          if fdz2:
            self.rep_wait_decisions.items = fdz2

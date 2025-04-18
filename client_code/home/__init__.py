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
    self.pcr_rb_af.text = mg.cb_af_tx
    self.pcr_rb_us.text = mg.cb_us_tx
    self.pcr_rb_cn.text = mg.cb_cn_tx
    self.pcr_rb_me.text = mg.cb_me_tx
    self.pcr_rb_sa.text = mg.cb_sa_tx
    self.pcr_rb_la.text = mg.cb_la_tx
    self.pcr_rb_pa.text = mg.cb_pa_tx
    self.pcr_rb_ec.text = mg.cb_ec_tx
    self.pcr_rb_eu.text = mg.cb_eu_tx
    self.pcr_rb_se.text = mg.cb_se_tx

    self.pcr_rb_pov.text = mg.cb_pov_tx
    self.pcr_rb_ineq.text = mg.cb_ineq_tx
    self.pcr_rb_emp.text = mg.cb_emp_tx
    self.pcr_rb_food.text = mg.cb_food_tx
    self.pcr_rb_ener.text = mg.cb_ener_tx
    self.pcr_rb_fut.text = mg.cb_fut_tx

    self.pcr_title.text = mg.pcr_title_tx
    self.pcr_col_left_title.text = mg.pcr_col_left_title_tx
    self.pcr_col_right_title.text = mg.pcr_col_right_title_tx
    self.pcr_submit.text = mg.pcr_submit_tx
#    self.pcr_submit_msg1.text = mg.pcr_submit_msg1
#    self.pcr_submit_msg2.text = mg.pcr_submit_msg2
    self.pcgd_title.text = mg.pcr_title_tx
    self.pcgd_info_rd1.content = mg.pcgd_rd1_info_tx
    self.pcgd_generating.text = mg.pcgd_generating_tx

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
#      alert(row['game_id'], title=mg.title_you_are_joining)
      mg.my_game_id = row['game_id']
#      row.update(p_status=1)
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
#    alert(self.p_dd_select_game.selected_value['game_id'], title=mg.title_you_are_joining)
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

  def set_avail_regs(self, **event_args):
    print("IN set_avail_regs")
    self.set_regs_invisible()
    cid = mg.my_game_id
    msg = mg.pcr_title_tx + ': '+cid
    self.pcr_title.text = msg
    runde = mg.game_runde
    regs = mg.regs
    for r in regs:
      len_rows_role_assign = len(app_tables.roles_assign.search(game_id=cid, taken=0, reg=r))
      if len_rows_role_assign > 0:
        if r == 'af':
          self.pcr_rb_af.visible = True
        elif r == 'us':
          self.pcr_rb_us.visible = True
        elif r == 'cn':
          self.pcr_rb_cn.visible = True
        elif r == 'me':
          self.pcr_rb_me.visible = True
        elif r == 'sa':
          self.pcr_rb_sa.visible = True
        elif r == 'la':
          self.pcr_rb_la.visible = True
        elif r == 'pa':
          self.pcr_rb_pa.visible = True
        elif r == 'ec':
          self.pcr_rb_ec.visible = True
        elif r == 'eu':
          self.pcr_rb_eu.visible = True
        elif r == 'se':
          self.pcr_rb_se.visible = True
     
  def show_roles(self, cid):
    print("in show_roles")
    self.pcr_col_right_title.visible = False
    self.pcr_submit.visible = False
    self.set_minis_invisible()
    self.set_regs_invisible()
    self.set_avail_regs()
    self.p_choose_role.visible =True
    
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
#    slots = [{key: r[key] for key in ["reg", "ta"]} for r in app_tables.roles_assign.search(game_id=cid, round=runde, taken=0)]
#    self.gm_card_wait_1_rp.items = slots
#    pass

  def set_minis_invisible(self, **event_args):
    self.pcr_rb_fut.visible = False
    self.pcr_rb_pov.visible = False
    self.pcr_rb_ineq.visible = False
    self.pcr_rb_emp.visible = False
    self.pcr_rb_food.visible = False
    self.pcr_rb_ener.visible = False
    self.pcr_rb_pov.selected = False
    self.pcr_rb_ineq.selected = False
    self.pcr_rb_emp.selected = False
    self.pcr_rb_food.selected = False
    self.pcr_rb_ener.selected = False
    self.pcr_rb_fut.selected = False

  def set_regs_invisible(self, **event_args):
    self.pcr_rb_us.visible = False
    self.pcr_rb_us.selected = False
    self.pcr_rb_af.visible = False
    self.pcr_rb_af.selected = False
    self.pcr_rb_cn.visible = False
    self.pcr_rb_cn.selected = False
    self.pcr_rb_me.visible = False
    self.pcr_rb_me.selected = False
    self.pcr_rb_sa.visible = False
    self.pcr_rb_sa.selected = False
    self.pcr_rb_la.visible = False
    self.pcr_rb_la.selected = False
    self.pcr_rb_pa.visible = False
    self.pcr_rb_pa.selected = False
    self.pcr_rb_ec.visible = False
    self.pcr_rb_ec.selected = False
    self.pcr_rb_eu.visible = False
    self.pcr_rb_eu.selected = False
    self.pcr_rb_se.visible = False
    self.pcr_rb_se.selected = False

  def set_ministries_visible(self, cid, reg):
    self.pcr_submit.visible = False
    self.set_minis_invisible()
    minis_ta = [r['role'] for r in app_tables.roles_assign.search(game_id=cid, reg=reg, taken=0)]
    for ta in minis_ta:
      if ta == 'pov':
        self.pcr_rb_pov.visible = True
      elif ta == 'emp':
        self.pcr_rb_emp.visible = True
      elif ta == 'ineq':
        self.pcr_rb_ineq.visible = True
      elif ta == 'food':
        self.pcr_rb_food.visible = True
      elif ta == 'ener':
        self.pcr_rb_ener.visible = True
      elif ta == 'fut':
        self.pcr_rb_fut.visible = True

  def reg_clicked(self, reg):
    cid = mg.my_game_id
    print ('in '+reg+' btn ' + cid)
    self.pcr_col_right_title.visible = True
    self.pcr_submit.visible = False
    mg.my_reg = reg
    self.set_minis_invisible()
    self.set_ministries_visible(cid, reg)

  def pcr_rb_us_clicked(self, **event_args):
    self.reg_clicked('us')

  def pcr_rb_af_clicked(self, **event_args):
    self.reg_clicked('af')

  def pcr_rb_pov_clicked(self, **event_args):
    self.pcr_submit.visible = True
    mg.my_ministry = 'pov'

  def pcr_rb_ineq_clicked(self, **event_args):
    self.pcr_submit.visible = True
    mg.my_ministry = 'ineq'    

  def pcr_rb_me_clicked(self, **event_args):
    self.reg_clicked('me')

  def pcr_rb_cn_clicked(self, **event_args):
    self.reg_clicked('cn')
    
  def pcr_rb_sa_clicked(self, **event_args):
    self.reg_clicked('sa')
    
  def pcr_rb_la_clicked(self, **event_args):
    self.reg_clicked('la')
    
  def pcr_rb_pa_clicked(self, **event_args):
    self.reg_clicked('pa')
    
  def pcr_rb_ec_clicked(self, **event_args):
    self.reg_clicked('ec')
    
  def pcr_rb_eu_clicked(self, **event_args):
    self.reg_clicked('eu')
    
  def pcr_rb_se_clicked(self, **event_args):
    self.reg_clicked('se')
    
  def pcr_rb_emp_clicked(self, **event_args):
    self.pcr_submit.visible = True
    mg.my_ministry = 'emp'    
    
  def pcr_rb_food_clicked(self, **event_args):
    self.pcr_submit.visible = True
    mg.my_ministry = 'food'    
    
  def pcr_rb_ener_clicked(self, **event_args):
    self.pcr_submit.visible = True
    mg.my_ministry = 'ener'    
    
  def pcr_rb_fut_clicked(self, **event_args):
    self.pcr_submit.visible = True
    mg.my_ministry = 'fut'    

  def all_roles_in_reg_logged(self, cid, reg):
    rows = len(app_tables.roles_assign.search(game_id=cid, taken=0, reg=reg))
    if rows == 0:
      return True
    else:
      return False
    
  def save_player_choice(self, cid, role, reg):
#    print ('in save_player_choice: ' + region)
#    print ('in save_player_choice: ' + ministry)
    rows = app_tables.roles_assign.search(game_id=cid, role=role, reg=reg)
    for r in rows:
      if r['taken'] == 0:
        r['taken'] = 1
        all_roles_in_reg_taken = self.all_roles_in_reg_logged(cid, reg)
        if all_roles_in_reg_taken:
          # set region as taken
          pass
      else:
        alert("Unfortunately, someone claimed the role before you :( Please choose another one.")
        return False
    return True
    
  def pcr_submit_click(self, **event_args):
    reg = mg.my_reg
    reglong = mg.reg_to_longreg[reg]
    role = mg.my_ministry
    rolelong = mg.ta_to_longmini[role]
    cid = mg.my_game_id
    self.pcgd_title.text = self.pcgd_title.text + ': ' +cid+', '+reglong+', '+rolelong
#    alert('reg is '+reg+' role is '+role)
    regs = mg.regs
    tas = mg.roles
    #tas = ['poverty', 'inequality', 'empowerment', 'food', 'energy', 'future']
    save_ok = self.save_player_choice(cid, role, reg)
    if save_ok:
      self.p_card_graf_dec.visible = True
      self.p_choose_role.visible = False
      which_region_long  = reglong
      wrx = mg.regs.index(reg)
      which_ministy_long = rolelong
      wmx = mg.roles.index(role)
      your_game_id = cid + "-" + str(wrx) + str(wmx)
      congrats = "\n" + mg.pcr_submit_msg1 + rolelong + mg.pcr_submit_msg2 + reglong + ".\n" + mg.pcr_submit_msg3 + "\n" + your_game_id 
      mg.my_personal_game_id = your_game_id
      alert(congrats)

      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 1)
      self.pcgd_generating.visible = True
#      make something visible
      while not self.task.is_completed():
        pass
      else:
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid)]
        self.plot_card_rp.items = slots

#      anvil.server.call('put_budget', 2025, cid)
#      within_budget = False
#      if which_ministry == 'future':
#        within_budget = self.do_future(cid, which_ministry, which_region, runde )
#      else:
#        self.do_non_future(cid, which_ministry, which_region , runde)      


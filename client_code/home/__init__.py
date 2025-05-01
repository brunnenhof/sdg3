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
import random

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    ### during dev, keep db small
    ### in production comment out the next 4 lines and only delete once game is closed
    ### in games_log
#    app_tables.cookies.delete_all_rows()
#    app_tables.state_of_play.delete_all_rows()
#    app_tables.step_done.delete_all_rows()
#    app_tables.roles_assign.delete_all_rows()
    ###
#    row = app_tables.cookies.get()
#    row.update(gm_step=0)
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
    self.gm_start_round.text = mg.gm_card_wait_1_btn_kick_off_round_1_tx
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
    self.fut_not_all_logged_in.text = mg.fut_not_all_logged_in_tx
#    self.pcr_submit_msg1.text = mg.pcr_submit_msg1
#    self.pcr_submit_msg2.text = mg.pcr_submit_msg2
    self.pcgd_title.text = mg.pcr_title_tx
    self.pcgd_info_rd1.content = mg.pcgd_rd1_info_tx
    self.pcgd_generating.text = mg.pcgd_generating_tx
    self.dec_info.content = mg.dec_info_tx
    self.dec_title.text = mg.dec_title_tx
    self.pcgd_advance.text = mg.pcgd_advance_tx

    self.refresh_numbers.text = mg.refresh_numbers_tx
    self.submit_numbers.text = mg.submit_numbers_tx
    self.fut_info.content = mg.fut_info_tx 
    self.fut_bud_lb1.text = mg.fut_bud_lb1_tx 
    self.fut_bud_lb2.text = mg.fut_bud_lb2_tx 
    self.fut_but_lb3.text = mg.fut_bud_lb3_tx 
    self.cpf_lb.text = mg.cfpov_tx
    self.cpf_lb2.text = mg.cfpov_lb_tx 
    self.cpf_ineq_lb.text = mg.cfineq_tx
    self.cpf_ineq_lb2.text = mg.cfineq_lb_tx 
    self.cpf_emp_lb.text = mg.cfemp_tx
    self.cpf_emp_lb2.text = mg.cfemp_lb_tx 
    self.cpf_food_lb.text = mg.cffood_tx
    self.cpf_food_lb2.text = mg.cffood_lb_tx 
    self.cpf_ener_lb.text = mg.cfener_tx
    self.cpf_ener_lb2.text = mg.cfener_lb_tx 
    self.gm_card_wait_1_temp_title.text = mg.gm_card_wait_1_temp_title_tx

    self.dropdown_menu_1.items = [("2025-2040", 1), ("2040-2060", 2), ("2060-2100", 3)]
    self.tick_refresh_fut.interval = 0

  def top_btn_thanks_click(self, **event_args):
    alert(content=mg.top_thanks_msg, title=mg.top_thanks_title, large=True)

  def top_btn_poc_click(self, **event_args):
    alert("Neither the user interface nor the server code is elegant nor efficient. Contact us if you can help making either or all better.",
         title="So far, this app is a Proof of Concept")

  def top_btn_help_click(self, **event_args):
    webbrowser.open_new("http://sdggamehelp.blue-way.net")

  def top_start_game_click(self, **event_args):
    game_id = anvil.server.call('generate_id')
    app_tables.cookies.add_row(game_id=game_id, r1sub=0, r2sub=0, r3sub=0,gm_step=0) ## clean slate
    self.top_start_game.visible = False
    self.top_join_game.visible = False
    mg.my_game_id = game_id
    jetzt = datetime.datetime.now()
    app_tables.games_log.add_row(game_id=game_id, gm_status=1, started=jetzt)
    msg = mg.gm_id_msg1 + game_id + mg.gm_id_msg2
    alert(msg, title=mg.gm_id_title)
    anfang = time.time()
    self.task = anvil.server.call('launch_set_roles', game_id)
    self.top_entry_label.visible = True
    while not self.task.is_completed():
      self.top_entry_label.text = mg.top_entry_label_tx
    else:
      ende = time.time()
      dauer = round(ende - anfang, 0)
      self.seconds.text = str(dauer)+' sec'
#      self.seconds.textcolor = '#FFD6D6'
      self.top_entry.visible = False
      self.gm_board.text = mg.msg_gm_board + '  for '+game_id
      self.gm_role_reg.visible = True

  def top_join_game_click(self, **event_args):
    rows = app_tables.games_log.search()
    if len(rows) == 1 and rows[0]['game_id'] == 'TEST':
      n = Notification(mg.no_active_game_to_join_tx, timeout=7, title='Ooopps...')
      n.show()
      return
    self.top_entry.visible = False
#    how_many_new = len(app_tables.games_log.search(gm_status=q.greater_than(3)))
    how_many_new = len(app_tables.games_log.search(gm_status=4))
    print(how_many_new)
    if how_many_new > 1:
      self.p_cp_choose_game.visible = True
      self.p_dd_select_game.items = [(row["game_id"], row) for row in app_tables.status.search(game_status=1, p_status=0, gm_status=1)]
#      cid = self.p_dd_select_game.selected_value["game_id"]
#      alert(cid)
    elif how_many_new == 1:
      row = app_tables.games_log.get(gm_status=4)
#      alert(row['game_id'], title=mg.title_you_are_joining)
      mg.my_game_id = row['game_id']
#      row.update(p_status=1)
      ccid = row['game_id']
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
    self.gm_cp_not_played.visible = False
    self.gm_board_info.visible = False
    self.setup_npbp_label.visible = True
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
    anfang = time.time()
    self.task = anvil.server.call('launch_set_npbp', cid, npbp)
    while not self.task.is_completed():
      self.setup_npbp_label.visible = True
    else:
      self.setup_npbp_label.visible = False
      ende = time.time()
      dauer = round(ende - anfang, 0)
      self.seconds.text = str(dauer)+' sec'
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
#    print("in show_roles")
    self.pcr_col_right_title.visible = False
    self.pcr_submit.visible = False
    self.set_minis_invisible()
    self.set_regs_invisible()
    self.set_avail_regs()
    self.p_choose_role.visible =True
    
  def gm_card_wait_1_btn_check_click(self, **event_args):
    cid = mg.my_game_id
    runde = mg.game_runde+1
    self.gm_card_wait_1_btn_check.visible = True
    self.gm_start_round.visible = False
    rows = app_tables.roles_assign.search(game_id=cid, round=runde, taken=0)
    if len(rows) == 0:
      self.gm_card_wait_1_btn_check.visible = False
      self.gm_start_round.visible = True
      self.gm_card_wait_1_rp.visible = False
      self.gm_card_wait_1_temp_title.text = mg.gm_card_wait_1_temp_title_tx2
    else:
      slots = []
#    slots2 = [{key: r[key] for key in ["reg", "role"]} for r in app_tables.roles_assign.search(game_id=cid, round=runde, taken=0)]
#    res = list({d[key] for d in slots2 if key in d})
      for row in rows:
        longreg = mg.reg_to_longreg[row['reg']]
        longrole = mg.ta_to_longmini[row['role']]
        slot = {'reg' : longreg, 'ta': longrole}
        if slot not in slots:
          slots.append(slot)
      self.gm_card_wait_1_temp_title.visible = True
      self.gm_card_wait_1_rp.visible = True
      self.gm_card_wait_1_rp.items = slots
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
          row2 = app_tables.step_done.get(game_id=cid, reg=reg)
          row2.update(p_step_done=1) ## all in the region are logged in
      else:
        alert("Unfortunately, someone claimed the role before you :( Please choose another one.")
        return False
    return True

  def get_runde(self, cid):
    row = app_tables.games_log.get(game_id=cid)
    r = row['gm_status']
    if r == 4:
      runde = 1
      yr = 2025
    elif r == 2:
      runde = 2
      yr = 2040
    elif r == 3:
      runde = 3
      yr = 2060
    elif r == 4:
      runde = 4
      yr = 2100
    else:
      print("runde is NOT in 1,2,3,4")
    return yr, runde

  def pcr_submit_click(self, **event_args):
    if self.pcr_rb_fut.selected:
      self.p_card_graf_dec.visible = False
    reg = mg.my_reg
    reglong = mg.reg_to_longreg[reg]
    role = mg.my_ministry
    rolelong = mg.ta_to_longmini[role]
    cid = mg.my_game_id
#    alert('reg is '+reg+' role is '+role)
    regs = mg.regs
    tas = mg.roles
    #tas = ['poverty', 'inequality', 'empowerment', 'food', 'energy', 'future']
    save_ok = self.save_player_choice(cid, role, reg)
    if save_ok:
      self.p_card_graf_dec.visible = True
      self.p_choose_role.visible = False
      self.dec_card.visible = False
      wrx = mg.regs.index(reg)
      wmx = mg.roles.index(role)
      self.pcgd_title.text = self.pcgd_title.text + ': ' +cid+'-'+str(wrx)+str(wmx)+',   '+reglong+',   '+rolelong
      your_game_id = cid + "-" + str(wrx) + str(wmx)
      congrats = "\n" + mg.pcr_submit_msg1 + rolelong + mg.pcr_submit_msg2 + reglong + ".\n" + mg.pcr_submit_msg3 + "\n" + your_game_id 
      mg.my_personal_game_id = your_game_id
      alert(congrats)

      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 1)
      self.pcgd_generating.visible = True
#      make something visible
      while not self.task.is_completed():
        pass
      else: ## background is done
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        if role == 'fut':
          self.card_fut.visible = True
          self.pcgd_info_rd1.content = mg.pcgd_rd1_info_short
          self.fut_info.content = mg.pcgd_rd1_info_fut_tx
        else:
          self.dec_card.visible = True
          self.pcgd_info_rd1.content = mg.pcgd_rd1_info_tx
        self.pcgd_info_rd1.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=1, reg=reg, ta=role)]
        self.plot_card_rp.items = slots

        ### get runde, yr
        yr, runde = self.get_runde(cid)
        anvil.server.call('budget_to_db', yr, cid)
        within_budget = False
        if role == 'fut':
          within_budget = self.do_future(cid, role, reg, runde, yr )
        else:
          self.do_non_future(cid, role, reg, runde, yr)      

  def show_hide_plots_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.show_hide_plots.visible = True
    self.show_hide_plots.selected = False
    self.show_hide_plots.text = mg.show_hide_plots_hide_tx
    if self.show_hide_plots.selected is False:
      pass
      
  def do_non_future(self, cid, role, reg, runde, yr):
    self.dec_card.visible = True
    self.pcgd_advance.visible = True
    pol_list = anvil.server.call('get_policy_budgets', reg, role, yr, cid)
#      print(pol_list)
    self.dec_rp.items = pol_list

  def check_all_colleagues_logged_in(self, cid, reg, runde):
    rows = app_tables.roles_assign.search(game_id=cid, reg=reg, round=runde, taken=1, role=q.not_('fut'))
    len_rows = len(rows)
    print(len_rows)
    if len(rows) == 32:
      return True
    else:
      return False
    
  def do_future(self, cid, role, reg, runde, yr):
    self.pcgd_advance.visible = False
    self.dec_card.visible = False
    self.card_fut.visible = True
    ## check if all your regional ministers have logged in
    all_colleauges_logged_in = self.check_all_colleagues_logged_in(cid, reg, runde)
    if not all_colleauges_logged_in:
      self.fut_not_all_logged_in.visible = True
      self.fut_bud_lb1.visible = False
      self.fut_bud_lb2.visible = False
      self.fut_but_lb3.visible = False
      self.fut_bud_amount.visible = False
      self.fut_invest.visible = False
      self.fut_invest_pct.visible = False
      self.refresh_numbers.visible = True
      self.submit_numbers.visible = False
      self.card_emp_fut.visible = False
      self.card_ener_fut.visible = False
      self.card_food_fut.visible = False
      self.card_ineq_fut.visible = False
      self.card_pov_fut.visible = False
    else:
      self.fut_not_all_logged_in.visible = False
      self.fut_bud_lb1.visible = True
      self.fut_bud_lb2.visible = True
      self.fut_but_lb3.visible = True
      self.fut_bud_amount.visible = True
      self.fut_invest.visible = True
      self.fut_invest_pct.visible = True
      self.refresh_numbers.visible = True
      self.submit_numbers.visible = True
      self.card_emp_fut.visible = True
      self.card_ener_fut.visible = True
      self.card_food_fut.visible = True
      self.card_ineq_fut.visible = True
      self.card_pov_fut.visible = True
      
      self.submit_numbers.visible = False
      f_bud_by_ta, fut_pov_list, fut_ineq_list, fut_emp_list, fut_food_list, fut_ener_list, within_budget = self.get_policy_investments(cid, role, reg, runde, yr)
      self.pov_rep_panel.visible = True
      self.tot_inv_pov.text = round(f_bud_by_ta['cpov'], 2)
      self.pov_rep_panel.items = fut_pov_list
      self.tot_inv_ineq.text = round(f_bud_by_ta['cineq'], 2)
      self.cpf_rp_ineq.items = fut_ineq_list    
      self.tot_inv_emp.text = round(f_bud_by_ta['cemp'], 2)
      self.cpf_rp_emp.items = fut_emp_list    
      self.tot_inv_food.text = round(f_bud_by_ta['cfood'], 2)
      self.cpf_food_rp.items = fut_food_list    
      self.tot_inv_ener.text = round(f_bud_by_ta['cener'], 2)
      self.cpf_ener_rp.items = fut_ener_list    
      if within_budget:
        self.submit_numbers.visible = True
      else:
        self.submit_numbers.visible = False
      return within_budget

  def calc_cost_home_tot(self, pct, tltl, gl, maxc):
    cost = 0
    for i in range(0, len(pct)):
      nw = pct[i] - tltl[i]
      nb = 0
      nt = gl[i] - tltl[i]
      pct_of_range = nw / (nt - nb)
      cost += maxc * pct_of_range
    return cost

  def calc_cost_home_ta(self, pct, tltl, gl, maxc, ta):
    # get_names
    if ta == 'pov':
      names = [r['name'] for r in app_tables.policies.search(ta='Poverty')]
    elif ta == 'ineq':
      names = [r['name'] for r in app_tables.policies.search(ta='Inequality')]
    elif ta == 'emp':
      names = [r['name'] for r in app_tables.policies.search(ta='Empowerment')]
    elif ta == 'food':
      names = [r['name'] for r in app_tables.policies.search(ta='Food')]
    elif ta == 'ener':
      names = [r['name'] for r in app_tables.policies.search(ta='Energy')]
    
    slots = []
    for i in range(0, len(pct)):
        nw = pct[i] - tltl[i]
        nb = 0
        nt = gl[i] - tltl[i]
        pct_of_range = nw / (nt - nb)
        cost = round(maxc * pct_of_range, 2)
        slot = {'pol_name' : names[i], 'pol_amount': cost}
        slots.append(slot)
    return slots

  def get_policy_investments(self, cid, role, reg, runde, yr):
    global budget
    pov_list = []
    pct_pov = [r['wert'] for r in app_tables.roles_assign.search(game_id=cid, role='pov', reg=reg, round=runde)]
    pct_ineq = [r['wert'] for r in app_tables.roles_assign.search(game_id=cid, role='ineq', reg=reg, round=runde)]
    pct_emp = [r['wert'] for r in app_tables.roles_assign.search(game_id=cid, role='emp', reg=reg, round=runde)]
    pct_food = [r['wert'] for r in app_tables.roles_assign.search(game_id=cid, role='food', reg=reg, round=runde)]
    pct_ener = [r['wert'] for r in app_tables.roles_assign.search(game_id=cid, role='ener', reg=reg, round=runde)]
    tltl_pov = [r['tltl'] for r in app_tables.policies.search(ta='Poverty')]
    gl_pov = [r['gl'] for r in app_tables.policies.search(ta='Poverty')]
    tltl_emp = [r['tltl'] for r in app_tables.policies.search(ta='Empowerment')]
    gl_emp = [r['gl'] for r in app_tables.policies.search(ta='Empowerment')]
    tltl_ineq = [r['tltl'] for r in app_tables.policies.search(ta='Inequality')]
    gl_ineq = [r['gl'] for r in app_tables.policies.search(ta='Inequality')]
    tltl_food = [r['tltl'] for r in app_tables.policies.search(ta='Food')]
    gl_food = [r['gl'] for r in app_tables.policies.search(ta='Food')]
    tltl_ener = [r['tltl'] for r in app_tables.policies.search(ta='Energy')]
    gl_ener = [r['gl'] for r in app_tables.policies.search(ta='Energy')]
    lb = app_tables.budget.get(reg=reg, game_id=cid, yr=yr)
    bud = lb['bud_all_tas']
    max_cost_pov = lb['c_pov']
    max_cost_food = lb['c_food']
    max_cost_ener = lb['c_ener']
    max_cost_ineq = lb['c_ineq']
    max_cost_emp = lb['c_emp']
    cost_pov = self.calc_cost_home_tot(pct_pov, tltl_pov, gl_pov, max_cost_pov)
    cost_emp = self.calc_cost_home_tot(pct_emp, tltl_emp, gl_emp, max_cost_emp)
    cost_ineq = self.calc_cost_home_tot(pct_ineq, tltl_ineq, gl_ineq, max_cost_ineq)
    cost_food = self.calc_cost_home_tot(pct_food, tltl_food, gl_food, max_cost_food)
    cost_ener = self.calc_cost_home_tot(pct_ener, tltl_ener, gl_ener, max_cost_ener)  
    costs_by_ta = {'cpov' : cost_pov, 'cfood' : cost_food, 'cemp': cost_emp, 'cineq' : cost_ineq, 'cener': cost_ener}
    total_cost = round(cost_pov + cost_emp + cost_ener + cost_food + cost_ineq, 2)
    pct_of_budget = total_cost / bud * 100
    self.fut_bud_amount.text = round(bud, 0)
    self.fut_invest.text = total_cost
    within_budget = False
    if pct_of_budget > 100:
      if pct_of_budget > 101:
        pct_shown = str(int(pct_of_budget))
      else:
        pct_shown = round(pct_of_budget, 1)
      self.fut_bud_amount.foreground = 'red'
      self.fut_invest.foreground = 'red'
      self.fut_invest_pct.foreground = 'red'
      self.fut_submit_all_pols.visible = False
    else:
      within_budget = True
      if pct_of_budget > 10:
        pct_shown = str(int(pct_of_budget))
      else:
        pct_shown = round(pct_of_budget, 1)
      self.fut_invest.foreground = 'green'
      self.fut_invest_pct.foreground = 'green'
      self.fut_bud_amount.foreground = 'green'
      self.submit_numbers.visible = True
    self.fut_invest_pct.text = pct_shown
    
    pov_list = self.calc_cost_home_ta(pct_pov, tltl_pov, gl_pov, max_cost_pov, 'pov')
    ineq_list = self.calc_cost_home_ta(pct_ineq, tltl_ineq, gl_ineq, max_cost_ineq, 'ineq')
    emp_list = self.calc_cost_home_ta(pct_emp, tltl_emp, gl_emp, max_cost_emp, 'emp')
    food_list = self.calc_cost_home_ta(pct_food, tltl_food, gl_food, max_cost_food, 'food')
    ener_list = self.calc_cost_home_ta(pct_ener, tltl_ener, gl_ener, max_cost_ener, 'ener')
    return costs_by_ta, pov_list, ineq_list, emp_list, food_list, ener_list, within_budget

  def refresh_numbers_click(self, **event_args):
    cid = mg.my_game_id
    role = 'fut'
    reg = mg.my_reg
    yr, runde = self.get_runde(cid)
    self.do_future(cid, role, reg, runde, yr)

  def all_reg_submitted(self, cid, step):
    rows = app_tables.step_done.search(game_id=cid, p_step_done=q.any_of(step, 99)
    if len(rows) == 10:
      return Tr
    pass

    
  def submit_numbers_click(self, **event_args):
    # Display a large popup with a title and three buttons.
    result = alert(content=mg.confirm_submit_tx,
               title=mg.confirm_title_tx,
               large=True,
               buttons= mg.confirm_buttons_tx
                  )
    if result == 'YES':
      my_cid = mg.my_personal_game_id
      print(my_cid)
#      cid = mg.my_game_id
#      print(cid)
      role = 'fut'
      reg = mg.my_reg
      print(reg)
      cid_cookie = anvil.server.call('get_game_id_from_cookie')
      print(cid_cookie)
      self.wait_for_run_after_submit.content = mg.after_submit_tx
      self.cid_reg_role_info.text = my_cid + '  + ' + mg.reg_to_longreg[reg] + '  - ' + mg.ta_to_longmini[role]
      self.card_fut.visible = False
      self.p_card_graf_dec.visible = False
      self.p_after_submit.visible = True
      
      rows = app_tables.game_files.search(game_id=cid_cookie)
      print(len(rows))
      if len(rows) == 0:
        msg = mg.p_advance_to_2_tx
        anvil.server.call('set_cookie_sub', 'r1', 1, cid_cookie)        
      elif len(rows) == 1:
        msg = mg.p_advance_to_3_tx

      self.p_advance_to_next_round.text = msg
      row2 = app_tables.step_done.get(game_id=cid_cookie, reg=reg)
      row2.update(p_step_done=2) ## the region submitted decisions for round 2025-2040

    else:
      n = Notification(mg.nothing_submitted_tx)
      n.show()
#      self.do_future(self, cid, role, reg, runde, yr)

  def gm_start_round_click(self, **event_args):
    ## first, check if all regions have submitted
    cid = mg.my_game_id
    yr, runde = self.get_runde(cid)
    row = app_tables.cookies.get(game_id=cid)
    if runde == 1:
      all_regs_submitted = (row['r1sub'] == 10)
      von = 2025
      bis = 2040
      row = app_tables.status.get(game_id=cid, game_status=1, p_status=0)
      row.update(game_status=2, p_status=1)
    elif runde == 2:
      all_regs_submitted = (row['r2sub'] == 10)
      von = 2040
      bis = 2060
      row = app_tables.status.get(game_id=cid, game_status=2, p_status=1)
      row.update(game_status=3, p_status=2)
    elif runde == 2:
      all_regs_submitted = (row['r3sub'] == 10)
      von = 2060
      bis = 2100
      row = app_tables.status.get(game_id=cid, game_status=3, p_status=2)
      row.update(game_status=4, p_status=3)
    print(runde)
    print(all_regs_submitted)
    self.gm_card_wait_1_info.visible = False
    if all_regs_submitted:
      self.gm_card_wait_1_temp_title.visible = False
      self.gm_card_wait_1_btn_check.visible = False
      self.gm_start_round.visible = False
      self.gm_card_wait_1_rp.visible = False
      self.gm_card_wait_1_info.text = mg.gm_wait_kickoff_r1_tx
      ## hide wait card
      self.card_fut.visible = False
      ## show run card
      self.wait_for_run_after_submit.content = mg.after_submit_tx
      self.wait_for_run_after_submit.visible = True
      ## update step done / status / others ???
      print("ln 686")
      print(cid)
      print(mg.my_reg)
      rows = app_tables.step_done.search(game_id=cid)
      for row in rows:
        if row['p_step_done'] == 2:
          row.update(p_step_done=3)  ## 3 = all regs submitted
      ## kickoff server run model
      n = Notification("off to run the model", timeout=4)
      n.show()
      self.task = anvil.server.call('launch_ugregmod', cid, von, bis)
#      make something visible
      while not self.task.is_completed(): # model still running
        pass
      else: ## model is done
        n= Notification("Model is done", timeout=3)
        n.show()
        self.gm_card_wait_1_info.text = mg.gm_wait_round_done_tx
        ### reset everything for next round ...
    else:  ## NOT all regs submitted
      n=Notification(mg.not_all_submitted_tx)
      n.show()

  def p_advance_to_next_round_click(self, **event_args):
    # Get the results until the end of the 
    """This method is called when the component is clicked."""
    cid = mg.my_game_id
    row = app_tables.status.get(game_id=cid)
    gm_status = row['gm_status']
    ## check if gm has set step_done gm_step_done to 2 (?)
    if gm_status == 1 or gm_status == 3:
      alert(mg.p_waiting_model_run_tx, title=mg.waiting_tx)
    ### prepare graphs and decisions for round 2 if gm_status == 2
    else:
      alert("not coded yet ...")

  def test_model_click(self, **event_args):
    n= Notification("off to run the model from test_model_click", timeout=4)
    n.show()
    cid = mg.my_game_id
    self.task = anvil.server.call('launch_ugregmod', cid, 2025, 2040)
#      make something visible
    while not self.task.is_completed(): # model still running
      pass
    else: ## model is done
      Notification("Model is done", timeout=7)

  def get_sorted_pol_list(self, runde, pol):
    r_to_x = {
      'us' : 0, 'af' : 1, 'cn' : 2, 'me' : 3, 'sa' : 4, 'la' : 5,
      'pa' : 6, 'ec' : 7, 'eu' : 8, 'se' : 9
    }
    rows = app_tables.roles_assign.search(round=runde, pol=pol) # in production also use game_id
    dic = {}
    for row in rows:
      rreg2 = r_to_x[row['reg']]
      dic[rreg2] = row['wert']
    myKeys = list(dic.keys())
    myKeys.sort()
    sd = {i: dic[i] for i in myKeys}
    pol_list = list(sd.values())
    return pol_list

  def randval(self, p, pl):
    pass

  def get_randGLbias_for_pol(self, pol, pl, tl, gl):
    idx = pl.index(pol)
    gle = gl[idx]
    tle = tl[idx]
#    avg = tle + (gle -tle) / 2
#    w = random.uniform(avg, gle)
    floor = tle 
    mid = (gle - tle ) / 2
    w = random.uniform(floor + mid, gle)
    if w < floor or w > gle:
      oops = 2
    print(pol+' min='+str(tle)+' max='+str(gle)+' wert='+str(w))
    return w

  def test_model_top_click(self, **event_args):
    ## clear db
    app_tables.cookies.delete_all_rows()
    app_tables.state_of_play.delete_all_rows()
    app_tables.step_done.delete_all_rows()
    app_tables.roles_assign.delete_all_rows()
    rows = app_tables.games_log.search(game_id=q.not_("TEST"))
    for row in rows:
      row.delete()

  def dropdown_menu_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.dropdown_menu_1.selected_value == 1:
      print(self.dropdown_menu_1.selected_value)      
      app_tables.game_files.delete_all_rows()
      von = 2025
      bis = 2040
    elif self.dropdown_menu_1.selected_value == 2:
      print(self.dropdown_menu_1.selected_value)       
      von = 2040
      bis = 2060
    else:
      print(self.dropdown_menu_1.selected_value)       
      von = 2060
      bis = 2100
    cid = mg.my_game_id
    cid = "QTO-53"
    anfang = time.time()
    self.yr_from_mod.visible = True
    self.task = anvil.server.call('launch_ugregmod', cid, von, bis)
#      make something visible
    while not self.task.is_completed(): # model still running
      yr = self.task.get_state(['Year'])
      self.yr_from_mod.text = yr
      pass
    else: ## model is done
      self.yr_from_mod.visible = False
      ende = time.time()
      dauer = round(ende - anfang, 0)
      abc = 'Using ' +str(dauer)+' sec to run the model successfully from '+str(von)+' to '+str(bis)
      alert(abc)
      self.card_test_plot.visible = True
      anvil.server.call('fill_test_plots', self.dropdown_menu_1.selected_value, "QTO-53")
      slots = [{key: r[key] for key in ["title", "fig1"]} for r in app_tables.test_plots.search(game_id= cid)]
      self.card_test_plot_rp.items = slots

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    dummy=anvil.server.call('fe_keepalive')
    

  def pcgd_advance_click(self, **event_args):
    ## this is a player (NOT fut) who wants to know if ready for next round
    ## first, check if all regions have submitted
    cid = mg.my_game_id
    yr, runde = self.get_runde(cid)
    row = app_tables.cookies.get(game_id=cid)
    if runde == 1:
      all_regs_submitted = (row['r1sub'] == 10)
    if not all_regs_submitted:
      n=Notification(mg.not_all_submitted_p_tx, timeout=5, title=mg.waiting_tx, style="info")
      n.show()
    else:
      ## get info for next round
#      self.gm_card_wait_1_btn_check.visible = False
#      self.gm_start_round = False
#      self.gm_card_wait_1_rp.visible = False
#      self.gm_card_wait_1_info.text = mg.gm_wait_kickoff_r1_tx
#      ## hide wait card
#      self.card_fut.visible = False
#      ## show run card
#      self.wait_for_run_after_submit.content = mg.after_submit_tx
#      self.wait_for_run_after_submit.visible = True
#      ## update step done / status / others ???
#      row = app_tables.step_done.get(game_id=cid, reg=mg.my_reg)
#      row.update(p_step_done=2)
#      ## kickoff server run model
#      n = Notification("off to run the model", timeout=4)
#      n.show()
#      self.task = anvil.server.call('launch_ugregmod', cid, 2025, 2040)
#      make something visible
      while not self.task.is_completed(): # model still running
        pass
      else: ## model is done
        n= Notification("Model is done", timeout=7)
        n.show()
        ### reset everything for next round ...

  def tick_refresh_fut_tick(self, **event_args):
    if not self.tick_refresh_fut.interval == 0:
      cid = mg.my_game_id
      reg = mg.my_reg
      yr, runde = self.get_runde(cid)    
      if len(app_tables.roles_assign.get(game_id=cid,reg='fut', round=runde, taken=1)) == 1:
        self.fut_not_all_logged_in.visible = True
        self.do_future(cid, 'fut', reg, runde, yr)
      else:
        self.fut_not_all_logged_in.visible = True
    else:
      self.tick_refresh_fut.interval = 52
      

      

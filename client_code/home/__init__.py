from ._anvil_designer import homeTemplate
from anvil import *
from .. import mg
from .. import lu
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
    self.tick_gm_round_ready.interval = 0
    self.timer_1.interval = 15227
    self.timer_1_tick()
#    app_tables.cookies.delete_all_rows()
#    app_tables.state_of_play.delete_all_rows()
#    app_tables.step_done.delete_all_rows()
#    app_tables.roles_assign.delete_all_rows()
    my_loc, my_loc2 = anvil.server.call('get_locale')
#    self.show_text.text = my_loc + ' ' + my_loc2
    my_loc = 'en'
    if my_loc == 'en':
      t1 = ("English", 0)
      t2 = ("Deutsch - Sie", 1)
      t3 = ("Deutsch - Du", 2)
      t4 = ("Français", 3)
      t5 = ("Norsk-Bokmål", 4)
      my_lox = 0
      self.lang_dd_menu.label = "Change the language"
      self.lang_dd_menu.placeholder = "English"
    elif my_loc == 'de':
      t3 = ("English", 0)
      t1 = ("Deutsch - Sie", 1)
      t2 = ("Deutsch - Du", 2)
      t4 = ("Français", 3)
      t5 = ("Norsk-Bokmål", 4)
      my_lox = 1      
      self.lang_dd_menu.label = "Ändern Sie die Sprache"
      self.lang_dd_menu.placeholder = "Deutsch-Sie"
    elif my_loc == 'fr':
      t2 = ("English", 0)
      t3 = ("Deutsch - Sie", 1)
      t4 = ("Deutsch - Du", 2)
      t1 = ("Français", 3)
      t5 = ("Norsk-Bokmål", 4)
      my_lox = 3
      self.lang_dd_menu.label = "Modifier la langue"
      self.lang_dd_menu.placeholder = "Français"
    elif my_loc == 'no':
      t2 = ("English", 0)
      t3 = ("Deutsch - Sie", 1)
      t4 = ("Deutsch - Du", 2)
      t5 = ("Français", 3)
      t1 = ("Norsk-Bokmål", 4)
      my_lox = 4      
      self.lang_dd_menu.label = "Endre språk"
      self.lang_dd_menu.placeholder = "Norsk-Bokmål"
    else:
      t1 = ("English", 0)
      t2 = ("Deutsch - Sie", 1)
      t3 = ("Deutsch - Du", 2)
      t4 = ("Français", 3)
      t5 = ("Norsk-Bokmål", 4)
      my_lox = 0
      self.lang_dd_menu.label = "Change the language"
  
    self.lang_dd_menu.items = [t1, t2, t3, t4, t5]
    mg.my_lang = my_lox
    self.top_title.text = lu.top_title_str[my_lox]
    self.top_btn_help.text = lu.top_btn_help_str[my_lox]
    self.top_btn_thanks.text = lu.top_btn_thanks_str[my_lox]
    self.top_btn_poc.text = "PoC"
    self.credits.text = lu.credits_btn_tx_str[my_lox]
    self.lang_rich_tx.content = lu.lang_info_str[my_lox]
    self.lang_lets_go.text = lu.lang_lets_go_tx[my_lox]
    if my_lox == 3:
      alert("Les textes en français proviennent de google. Aidez-nous à les améliorer.", title="Pardon")
    elif my_lox == 4:
      alert("De norske tekstene kommer fra google. Vennligst hjelp oss med å forbedre dem.", title="Unnskyld")
    elif my_lox == 2:
      alert("Wir haben die Texte und Aufforderungen noch nicht in das informelle Deutsch übersetzt. Solange nutzen wir die formelle 'Sie' Form. Wenn Du helfen möchtest, lass uns das wissen.", title="Entschuldige")
    elif my_lox > 4:
      alert("We have not yet translated the texts and prompts to your language. If you want to help, please get in touch.", title="Apologies")

  def lang_dd_menu_change(self, **event_args):
    print(self.lang_dd_menu.selected_value)
    """This method is called when an item is selected"""
    print(self.lang_dd_menu.selected_value)
    mg.my_lang = int(self.lang_dd_menu.selected_value)
    my_lox = mg.my_lang
    print('my_lox ' + str(my_lox))
    print(lu.lang_avail_items[my_lox])
    self.lang_dd_menu.placeholder = lu.lang_avail_items[my_lox]
    self.top_title.text = lu.top_title_str[my_lox]
    self.top_btn_help.text = lu.top_btn_help_str[my_lox]
    self.top_btn_thanks.text = lu.top_btn_thanks_str[my_lox]
    self.top_btn_poc.text = "PoC"
    self.credits.text = lu.credits_btn_tx_str[my_lox]
    self.lang_rich_tx.content = lu.lang_info_str[my_lox]
    self.lang_lets_go.text = lu.lang_lets_go_tx[my_lox]
#    self.lang_dd_menu.items = lu.lang_avail_items
    self.lang_rich_tx.content = lu.lang_info_str[my_lox]
    self.lang_dd_menu.label = lu.lang_dd_menu_tx_str[my_lox]

    if my_lox == 3:
      alert("Les textes en français proviennent de google. Aidez-nous à les améliorer.", title="Pardon")
    elif my_lox == 4:
      alert("De norske tekstene kommer fra google. Vennligst hjelp oss med å forbedre dem.", title="Unnskyld")
    elif my_lox == 2:
      alert("Wir haben die Texte und Aufforderungen noch nicht in das informelle Deutsch übersetzt. Solange nutzen wir die formelle 'Sie' Form. Wenn Du helfen möchtest, lass uns das wissen.", title="Entschuldige")
    elif my_lox > 4:
      alert("We have not yet translated the texts and prompts to your language. If you want to help, please get in touch.", title="Apologies")

  """
  my_loc = mg.my_lang
  top_thanks_msg = lu.top_btn_thanks_str[my_loc]
  top_thanks_title = mg.top_thanks_title_en
    top_btn_help.text = mg.top_btn_help_en
    top_btn_thanks.text = mg.top_btn_thanks_en
    top_btn_poc.text = 'PoC'
    top_join_game.text = mg.top_join_game_en
    top_start_game.text = mg.top_start_game_en
    p_lb_choose_game.text = mg.p_lb_choose_game_en
    p_btn_select_game.text = mg.p_btn_select_game_en
    gm_board.text = mg.msg_gm_board_en
    gm_board_info.content = mg.msg_gm_board_info_en
    cb_af.text = mg.cb_af_tx_en
    cb_us.text = mg.cb_us_tx_en
    cb_cn.text = mg.cb_cn_tx_en
    cb_me.text = mg.cb_me_tx_en
    cb_sa.text = mg.cb_sa_tx_en
    cb_la.text = mg.cb_la_tx_en
    cb_pa.text = mg.cb_pa_tx_en
    cb_ec.text = mg.cb_ec_tx_en
    cb_eu.text = mg.cb_eu_tx_en
    cb_se.text = mg.cb_se_tx_en
    gm_reg_npbp.text = mg.gm_reg_npbp_tx_en
    gm_card_wait_1_info.content = mg.gm_card_wait_1_info_tx_en
    gm_card_wait_1_btn_check.text = mg.gm_card_wait_1_btn_check_tx_en
    gm_start_round.text = mg.gm_card_wait_1_btn_kick_off_round_1_tx_en
    setup_npbp_label.text = mg.setup_npbp_label_tx_en
    pcr_rb_af.text = mg.cb_af_tx_en
    pcr_rb_us.text = mg.cb_us_tx_en
    pcr_rb_cn.text = mg.cb_cn_tx_en
    pcr_rb_me.text = mg.cb_me_tx_en
    pcr_rb_sa.text = mg.cb_sa_tx_en
    pcr_rb_la.text = mg.cb_la_tx_en
    pcr_rb_pa.text = mg.cb_pa_tx_en
    pcr_rb_ec.text = mg.cb_ec_tx_en
    pcr_rb_eu.text = mg.cb_eu_tx_en
    pcr_rb_se.text = mg.cb_se_tx_en
    pcr_rb_pov.text = mg.cb_pov_tx_en
    pcr_rb_ineq.text = mg.cb_ineq_tx_en
    pcr_rb_emp.text = mg.cb_emp_tx_en
    pcr_rb_food.text = mg.cb_food_tx_en
    pcr_rb_ener.text = mg.cb_ener_tx_en
    pcr_rb_fut.text = mg.cb_fut_tx_en
    pcr_title.text = mg.pcr_title_tx_en
    pcr_col_left_title.text = mg.pcr_col_left_title_tx_en
    pcr_col_right_title.text = mg.pcr_col_right_title_tx_en
    pcr_submit.text = mg.pcr_submit_tx_en
    fut_not_all_logged_in.text = mg.fut_not_all_logged_in_tx_en
      #    self.pcr_submit_msg1.text = mg.pcr_submit_msg1
      #    self.pcr_submit_msg2.text = mg.pcr_submit_msg2
    pcgd_title.text = mg.pcr_title_tx_en
    pcgd_info_rd1.content = mg.pcgd_rd1_info_tx_en
    pcgd_generating.text = mg.pcgd_generating_tx_en
    dec_info.content = mg.dec_info_tx_en
    dec_title.text = mg.dec_title_tx_en
    pcgd_advance.text = mg.pcgd_advance_tx_en
    refresh_numbers.text = mg.refresh_numbers_tx_en
    submit_numbers.text = mg.submit_numbers_tx_en
    fut_info.content = mg.fut_info_tx_en
    fut_bud_lb1.text = mg.fut_bud_lb1_tx_en
    fut_bud_lb2.text = mg.fut_bud_lb2_tx_en 
    fut_but_lb3.text = mg.fut_bud_lb3_tx_en 
    cpf_lb.text = mg.cfpov_tx_en
    cpf_lb2.text = mg.cfpov_lb_tx_en 
    cpf_ineq_lb.text = mg.cfineq_tx_en
    cpf_ineq_lb2.text = mg.cfineq_lb_tx_en 
    cpf_emp_lb.text = mg.cfemp_tx_en
    cpf_emp_lb2.text = mg.cfemp_lb_tx_en 
    cpf_food_lb.text = mg.cffood_tx_en
    cpf_food_lb2.text = mg.cffood_lb_tx_en 
    cpf_ener_lb.text = mg.cfener_tx_en
    cpf_ener_lb2.text = mg.cfener_lb_tx_en 
    gm_card_wait_1_temp_title.text = mg.gm_card_wait_1_temp_title_tx_en
    credits.text = mg.credits_btn_tx_en
  """  
  def top_btn_thanks_click(self, **event_args):
    my_lox = mg.my_lang
    alert(content=lu.top_thanks_msg_str[my_lox], title=lu.top_thanks_title_str[my_lox], large=True)

  def top_btn_poc_click(self, **event_args):
    alert("Neither the user interface nor the server code is elegant, nor efficient, nor 'pythonic'. Contact us if you can help making anything better.",
         title="So far, this app is a Proof of Concept")

  def top_btn_help_click(self, **event_args):
    my_lox = mg.my_lang
    webbrowser.open_new("http://sdggamehelp.blue-way.net")

  def top_start_game_click(self, **event_args):
    my_lox = mg.my_lang
    t = TextBox(placeholder=lu.enter_code_tx[my_lox])
    alert(content=t,
          title=lu.enter_code_title_tx[my_lox])
    print(f"You entered: {t.text}")
    code = t.text.upper()
    if not code == 'LTG-ND':
      alert(lu.wrong_code_tx[my_lox])
      return
      pass
    with Notification("Clearing DBs ..."):
      self.test_model_top_click() ## clearind DBs at the start
    game_id = anvil.server.call('generate_id')
    anvil.server.call('budget_to_db', 2025, game_id)
    app_tables.cookies.add_row(game_id=game_id, r1sub=0, r2sub=0, r3sub=0,gm_step=0) ## clean slate
    self.top_start_game.visible = False
    self.top_join_game.visible = False
    mg.my_game_id = game_id
    jetzt = datetime.datetime.now()
    app_tables.games_log.add_row(game_id=game_id, gm_status=1, started=jetzt)
    self.tick_gm_round_ready.interval = 0
    # self.tick_gm_round_ready_tick()
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

  def check_rnsub(self, cid):
    ## ToDo
    ## in production switch first true and false and handle in top_join_game_click
    row = app_tables.cookies.get(game_id=cid)
    if row['r1sub'] < 10 or row['r2sub'] < 10 or row['r3sub'] < 10:
      return True 
    else:
      return True
  
  def any_open_games(self, g_nbr):
    rows = app_tables.games_log.search()
    open_games = []
    for i in range(1,g_nbr):
      if rows[i]['closed'] == None:
        cid = rows[i]['game_id']
        if self.check_rnsub(cid):
          open_games.append(cid)
    return len(open_games), open_games

  def top_join_game_click(self, **event_args):
    rows = app_tables.games_log.search()
    if len(rows) == 1 and rows[0]['game_id'] == 'TEST':
      n = Notification(mg.no_active_game_to_join_tx, timeout=7, title='Ooopps...')
      n.show()
      return
    lenopen, open = self.any_open_games(len(rows))
    if lenopen == 0:
      n = Notification(mg.no_active_game_to_join_tx, timeout=7, title='Ooops...')
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
      self.gm_start_round.visible = True
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
    elif r == 6:
      runde = 2
      yr = 2040
    elif r == 10:
      runde = 3
      yr = 2060
    elif r == 12:
      runde = 4
      yr = 2100
    else:
      return 123, 999
    return yr, runde

  def pcr_submit_click(self, **event_args):
    anfang = time.time()
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
      mg.fut_title_tx2 = self.pcgd_title.text
      your_game_id = cid + "-" + str(wrx) + str(wmx)
      congrats = mg.pcr_submit_msg1 + rolelong + mg.pcr_submit_msg2 + reglong + ".\n" + mg.pcr_submit_msg3 + "\n" + your_game_id 
      mg.my_personal_game_id = your_game_id
      alert(congrats, title=mg.pcr_submit_title)
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 1)
      self.pcgd_generating.visible = True
#      make something visible
      while not self.task.is_completed():
        pass
      else: ## background is done
        ### get runde, yr
        yr, runde = self.get_runde(cid)
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
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        if role == 'fut':
          self.do_future(cid, role, reg, runde, yr )
        else:
          pass ## dont show policies on last round
          self.do_non_future(cid, role, reg, runde, yr)      
    dauer = round(time.time() - anfang, 0)
    self.top_duration.text = dauer

  def show_hide_plots_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.show_hide_plots.visible = True
    self.show_hide_plots.selected = False
    self.show_hide_plots.text = mg.show_hide_plots_hide_tx
    if self.show_hide_plots.selected is False:
      pass
      
  def do_non_future(self, cid, role, reg, runde, yr):
    print("in do_NON_future ie TAs "+cid+' '+reg+' '+role+' '+str(runde)+' '+str(yr))
    if yr == 2100:
      return
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
    print("in do_future "+cid+' '+reg+' '+role+' '+str(runde)+' '+str(yr))
    self.pcgd_advance.visible = False
    self.dec_card.visible = False
    self.card_fut.visible = True
    ## check if all your regional ministers have logged in
    ## ToDo when game is restarted from suspension this must be done differently.
    if runde == 1:
      all_colleauges_logged_in = self.check_all_colleagues_logged_in(cid, reg, runde)
    else:
      all_colleauges_logged_in = True
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
      self.pcgd_plot_card.visible = True
      self.submit_numbers.visible = False
      if not yr == 2100:
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
      return True 

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
    rows = app_tables.step_done.search(game_id=cid, p_step_done=q.any_of(step, 99))
    if len(rows) == 10:
      return True 
    else:
      return False
    
  def submit_numbers_click(self, **event_args):
    # First, confirm submission
    result = alert(content=mg.confirm_submit_tx,
               title=mg.confirm_title_tx,
               large=True,
               buttons= mg.confirm_buttons_tx
                  )
    if result == 'NO':
      n = Notification(mg.nothing_submitted_tx)
      n.show()
    else: ## submission confirmed, reg DID submit numbers
      my_cid = mg.my_personal_game_id
#      print(my_cid)
      cid = mg.my_game_id
#      print(cid)
      yr, runde = self.get_runde(cid)
      print("--------")
      print("submit_numbers_click "+str(yr)+' '+str(runde))
      role = 'fut'  ## we're in the Future TA
      reg = mg.my_reg
#      print(reg)
      row = app_tables.step_done.get(game_id=cid, reg=reg)
      pStepDone = row['p_step_done']
      cid_cookie = anvil.server.call('get_game_id_from_cookie')
      print(cid_cookie)
      ## show confirmation alert
      self.cid_reg_role_info.text = my_cid + '  + ' + mg.reg_to_longreg[reg] + '  - ' + mg.ta_to_longmini[role]
      self.card_fut.visible = False
      self.p_card_graf_dec.visible = False
      self.p_after_submit.visible = True
      ## bump cookie for this round r_sub by one
      all_regs_sub = False
      if runde == 1:
        print("submit_numbers bump cookie runde="+str(runde))
        anvil.server.call('set_cookie_sub', 'r1', 1, cid_cookie) 
        rc = app_tables.cookies.get(game_id=cid_cookie)
        if rc['r1sub'] == 10:
          all_regs_sub = True
      elif runde == 2:
        print("submit_numbers bump cookie runde="+str(runde)+' '+cid_cookie)
        anvil.server.call('set_cookie_sub', 'r2', 1, cid_cookie)        
        rc = app_tables.cookies.get(game_id=cid_cookie)
        if rc['r2sub'] == 10:
          all_regs_sub = True
      elif runde == 3:
        print("submit_numbers bump cookie runde="+str(runde))
        anvil.server.call('set_cookie_sub', 'r3', 1, cid_cookie)        
        rc = app_tables.cookies.get(game_id=cid_cookie)
        if rc['r3sub'] == 10:
          all_regs_sub = True
      ### update steps

      if not all_regs_sub: ## there is at least one region (of players) that has not yet submitted
        row2 = app_tables.step_done.get(game_id=cid_cookie, reg=reg)
        if runde == 1:
          row2.update(p_step_done=3) ## the region submitted decisions for round 2025-2040
        elif runde == 2:
          row2.update(p_step_done=5) ## the region submitted decisions for round 2040- 2060
        elif runde == 3:
          row2.update(p_step_done=7) ## the region submitted decisions for round 2060 - 2100
        n = Notification(mg.not_all_submitted_p_tx, timeout=7)
        n.show() 
      else:  ## all HAVE submitted
        row = app_tables.games_log.get(game_id=cid_cookie)
        print("in submit_numbers_click, all HAVE sub gmStatus "+str(row['gm_status']))
        rc = app_tables.cookies.get(game_id=cid_cookie)
        print("rXsub " + str(rc['r1sub']) + ' ' + str(rc['r2sub']) + ' ' + str(rc['r3sub']) + ' ')
        if row['gm_status'] == 4:
          row['gm_status'] = 5 ## off to run 2025 to 2040
        if row['gm_status'] == 6:
          row['gm_status'] = 7 ## all regs submitted for 2040 to 2060
        if row['gm_status'] == 9:
          row['gm_status'] = 10 ## all regs submitted for 2060 to 2100
        rg = app_tables.games_log.get(game_id=cid_cookie)
        print("in submit_numbers_click, updated gmStatus "+str(rg['gm_status']))
        n = Notification(mg.all_submitted_p_tx, timeout=7)
        n.show()
        self.test_model.visible = False  ## this is a debug button
        ## give feedback
        ## after_submit_tx = "Your region's decisions have been submitted - thanks!\nOnce all regions have submitted their decisons, the model will be advanced for the next round. This will take a bit of time ..."
        self.card_fut.visible = False
        self.p_after_submit.visible = True
        self.wait_for_run_after_submit.content = mg.after_submit_tx
        if runde == 1:
          # p_advance_to_next_round_tx = "Get the results until 2040 and the decision sheet for 2040-2060 - your children's future"
          self.p_advance_to_next_round.text = mg.p_advance_to_next_round_tx
        elif runde == 2:
          # p_advance_to_1_tx = "Get the results until 2060 and the decision sheet for 2060-210 - your grandchildren's future"
          self.p_advance_to_next_round.text = mg.p_advance_to_1_tx
        elif runde == 3:
          # p_advance_to_2_tx = "Get the results until the end of the century"
          self.p_advance_to_next_round.text = mg.p_advance_to_2_tx
#p_waiting_model_run_tx = "... still waiting for the GM to advance the model ..."
#waiting_tx = "Waiting ..."

  def gm_start_round_click(self, **event_args):
    ## first, check if all regions have submitted
    self.gm_card_wait_1_rp.visible = False
    self.gm_wait_kickoff_r1.visible = False
    self.gm_wait_kickoff_r1_rp.visible = False
    self.gm_start_round.visible = False
    cid_cookie = anvil.server.call('get_game_id_from_cookie')
    print("gm_start_round_click "+ str(cid_cookie))
    row = app_tables.games_log.get(game_id=cid_cookie)
    if row['gm_status'] not in [5,7,10]:
#    if row['gm_status'] == 4: ## waiting for submissions for all regions for 2025 to 2040
      n = Notification(mg.not_all_submitted_gm_tx, timeout=7)
      n.show()
      return
    if row['gm_status'] == 5: ## 2025 to 2040 ready
      von = 2025
      bis = 2040
      runde = 1
    elif row['gm_status'] == 6:
      n = Notification(mg.gm_wait_sub2_tx, title=mg.waiting_tx, style="warning")
      n.show()
      return
    elif row['gm_status'] == 7:
      von = 2040
      bis = 2060
      runde = 2
    elif row['gm_status'] == 10:
      von = 2060
      bis = 2100
      runde = 3
    else:
      abc = str(row['gm_status'])
      abc2 = "row['gm_status'] not correct " + abc
      alert(abc2)
      return
    self.gm_card_wait_1_info.visible = True
    # running_model_tx = "... advancing the model ..."
    # gm_wait_round_started_tx = 'The model has been started. Please wait until the simulation is done...'
    self.gm_card_wait_1_info.content = mg.gm_wait_round_started_tx
    self.gm_card_wait_1_temp_title.visible = False
    self.gm_card_wait_1_btn_check.visible = False
    self.gm_start_round.visible = False
    self.gm_card_wait_1_rp.visible = False
    self.gm_wait_kickoff_r1_rp.visible = False
    self.task = anvil.server.call('launch_ugregmod', cid_cookie, von, bis)
#      make something visible
    while not self.task.is_completed(): # model still running
      pass
    else: ## model is done
      # gm_wait_round_done_tx = 'The model has been advanced. Tell your players to click on the Start next round button.'
      self.gm_card_wait_1_info.content = mg.gm_wait_round_done_tx
      time.sleep(2)
      self.gm_card_wait_1_info.content = mg.gm_wait_round_done_tx2
      row = app_tables.games_log.get(game_id=cid_cookie)
      if runde == 1:
        row['gm_status'] = 6 ## first round successfully done
        self.gm_start_round.visible = True
        self.gm_start_round.text = mg.gm_start_round_tx_2
        anvil.server.call('budget_to_db', 2040, cid_cookie)
      elif runde == 2:
        self.gm_start_round.visible = True
        row['gm_status'] = 10
        self.gm_start_round.text = mg.gm_start_round_tx_3
        anvil.server.call('budget_to_db', 2060, cid_cookie)
        print("gm_start_round:: "+str(runde)+' gm_status=10')
      elif runde == 3:
        self.gm_card_wait_1_info.content = mg.gm_wait_round_done_tx3
        self.gm_start_round.visible = False
        row['gm_status'] = 12
        self.gm_start_round.text = mg.gm_start_round_tx_3
#        anvil.server.call('budget_to_db', 2100, cid_cookie)
        print("gm_start_round:: "+str(runde)+' gm_status=12')

  def p_advance_to_next_round_click(self, **event_args):
    # Get the results until the end of the for FUT
    cid = mg.my_game_id
    row = app_tables.games_log.get(game_id=cid)
    print("in p_advance_to_next_round_click")
    print("in p_advance_to_next_round_click -> 3rd line "+cid+' fut '+mg.my_reg+' '+str(row['gm_status']))
    if row['gm_status'] == 5:
      alert(mg.p_waiting_model_run_tx, title=mg.waiting_tx)
    ### prepare graphs and decisions for round 2 if gm_status == 2
    elif row['gm_status'] == 6: ## 2025 to 2040 successfully run
      reg = mg.my_reg
      runde = 2
      yr = 2040
      print("in p_advance_to_next_round_click -> do_future with "+cid+' fut '+reg+' '+str(runde)+' '+str(yr))
      self.p_card_graf_dec.visible = True
      self.p_choose_role.visible = False
      self.dec_card.visible = False
      self.p_after_submit.visible = False
      role = 'fut'
      self.pcgd_title.text = mg.fut_title_tx2
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 2)
      self.pcgd_generating.visible = True
      #      make something visible
      while not self.task.is_completed():
        pass
      else: ## background is done
        ### get runde, yr
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        self.card_fut.visible = True
        self.pcgd_info_rd1.content = mg.pcgd_rd1_info_short
        self.fut_info.content = mg.pcgd_rd1_info_fut_tx
        self.pcgd_info_rd1.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        self.do_future(cid, role, reg, runde, yr )
    elif row['gm_status'] == 10: ## 2040 to 2060 successfully run
      reg = mg.my_reg
      runde = 3
      yr = 2060
      print("in p_advance_to_next_round_click -> do_future with "+cid+' fut '+reg+' '+str(runde)+' '+str(yr))
      self.p_card_graf_dec.visible = True
      self.p_choose_role.visible = False
      self.dec_card.visible = False
      self.p_after_submit.visible = False
      role = 'fut'
      self.pcgd_title.text = mg.fut_title_tx2
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 3)
      self.pcgd_generating.visible = True
      #      make something visible
      while not self.task.is_completed():
        pass
      else: ## background is done
        ### get runde, yr
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        self.card_fut.visible = True
        self.pcgd_info_rd1.content = mg.pcgd_rd1_info_short
        self.fut_info.content = mg.pcgd_rd1_info_fut_tx
        self.pcgd_info_rd1.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        self.do_future(cid, role, reg, runde, yr )
    elif row['gm_status'] == 12: ## 2060 to 2100 successfully run
      reg = mg.my_reg
      runde = 4
      yr = 2100
      print("in p_advance_to_next_round_click -> do_future with "+cid+' fut '+reg+' '+str(runde)+' '+str(yr))
      self.p_card_graf_dec.visible = True
      self.p_choose_role.visible = False
      self.dec_card.visible = False
      self.card_fut.visible = False
      self.p_after_submit.visible = False
      role = 'fut'
      self.pcgd_title.text = mg.fut_title_tx2
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 4)
      self.pcgd_generating.visible = True
      #      make something visible
      while not self.task.is_completed():
        pass
      else: ## background is done
        ### get runde, yr
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        self.card_fut.visible = False ## no more budget at the end
        self.pcgd_info_rd1.content = mg.pcgd_rd1_info_end
        self.fut_info.content = mg.pcgd_rd1_info_end_tx
        self.pcgd_info_rd1.visible = True
        self.fut_detail('hide')
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        self.do_future(cid, role, reg, runde, yr )
        self.fut_detail('hide')

  def fut_detail(self, hs):
    if hs == 'hide':
      self.card_emp_fut.visible = False
      self.card_ener_fut.visible = False
      self.card_food_fut.visible = False
      self.card_ineq_fut.visible = False
      self.card_pov_fut.visible = False
      self.fut_bud_lb1.visible = False
      self.fut_bud_lb2.visible = False
      self.fut_but_lb3.visible = False
      self.fut_bud_amount.visible = False
      self.fut_invest.visible = False
      self.fut_invest_pct.visible = False
      self.refresh_numbers.visible = False
    else:
      self.card_emp_fut.visible = True 
      self.card_ener_fut.visible = True
      self.card_food_fut.visible = True
      self.card_ineq_fut.visible = True
      self.card_pov_fut.visible = True
      self.fut_bud_lb1.visible = True
      self.fut_bud_lb2.visible = True
      self.fut_but_lb3.visible = True
      self.fut_bud_amount.visible = True
      self.fut_invest.visible = True
      self.fut_invest_pct.visible = True
      self.refresh_numbers.visible = True
      
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
#    print(pol+' min='+str(tle)+' max='+str(gle)+' wert='+str(w))
    return w

  def test_model_top_click(self, **event_args):
    ## clear db
    app_tables.cookies.delete_all_rows()
    app_tables.state_of_play.delete_all_rows()
    app_tables.step_done.delete_all_rows()
    app_tables.roles_assign.delete_all_rows()
    app_tables.game_files.delete_all_rows()
    app_tables.plots.delete_all_rows()
    rows = app_tables.games_log.search(game_id=q.not_("TEST"))
    for row in rows:
      row.delete()

  def lang_dd_menu_changeOLD(self, **event_args):
    """This method is called when an item is selected"""
    if self.lang_dd_menu.selected_value == 1: ## english
      pass
    if self.lang_dd_menu.selected_value == 1:
      print(self.lang_dd_menu.selected_value)      
      app_tables.game_files.delete_all_rows()
      von = 2025
      bis = 2040
    elif self.lang_dd_menu.selected_value == 2:
      print(self.lang_dd_menu.selected_value)       
      von = 2040
      bis = 2060
    else:
      print(self.lang_dd_menu.selected_value)       
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
      anvil.server.call('fill_test_plots', self.lang_dd_menu.selected_value, "QTO-53")
      slots = [{key: r[key] for key in ["title", "fig1"]} for r in app_tables.test_plots.search(game_id= cid)]
      self.card_test_plot_rp.items = slots

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    dummy=anvil.server.call_s('fe_keepalive')

  def all_submit(self, cid, runde):
    rowc = app_tables.cookies.get(game_id=cid)
    if runde == 1:
      if rowc['r1sub'] == 10:
        return True 
      else:
        return False 
    if runde == 2:
      if rowc['r2sub'] == 10:
        return True 
      else:
        return False 
    if runde == 3:
      if rowc['r3sub'] == 10:
        return True 
      else:
        return False 
        
  def my_all_submit(self, reg, round):
    ## a dead def, never called
    cid = mg.my_game_id
    reg = mg.my_reg
    row = app_tables.games_log.get(game_id=cid)
    rowc = app_tables.cookies.get(game_id=cid)
    rowp = app_tables.step_done.get(game_id=cid, reg=reg)
    regStatus = rowp['p_step_done']
    gmStatus = row['gm_status']
    if gmStatus == 4:
      if self.all_submit(cid, 1):
        return 1 ## r1 all submit
      else:
        return 2 ## r1 still some regs to submit
      return 6 ## r1 has been run
    if gmStatus == 6:
      return 6 ## r1 has been run
    if gmStatus == 6:
      return 6 ## r1 has been run
    if round == 1:
      if rowc['r1sub'] == 10:
        return 1
    if round == 2:
      if rowc['r2sub'] == 10:
        return 2
    if round == 3:
      if rowc['r3sub'] == 10:
        return 3
    pass
    
  def pcgd_advance_click(self, **event_args):
    ## this is a player (NOT fut) who wants to know if ready for next round
    ## first, check if all regions have submitted
    my_cid = mg.my_game_id
    cid = mg.my_game_id
    reg = mg.my_reg
    row = app_tables.games_log.get(game_id=cid)
    gmStatus = row['gm_status']
    if gmStatus == 4:
      ### NOT all regs have submitted for round 2025 to 2040
      n = Notification(mg.not_all_submitted_p_tx, timeout=5, title=mg.waiting_tx, style="info")
      n.show()
      return
    if gmStatus == 5:
      ### all regs HAVE submitted for round 2025 to 2040
      n = Notification(mg.all_submitted_p_tx, timeout=5, title=mg.waiting_tx, style="info")
      n.show()
      return
#    if gmStatus == 6:
#      ### waiting for GM to start round 2025 to 2040
#      n = Notification(mg.waiting_for_gm_to_start_round, timeout=5, title=mg.waiting_tx, style="info")
#      n.show()
#      return
    print("pcgd_advance_click -- gmStatus > 5: it is="+str(gmStatus))
    if gmStatus == 6:
      rc = app_tables.cookies.get(game_id=cid)
      if rc['r1sub'] < 10:
        n = Notification(mg.not_to_2060, style="warning")
        n.show()
        return
      print("pcgd_advance_tx")
      anfang = time.time()
      ### round 2025 to 2040 ran successfully
      n = Notification(mg.sim_success_tx1, timeout=5, title=mg.sim_success_title_tx, style="success")
      n.show()
      # prepare TA card for new round
      self.p_card_graf_dec.visible = True 
      self.pcgd_title.text = mg.player_board_tx + mg.my_personal_game_id + ', ' + mg.reg_to_longreg[reg] + ', '+ mg.pov_to_Poverty[mg.my_ministry]
      self.pcgd_info_rd1.content = mg.pcgd_info_after_rd1_tx
      self.pcgd_advance.visible = True 
      self.pcgd_plot_card.visible = True 
      self.plot_card_rp.visible = True
      self.dec_card.visible = True 
      role = mg.my_ministry
      print("mg.my_ministry= "+role)
      yr, runde = self.get_runde(cid)
      self.pcgd_generating.visible = True
      self.pcgd_generating.text = mg.pcgd_generating_tx1
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 2)
      while not self.task.is_completed():
        pass
      else: ## launch_create_plots_for_slots is done
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        if role == 'fut':
          self.dec_card.visible = False
          self.pcgd_info_rd1.visible = True
          self.card_fut.visible = True
          self.pcgd_info_rd1.content = mg.pcgd_rd1_info_short
          self.fut_info.content = mg.pcgd_rd1_info_fut_tx
        else:
          self.dec_card.visible = True
          self.pcgd_info_rd1.content = mg.pcgd_rd1_info_tx
          self.pcgd_info_rd1.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        if role == 'fut':
          self.do_future(cid, role, reg, runde, yr )
        else:
          self.do_non_future(cid, role, reg, runde, yr)      
      dauer = round(time.time() - anfang, 0)
      self.top_duration.text = dauer
      return
    if gmStatus == 7:  ## waiting for decisions until 2060
      rc = app_tables.cookies.get(game_id=cid)
      if rc['r2sub'] < 10:
        n = Notification(mg.not_to_2060, style="warning")
        n.show()
        return
      else:
        n = Notification(mg.all_submitted_p_tx, timeout=7, style="info")
        n.show()
        return
    if gmStatus == 10: ## 2040 to 2060 successfully run
      print("pcgd_advance_tx -- gmStatus is "+str(gmStatus))
      anfang = time.time()
      ### round 2040 to 2060 ran successfully
      n = Notification(mg.sim_success_tx1, timeout=5, title=mg.sim_success_title_tx, style="success")
      n.show()
      # prepare TA card for new round
      self.p_card_graf_dec.visible = True 
      self.pcgd_title.text = mg.player_board_tx + mg.my_personal_game_id + ', ' + mg.reg_to_longreg[reg] + ', '+ mg.pov_to_Poverty[mg.my_ministry]
      self.pcgd_info_rd1.content = mg.pcgd_info_after_rd1_tx
      self.pcgd_advance.visible = True 
      self.pcgd_plot_card.visible = True 
      self.plot_card_rp.visible = True
      self.dec_card.visible = True 
      role = mg.my_ministry
      print("mg.my_ministry= "+role)
      yr, runde = self.get_runde(cid)
      self.pcgd_generating.visible = True
      self.pcgd_generating.text = mg.pcgd_generating_tx2
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 3)
      while not self.task.is_completed():
        pass
      else: ## launch_create_plots_for_slots is done
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        if role == 'fut':
          self.dec_card.visible = False
          self.pcgd_info_rd1.visible = True
          self.card_fut.visible = True
          self.pcgd_info_rd1.content = mg.pcgd_rd1_info_short
          self.fut_info.content = mg.pcgd_rd1_info_fut_tx
        else:
          self.dec_card.visible = True
          self.pcgd_info_rd1.content = mg.pcgd_rd1_info_tx
          self.pcgd_info_rd1.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        if role == 'fut':
          self.do_future(cid, role, reg, runde, yr )
        else:
          self.do_non_future(cid, role, reg, runde, yr)      
      dauer = round(time.time() - anfang, 0)
      self.top_duration.text = dauer
      return
    if gmStatus == 12: ## 2060 to 2100 successfully run
      print("+++++++++++++++++++++++++++++")
      print("pcgd_advance_tx ++++++ gmStatus is "+str(gmStatus))
      anfang = time.time()
      n = Notification(mg.sim_success_tx1, timeout=5, title=mg.sim_success_title_tx, style="success")
      n.show()
      # prepare TA card for new round
      self.p_card_graf_dec.visible = True 
      self.pcgd_title.text = mg.player_board_tx + mg.my_personal_game_id + ', ' + mg.reg_to_longreg[reg] + ', '+ mg.pov_to_Poverty[mg.my_ministry]
      self.pcgd_info_rd1.content = mg.pcgd_info_after_rd1_tx
      self.pcgd_advance.visible = False 
      self.pcgd_plot_card.visible = True 
      self.plot_card_rp.visible = True
      self.dec_card.visible = False 
      role = mg.my_ministry
      print("mg.my_ministry= "+role)
      yr, runde = self.get_runde(cid)
      self.pcgd_generating.visible = True
      self.pcgd_generating.text = mg.pcgd_generating_tx2
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 4)
      while not self.task.is_completed():
        pass
      else: ## launch_create_plots_for_slots is done
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        if role == 'fut':
          self.dec_card.visible = False
          self.pcgd_info_rd1.visible = True
          self.card_fut.visible = True
          self.pcgd_info_rd1.content = mg.pcgd_rd1_info_short
          self.fut_info.content = mg.pcgd_rd1_info_fut_tx
        else:
          self.dec_card.visible = False
          self.pcgd_info_rd1.content = mg.pcgd_rd1_info_tx
          self.pcgd_info_rd1.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        if role == 'fut':
          print()
          self.do_future(cid, role, reg, runde, yr )
        else:
          self.do_non_future(cid, role, reg, runde, yr)      
      dauer = round(time.time() - anfang, 0)
      self.top_duration.text = dauer
      return

  def tick_gm_round_ready_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    cid = mg.my_game_id
    row = app_tables.games_log.get(game_id=cid)
    if row['gm_status'] == 5:
      self.gm_card_wait_1_btn_check.visible = False
      self.gm_start_round.visible = True
    else:
      self.gm_card_wait_1_btn_check.visible = True
      self.gm_start_round.visible = False

  def credits_click(self, **event_args):
    alert(mg.credits_tx, title=mg.credits_title)


     

      

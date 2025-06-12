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
from time import strftime, localtime
from ..log_sign import log_sign

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.tick_gm_round_ready.interval = 0
    self.timer_1.interval = 104104
    self.timer_1_tick()
#    app_tables.cookies.delete_all_rows()
#    app_tables.state_of_play.delete_all_rows()
#    app_tables.step_done.delete_all_rows()
#    app_tables.roles_assign.delete_all_rows()

#    user = anvil.users.get_user()
#    self.user_dbg(user, '__init__ Home')
#    if user is not None:
#      who = user['reg']
#      wo = user['where']
#      user = anvil.users.get_user()
#      self.user_dbg(user, '__init__ Home 2')
#      if who is None and wo == 2:
#        self.show_none_2(user)
#        return
#      if who == 'gm' and wo == 3:
#        self.show_gm_3(user)
#        return

    my_loc, my_loc2, lox = anvil.server.call('get_locale')
    mg.my_lang = lox
    alert(lu.sign_up[lox], title=lu.why_sign_up_title[lox], large=True)
    new_user = {}
    # Open an alert displaying the 'ArticleEdit' Form
    save_clicked = alert(
      content=log_sign(item=new_user),
      #      title="Sign Up",
      large=False,
      buttons=[]
    )
    if save_clicked == 42 or save_clicked == 342:
      ### left the app
      self.navbar_links.visible = False
      self.bye_card.visible = True 
      self.lang_card.visible = False 
      self.top_entry.visible = False 
      self.bye_tx.text = lu.bye_tx[lox]
      return
    elif save_clicked == 'admin':
      self.adm_card.visible = True 
      self.navbar_links.visible = False 
      self.lang_card.visible = False
      return
    else:
      usr = save_clicked['u']
      mg.my_email = usr
      row = app_tables.nutzer.get(email=usr)
      wo = row['wo']
      reg = row['reg']
      role = row['role']
      game_id = row['game_id']
      lx = row['lang']

#    wo = 5
#    reg = 'gm'
    if wo == 1:
      ## just registered
      self.do_lang(my_loc)
      pass
    elif wo == 2 and not reg == 'gm':
      ## player, NOT fut, round 1 waiting for decisions
      em = mg.my_email
      user = app_tables.nutzer.get(email=em)
      self.show_reg_2(reg, role, lx, game_id, em)
    elif wo == 5 and reg == 'gm':
      ## success to 2040
      em = mg.my_email
      user = app_tables.nutzer.get(email=em)
      self.show_gm_5(lx, game_id)
    elif wo == 2:
      ## gm select npbp
      em = mg.my_email
      user = app_tables.nutzer.get(email=em)
      self.show_none_2(user)
      pass
    elif wo == 3:
      ## select npbp
      em = mg.my_email
      user = app_tables.nutzer.get(email=em)
      self.show_gm_3(user)
#      gm_card_wait_1
      pass
    elif wo == 4:
      ## npbp selected & set up ... waiting for players to log in
      em = mg.my_email
      user = app_tables.nutzer.get(email=em)
      self.show_gm_4(user)

  def show_reg_2(self, reg, role, lx, cid, em):
    mg.my_game_id = cid
    mg.my_ministry = role
    mg.my_reg = reg
    row = app_tables.nutzer.get(email=em)
    lx = row['lang']
    mg.my_lang = lx
    self.lang_card.visible = False 
    self.p_card_graf_dec.visible = True
    wrx = mg.regs.index(reg)
    wmx = mg.roles.index(role)
    reglong = self.do_reg_to_longreg(reg)
    rolelong = self.do_ta_to_longmini(role)
    self.pcgd_advance.text = lu.pcgd_advance_tx_str[lx]
    self.pcgd_title.text = lu.player_board_tx_str[lx] + ': ' +cid+'-'+str(wrx)+str(wmx)+',   '+reglong+',   '+rolelong
    mg.fut_title_tx2 = self.pcgd_title.text
    your_game_id = cid + "-" + str(wrx) + str(wmx)
#    congrats = lu.pcr_submit_msg1_str[lx] + rolelong + lu.pcr_submit_msg2_str[lx] + reglong + ".\n" + lu.pcr_submit_msg3_str[lx] + "\n" + your_game_id 
    mg.my_personal_game_id = your_game_id
#    alert(congrats, title=lu.pcr_submit_title_str[lx])
    yr, runde = self.get_runde(cid)
    self.pcgd_generating.visible = False
    self.pcgd_plot_card.visible = True
    if role == 'fut':
      self.card_fut.visible = False
      self.dec_card.visible = False 
      self.p_after_submit.visible = True
      self.pcgd_info_rd1.content = lu.pcgd_rd1_info_short_str[lx]
      self.fut_info.content = lu.pcgd_rd1_info_fut_tx_str[lx]
    else:
      self.dec_card.visible = True
      self.pcgd_info_rd1.content = lu.pcgd_rd1_info_tx_str[lx]
    self.pcgd_info_rd1.visible = True
    slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
    self.plot_card_rp.items = slots
    if role == 'fut':
      self.cid_reg_role_info.text = cid + '  +++ ' + self.do_reg_to_longreg(reg) + '  - ' + self.do_ta_to_longmini(role)
      self.wait_for_run_after_submit.content = lu.after_submit_tx_str[lx]
      self.p_advance_to_next_round.text = lu.p_advance_to_next_round_tx_str[lx]
      row_cookies = app_tables.cookies.get(game_id=cid)
      if runde == 1:
        if not row_cookies['r1sub'] == 10:
          self.do_future(cid, role, reg, runde, yr, lx )
          self.p_after_submit.visible = False
      elif runde == 2:
        if not row_cookies['r2sub'] == 10:
          self.do_future(cid, role, reg, runde, yr, lx )
          self.p_after_submit.visible = False
      elif runde == 3:
        if not row_cookies['r2sub'] == 10:
          self.do_future(cid, role, reg, runde, yr, lx )
          self.p_after_submit.visible = False
      else:
        alert("show_reg_2: runde not 1 nor 2 nor 3 but "+str(runde))
    else:
      self.do_non_future(cid, role, reg, runde, yr, lx)
#    row['wo'] = 2
    a= 2
      # show instructions, graphs, decision sliders 
    
  def do_lang(self, my_loc):
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
      alert("We have not yet translated the texts and prompts to your language. As a fallback, we are using English. If you want to help translating, please get in touch.", title="Apologies")
      self.lang_dd_menu.placeholder = "English"
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
      alert("De norske tekstene kommer fra google. Vennligst hjelp oss med å forbedre dem.", title="Beklager")
    elif my_lox == 2:
      alert("Wir haben die Texte und Aufforderungen noch nicht in das informelle Deutsch übersetzt. Solange nutzen wir die formelle 'Sie' Form. Wenn Du helfen möchtest, lass uns das wissen.", title="Entschuldige")
    elif my_lox > 4:
      alert("We have not yet translated the texts and prompts to your language. If you want to help, please get in touch.", title="Apologies")

  def user_dbg(self, u, von):
    if u is None:
      self.err_msg.text = self.err_msg.text + '\nuser=NONE from '+von
    else:
      if u['email'] is None:
        em = 'NONE'
      else:
        em = u['email']
      self.err_msg.text = self.err_msg.text + '\nUser: email='+em
      if u['reg'] is None:
        re = 'NONE'
      else:
        re = u['reg']
      self.err_msg.text = self.err_msg.text + ' reg='+re
      if u['where'] is None:
        we = 'NONE'
      else:
        we = str(u['where'])
      self.err_msg.text = self.err_msg.text + ' where='+we
      if u['role'] is None:
        ro = 'NONE'
      else:
        ro = u['role']
      self.err_msg.text = self.err_msg.text + ' role='+ro
      if u['game_id'] is None:
        ro = 'NONE'
      else:
        ro = u['game_id']
      self.err_msg.text = self.err_msg.text + ' game_ID='+ro+' '+von

  def show_none_2(self, user):
    lx = user['lang']
    mg.my_lang = lx
    self.set_lang(lx)
    self.top_title.text = lu.top_title_str[lx]    
    self.lang_card.visible = False 
    self.top_entry.visible = True 
    
  def show_gm_3(self, user):
    lx = user['lang']
    mg.my_lang = lx
    cid = user['game_id']
    mg.my_game_id = cid
    self.set_lang(lx)
    self.lang_card.visible = False 
    self.top_entry.visible = False 
    self.gm_role_reg.visible = True 
    self.gm_board.text = lu.msg_gm_board_head_str[lx] + cid
    self.top_title.text = lu.top_title_str[lx]
    self.gm_card_wait_1.visible = False  
    self.gm_card_wait_1_info.visible = True 
    self.gm_card_wait_1_btn_check.visible = True 

  def set_reg_cb_false(self):
    self.cb_us.visible = False
    self.cb_af.visible = False
    self.cb_cn.visible = False
    self.cb_me.visible = False
    self.cb_sa.visible = False
    self.cb_la.visible = False
    self.cb_pa.visible = False
    self.cb_ec.visible = False
    self.cb_eu.visible = False
    self.cb_se.visible = False

  def show_gm_4(self, user):
    lx = user['lang']
    mg.my_lang = lx
    cid = user['game_id']
    mg.my_game_id = cid
    self.set_lang(lx)
    self.lang_card.visible = False 
    self.top_entry.visible = False 
    self.gm_role_reg.visible = True 
    self.gm_board.text = lu.msg_gm_board_head_str[lx] + cid
    self.top_title.text = lu.top_title_str[lx]
    self.gm_board_info.visible = False 
    self.gm_reg_npbp.visible = False 
    self.set_reg_cb_false()
    self.gm_card_wait_1.visible = True  
    self.gm_card_wait_1_info.visible = True 
    self.gm_card_wait_1_btn_check.visible = True 

  def show_gm_5(self, lx, cid):
      mg.my_lang = lx
      mg.my_game_id = cid
      self.set_lang(lx)
      self.lang_card.visible = False 
      self.top_entry.visible = False 
      self.set_reg_cb_false()
#      gm_card_wait_1_temp_title
      self.gm_card_wait_1_info.content = lu.gm_wait_round_done_tx0_str[lx]
      self.gm_card_wait_1_rp.visible = False
      self.gm_wait_kickoff_r1_rp.visible = False

      self.gm_role_reg.visible = True 
      self.gm_board.text = lu.msg_gm_board_head_str[lx] + cid
      self.top_title.text = lu.top_title_str[lx]
      self.gm_board_info.visible = False 
      self.gm_reg_npbp.visible = False 
      self.gm_card_wait_1.visible = True  
      self.gm_card_wait_1_info.visible = True 
      self.gm_card_wait_1_btn_check.visible = False 
      self.gm_start_round.visible = True
      a=3
    
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

  my_lox = mg.my_lang
#  p_btn_select_game.text = mg.p_btn_select_game_en
#  gm_board_info.content = lu.msg_gm_board_info_str[my_lox]
    
  def top_btn_thanks_click(self, **event_args):
    my_lox = mg.my_lang
    alert(content=lu.top_thanks_msg_str[my_lox], title=lu.top_thanks_title_str[my_lox])

  def top_btn_poc_click(self, **event_args):
    lx = mg.my_lang
    alert(lu.poc_str[lx],
         title=lu.poc_title[lx])

  def top_btn_help_click(self, **event_args):
    my_lox = mg.my_lang
    webbrowser.open_new("http://sdggamehelp.blue-way.net")

  def set_lang(self, my_lox):
    self.cb_af.text = lu.cb_af_tx_str[my_lox]
    self.cb_us.text = lu.cb_us_tx_str[my_lox]
    self.cb_cn.text = lu.cb_cn_tx_str[my_lox]
    self.cb_me.text = lu.cb_me_tx_str[my_lox]
    self.cb_sa.text = lu.cb_sa_tx_str[my_lox]
    self.cb_la.text = lu.cb_la_tx_str[my_lox]
    self.cb_pa.text = lu.cb_pa_tx_str[my_lox]
    self.cb_ec.text = lu.cb_ec_tx_str[my_lox]
    self.cb_eu.text = lu.cb_eu_tx_str[my_lox]
    self.cb_se.text = lu.cb_se_tx_str[my_lox]
    self.gm_reg_npbp.text = lu.gm_reg_npbp_tx_str[my_lox]
    self.gm_card_wait_1_info.content = lu.gm_card_wait_1_info_tx_str[my_lox]
    self.gm_card_wait_1_btn_check.text = lu.gm_card_wait_1_btn_check_tx_str[my_lox]
    self.gm_start_round.text = lu.gm_card_wait_1_btn_kick_off_round_1_tx_str[my_lox]
    self.setup_npbp_label.text = lu.setup_npbp_label_tx_str[my_lox]
    self.pcr_rb_af.text = lu.cb_af_tx_str[my_lox]
    self.pcr_rb_us.text = lu.cb_us_tx_str[my_lox]
    self.pcr_rb_cn.text = lu.cb_cn_tx_str[my_lox]
    self.pcr_rb_me.text = lu.cb_me_tx_str[my_lox]
    self.pcr_rb_sa.text = lu.cb_sa_tx_str[my_lox]
    self.pcr_rb_la.text = lu.cb_la_tx_str[my_lox]
    self.pcr_rb_pa.text = lu.cb_pa_tx_str[my_lox]
    self.pcr_rb_ec.text = lu.cb_ec_tx_str[my_lox]
    self.pcr_rb_eu.text = lu.cb_eu_tx_str[my_lox]
    self.pcr_rb_se.text = lu.cb_se_tx_str[my_lox]
    self.pcr_rb_pov.text = lu.cb_pov_tx_str[my_lox]
    self.pcr_rb_ineq.text = lu.cb_ineq_tx_str[my_lox]
    self.pcr_rb_emp.text = lu.cb_emp_tx_str[my_lox]
    self.pcr_rb_food.text = lu.cb_food_tx_str[my_lox]
    self.pcr_rb_ener.text = lu.cbener_tx_str[my_lox]
    self.pcr_rb_fut.text = lu.cb_fut_tx_str[my_lox]
    self.pcr_title.text = lu.pcr_title_tx_str[my_lox]
    self.pcr_col_left_title.text = lu.pcr_col_left_title_tx_str[my_lox]
    self.pcr_col_right_title.text = lu.pcr_col_right_title_tx_str[my_lox]
    self.pcr_submit.text = lu.pcr_submit_tx_str[my_lox]
    self.fut_not_all_logged_in.text = lu.fut_not_all_logged_in_tx_str[my_lox]
    #    self.pcr_submit_msg1.text = mg.pcr_submit_msg1
    #    self.pcr_submit_msg2.text = mg.pcr_submit_msg2
    self.pcgd_title.text = lu.pcr_title_tx_str[my_lox]
    self.pcgd_info_rd1.content = lu.pcgd_rd1_info_tx_str[my_lox]
    self.pcgd_generating.text = lu.pcgd_generating_tx4_str[my_lox]
    self.dec_info.content = lu.dec_info_tx_str[my_lox]
    self.dec_title.text = lu.dec_title_tx_str[my_lox]
    self.pcgd_advance.text = lu.pcgd_advance_tx_str[my_lox]
    self.refresh_numbers.text = lu.refresh_numbers_tx_str[my_lox]
    self.submit_numbers.text = lu.submit_numbers_tx_str[my_lox]
    self.fut_info.content = lu.fut_info_tx_str[my_lox]
    self.fut_bud_lb1.text = lu.fut_bud_lb1_tx_str[my_lox]
    self.fut_bud_lb2.text = lu.fut_bud_lb2_tx_str[my_lox]
    self.fut_but_lb3.text = lu.fut_bud_lb3_tx_str[my_lox]
    self.cpf_lb.text = lu.cfpov_tx_str[my_lox]
    self.cpf_lb2.text = lu.cfpov_lb_tx_str[my_lox]
    self.cpf_ineq_lb.text = lu.cfineq_tx_str[my_lox]
    self.cpf_ineq_lb2.text = lu.cfineq_lb_tx_str[my_lox]
    self.cpf_emp_lb.text = lu.cfemp_tx_str[my_lox]
    self.cpf_emp_lb2.text = lu.cfemp_lb_tx_str[my_lox]
    self.cpf_food_lb.text = lu.cffood_tx_str[my_lox]
    self.cpf_food_lb2.text = lu.cffood_lb_tx_str[my_lox]
    self.cpf_ener_lb.text = lu.cfener_tx_str[my_lox]
    self.cpf_ener_lb2.text = lu.cfener_lb_tx_str[my_lox]
    self.gm_card_wait_1_temp_title.text = lu.gm_card_wait_1_temp_title_tx1_str[my_lox]
    self.gm_board_info.content = lu.msg_gm_board_info_str[my_lox]
    self.show_hide_plots.tooltip = lu.show_hide_plots_tx[my_lox]
    self.top_start_game.text = lu.top_start_game_str[my_lox]
    self.top_join_game.text = lu.top_join_game_str[my_lox]
    self.top_btn_thanks.text = lu.top_btn_thanks_str[my_lox]
    self.top_btn_help.text = lu.top_btn_help_str[my_lox]
    self.credits.text = lu.credits_btn_tx_str[my_lox]
    self.top_btn_poc.text = "PoC"
#    self.credits.text = lu.credits_btn_tx_str[my_lox]

  def show_npbp_choice(self, my_lox, anfang, game_id):
    self.set_lang(my_lox)
    ende = time.time()
    dauer = round(ende - anfang, 0)
    self.seconds.text = str(dauer)+' sec'
    self.seconds.textcolor = 'red'
    self.top_entry.visible = False
    self.gm_board.text = lu.msg_gm_board_head_str[my_lox] +game_id
    self.gm_role_reg.visible = True
    self.seconds.visible = True
    self.gm_board_info.visible = True
    self.gm_cp_not_played.visible = True
    self.setup_npbp_label.visible = False
    ## deselect all regions
    self.cb_us.checked = False
    self.cb_af.checked = False
    self.cb_cn.checked = False
    self.cb_me.checked = False
    self.cb_sa.checked = False
    self.cb_pa.checked = False
    self.cb_la.checked = False
    self.cb_ec.checked = False
    self.cb_eu.checked = False
    self.cb_se.checked = False
    em = mg.my_email
    row = app_tables.nutzer.get(email=em)
    row['wo'] = 3

  def top_start_game_click(self, **event_args):
    my_lox = mg.my_lang
    self.top_join_game.visible = False 
    t = TextBox(placeholder=lu.enter_code_tx[my_lox])
    alert(content=t,title=lu.enter_code_title_tx[my_lox])
    print(f"You entered: {t.text}")
    code = t.text.upper()
#    if not code == 'LTG-ND':
    if not code == '':
      alert(lu.wrong_code_tx[my_lox])
      return
    game_id = anvil.server.call('generate_id')
    anvil.server.call('budget_to_db', 2025, game_id)
    em = mg.my_email
    rows = app_tables.nutzer.search(email=em)
    row_ln = len(rows)
    if row_ln == 1:
      rows[0]['reg'] = 'gm'
      rows[0]['game_id'] = game_id
      rows[0]['wo'] = 2
      mg.my_game_id = game_id
    else:
      alert("top_start_game_click row_ln NOT eq 1")
    app_tables.cookies.add_row(game_id=game_id, r1sub=0, r2sub=0, r3sub=0,gm_step=0) ## clean slate
    self.top_start_game.visible = False
    self.top_join_game.visible = False
    mg.my_game_id = game_id
    jetzt = datetime.datetime.now()
    app_tables.games_log.add_row(game_id=game_id, gm_status=1, started=jetzt)
    self.tick_gm_round_ready.interval = 0
    # self.tick_gm_round_ready_tick()
    msg = lu.gm_id_msg1_str[my_lox] + game_id + lu.gm_id_msg2_str[my_lox]
    alert(msg, title=lu.gm_id_title_str[my_lox])
    anfang = time.time()
    self.task = anvil.server.call('launch_set_roles', game_id)
    self.top_entry_label.visible = True
    while not self.task.is_completed():
      self.top_entry_label.text = lu.topentry_label_tx_str[my_lox]
    else:
      self.show_npbp_choice(my_lox, anfang, game_id)
      a=2

  def check_rnsub(self, cid):
    ## ToDo
    ## in production switch first true and false and handle in top_join_game_click
    row = app_tables.cookies.get(game_id=cid)
    if row['r1sub'] < 10 or row['r2sub'] < 10 or row['r3sub'] < 10:
      return True 
    else:
      return True
  
  def top_join_game_click(self, **event_args):
    lx = mg.my_lang
    self.lang_card.visible = False 
    self.top_entry.visible = False
#    self.top_join_game.visible = False
    self.p_cp_choose_game.visible = True 
    self.p_lb_choose_game.text = lu.p_lb_choose_game_str[lx]
    self.p_enter_id.placeholder = lu.p_enter_id_str[lx]
    self.p_enter_id.focus()
    
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
    lx = mg.my_lang
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
    if len(npbp) == 10:
      alert(lu.need_one_reg[lx], title=lu.need_one_reg_title[lx])
      self.gm_role_reg.visible = False 
      self.top_entry.visible = True 
      self.top_start_game.visible = True 
      self.top_entry_label.visible = False 
      self.show_npbp_choice(lx, anfang, cid)
      return
    self.task = anvil.server.call('launch_set_npbp', cid, npbp)
    while not self.task.is_completed():
      self.setup_npbp_label.visible = True
    else:
      self.setup_npbp_label.visible = False
      ende = time.time()
      dauer = round(ende - anfang, 0)
      self.seconds.text = str(dauer)+' sec'
    self.gm_card_wait_1.visible = True
    # update user
    em = mg.my_email
    row = app_tables.nutzer.get(email=em)
    row['wo'] = 4
      
  def set_avail_regs(self, **event_args):
    print("IN set_avail_regs")
    self.set_regs_invisible()
    lx = mg.my_lang
    cid = mg.my_game_id
    msg = lu.pcr_title_tx_str[lx] + ': '+cid
    self.pcr_title.text = msg
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

  def do_ta_to_longmini(self, role):
    lx = mg.my_lang
    if role == 'pov':
      return lu.ta_to_longmini_pov_str[lx]
    if role == 'ineq':
      return lu.ta_to_longmini_ineq_str[lx]
    if role == 'emp':
      return lu.ta_to_longmini_emp_str[lx]
    if role == 'food':
      return lu.ta_to_longmini_food_str[lx]
    if role == 'ener':
      return lu.ta_to_longmini_ener_str[lx]
    if role == 'fut':
      return lu.ta_to_longmini_fut_str[lx]

  def do_reg_to_longreg(self, reg):
    lx = mg.my_lang
    if reg == 'us':
      return lu.reg_to_longreg_us_str[lx]
    if reg == 'af':
      return lu.reg_to_longreg_af_str[lx]
    if reg == 'cn':
      return lu.reg_to_longreg_cn_str[lx]
    if reg == 'me':
      return lu.reg_to_longreg_me_str[lx]
    if reg == 'pa':
      return lu.reg_to_longreg_pa_str[lx]
    if reg == 'la':
      return lu.reg_to_longreg_la_str[lx]
    if reg == 'sa':
      return lu.reg_to_longreg_sa_str[lx]
    if reg == 'ec':
      return lu.reg_to_longreg_ec_str[lx]
    if reg == 'eu':
      return lu.reg_to_longreg_eu_str[lx]
    if reg == 'se':
      return lu.reg_to_longreg_se_str[lx]

  def gm_card_wait_1_btn_check_click(self, **event_args):
    lx = mg.my_lang
    cid = mg.my_game_id
    runde = mg.game_runde+1
    self.gm_card_wait_1_btn_check.visible = True
    self.gm_start_round.visible = False
    self.gm_wait_kickoff_r1.visible = False 
    rows = app_tables.roles_assign.search(game_id=cid, round=runde, taken=0)
    if len(rows) == 0:
      self.gm_card_wait_1_btn_check.visible = False
      self.gm_card_wait_1_rp.visible = False
      self.gm_card_wait_1_temp_title.text = lu.gm_card_wait_1_temp_title_tx2_str[lx]
      self.gm_start_round.visible = True
    else:
      slots = []
#    slots2 = [{key: r[key] for key in ["reg", "role"]} for r in app_tables.roles_assign.search(game_id=cid, round=runde, taken=0)]
#    res = list({d[key] for d in slots2 if key in d})
      for row in rows:
        longreg = self.do_reg_to_longreg(row['reg'])
        longrole = self.do_ta_to_longmini(row['role'])
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
#    em = mg.email
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
    em = mg.my_email
    row = app_tables.nutzer.get(email=em)
    row['game_id'] = cid
    row['reg'] = reg
    row['role'] = role
    row['wo'] = 1 
    return True

  def get_runde(self, cid):
    row = app_tables.games_log.get(game_id=cid)
    r = row['gm_status']
    if r == 4 or r == 5:
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

  def show_p_1(self, reg, role, cid, reglong, rolelong):
    em = mg.my_email
    mg.my_game_id = cid
    mg.my_ministry = role
    mg.my_reg = reg
    row = app_tables.nutzer.get(email=em)
    lx = row['lang']
    mg.my_lang = lx
    self.p_card_graf_dec.visible = True
    self.p_choose_role.visible = False
    self.dec_card.visible = False
    wrx = mg.regs.index(reg)
    wmx = mg.roles.index(role)
    self.pcgd_title.text = self.pcgd_title.text + ': ' +cid+'-'+str(wrx)+str(wmx)+',   '+reglong+',   '+rolelong
    mg.fut_title_tx2 = self.pcgd_title.text
    your_game_id = cid + "-" + str(wrx) + str(wmx)
    congrats = lu.pcr_submit_msg1_str[lx] + rolelong + lu.pcr_submit_msg2_str[lx] + reglong + ".\n" + lu.pcr_submit_msg3_str[lx] + "\n" + your_game_id 
    mg.my_personal_game_id = your_game_id
    alert(congrats, title=lu.pcr_submit_title_str[lx])
    self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 1, lx)
    self.pcgd_generating.visible = True
#      make something visible
    while not self.task.is_completed():
      pass
    else: ## background is done
      yr, runde = self.get_runde(cid)
      self.pcgd_generating.visible = False
      self.pcgd_plot_card.visible = True
      if role == 'fut':
        self.card_fut.visible = True
        self.pcgd_info_rd1.content = lu.pcgd_rd1_info_short_str[lx]
        self.fut_info.content = lu.pcgd_rd1_info_fut_tx_str[lx]
      else:
        self.dec_card.visible = True
        self.pcgd_info_rd1.content = lu.pcgd_rd1_info_tx_str[lx]
    self.pcgd_info_rd1.visible = True
    slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
    self.plot_card_rp.items = slots
    if role == 'fut':
      self.do_future(cid, role, reg, runde, yr, lx )
    else:
      self.do_non_future(cid, role, reg, runde, yr, lx)
    row['wo'] = 2

  def pcr_submit_click(self, **event_args):
    #anfang = time.time()
    if self.pcr_rb_fut.selected:
      self.p_card_graf_dec.visible = False
    reg = mg.my_reg
    reglong = self.do_reg_to_longreg(reg)
    role = mg.my_ministry
    rolelong = self.do_ta_to_longmini(role)
    cid = mg.my_game_id
    save_ok = self.save_player_choice(cid, role, reg)
    if save_ok:
      self.show_p_1(reg, role, cid, reglong, rolelong)
#    dauer = round(time.time() - anfang, 0)
#    self.top_duration.text = dauer

  def show_hide_plots_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.show_hide_plots.visible = True
    self.show_hide_plots.selected = False
#    self.show_hide_plots.text = lu.show_hide_plots_hide_tx_str[lx]
    if self.show_hide_plots.selected is False:
      pass
      
  def do_non_future(self, cid, role, reg, runde, yr, lx):
    lang = mg.my_lang
    print("in do_NON_future ie TAs "+cid+' '+reg+' '+role+' '+str(runde)+' '+str(yr)+' lang:'+str(lang))
    if yr == 2100:
      return
    self.dec_card.visible = True
    self.pcgd_advance.visible = True
    pol_list = anvil.server.call('get_policy_budgets', reg, role, yr, cid, lang)
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

  def set_fut_not_all_logged_in(self, lx):
    self.fut_not_all_logged_in.text = lu.fut_not_all_logged_in_tx_str[lx]
    self.refresh_numbers.text = lu.refresh_numbers_tx_str[lx]    
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

  def set_fut_all_logged_in(self, lx):
    self.submit_numbers.text = lu.submit_numbers_tx_str[lx]
    self.refresh_numbers.text = lu.refresh_numbers_tx_str[lx]    
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

  def do_future(self, cid, role, reg, runde, yr, lx):
    self.err_msg.text = self.err_msg.text + "\n-------entering do_future cid="+cid+' reg='+reg+' role='+role+' round='+str(runde)+' yr='+str(yr)
    self.pcgd_advance.visible = False
    self.dec_card.visible = False
    self.card_fut.visible = True
    ## check if all your regional ministers have logged in
    ## ToDo when game is restarted from suspension this must be done differently.
    all_colleauges_logged_in = self.check_all_colleagues_logged_in(cid, reg, runde)
    if not all_colleauges_logged_in:
      self.set_fut_not_all_logged_in(lx)
    else:
      self.set_fut_all_logged_in(lx)
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
          self.submit_numbers.text = lu.submit_numbers_tx_str[lx] + str(yr)
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

  def get_all_pol_to_names(self, ab, lx):
#    print(' -------------  get_all_pol_to_names')
#    print(ab)
    abs = []
    for a in ab:
      if a == 'ExPS':
        abs.append(lu.pol_to_name_ExPS_str[lx])
      elif a == 'CCS':
        abs.append(lu.pol_to_name_CCS_str[lx])
      elif a == 'TOW':
        abs.append(lu.pol_to_name_TOW_str[lx])
      elif a == 'FPGDC':
        abs.append(lu.pol_to_name_FPGDC_str[lx])
      elif a == 'RMDR':
        abs.append(lu.pol_to_name_RMDR_str[lx])
      elif a == 'REFOREST':
        abs.append(lu.pol_to_name_REFOREST_str[lx])
      elif a == 'FTPEE':
        abs.append(lu.pol_to_name_FTPEE_str[lx])
      elif a == 'LPBsplit':
        abs.append(lu.pol_to_name_LPBsplit_str[lx])
      elif a == 'FMPLDD':
        abs.append(lu.pol_to_name_FMPLDD_str[lx])
      elif a == 'StrUP':
        abs.append(lu.pol_to_name_StrUP_str[lx])
      elif a == 'Wreaction':
        abs.append(lu.pol_to_name_Wreaction_str[lx])
      elif a == 'SGMP':
        abs.append(lu.pol_to_name_SGMP_str[lx])
      elif a == 'FWRP':
        abs.append(lu.pol_to_name_FWRP_str[lx])
      elif a == 'ICTR':
        abs.append(lu.pol_to_name_ICTR_str[lx])
      elif a == 'XtaxCom':
        abs.append(lu.pol_to_name_XtaxCom_str[lx])
      elif a == 'Lfrac':
        abs.append(lu.pol_to_name_Lfrac_str[lx])
      elif a == 'IOITR':
        abs.append(lu.pol_to_name_IOITR_str[lx])
      elif a == 'IWITR':
        abs.append(lu.pol_to_name_IWITR_str[lx])
      elif a == 'SGRPI':
        abs.append(lu.pol_to_name_SGRPI_str[lx])
      elif a == 'FEHC':
        abs.append(lu.pol_to_name_FEHC_str[lx])
      elif a == 'XtaxRateEmp':
        abs.append(lu.pol_to_name_XtaxRateEmp_str[lx])
      elif a == 'FLWR':
        abs.append(lu.pol_to_name_FLWR_str[lx])
      elif a == 'RIPLGF':
        abs.append(lu.pol_to_name_RIPLGF_str[lx])
      elif a == 'FC':
        abs.append(lu.pol_to_name_FC_str[lx])
      elif a == 'NEP':
        abs.append(lu.pol_to_name_NEP_str[lx])
      elif a == 'Ctax':
        abs.append(lu.pol_to_name_Ctax_str[lx])
      elif a == 'DAC':
        abs.append(lu.pol_to_name_DAC_str[lx])
      elif a == 'XtaxFrac':
        abs.append(lu.pol_to_name_XtaxFrac_str[lx])
      elif a == 'LPBgrant':
        abs.append(lu.pol_to_name_LPBgrant_str[lx])
      elif a == 'LPB':
        abs.append(lu.pol_to_name_LPB_str[lx])
      elif a == 'SSGDR':
        abs.append(lu.pol_to_name_SSGDR_str[lx])
      elif a == 'ISPV':
        abs.append(lu.pol_to_name_ISPV_str[lx])
    return abs

               
  def calc_cost_home_ta(self, pct, tltl, gl, maxc, ta):
    lx = mg.my_lang
    self.err_msg.text = self.err_msg.text + "\n-------entering calc_cost_home_ta with ta=" + ta + ' maxc=' + str(maxc)
    # get_names
    if ta == 'pov':
      abbrs = [r['abbr'] for r in app_tables.policies.search(ta='Poverty')]
      names = self.get_all_pol_to_names(abbrs, lx)
    elif ta == 'ineq':
      abbrs = [r['abbr'] for r in app_tables.policies.search(ta='Inequality')]
      names = self.get_all_pol_to_names(abbrs, lx)
    elif ta == 'emp':
      abbrs = [r['abbr'] for r in app_tables.policies.search(ta='Empowerment')]
      names = self.get_all_pol_to_names(abbrs, lx)
    elif ta == 'food':
      abbrs = [r['abbr'] for r in app_tables.policies.search(ta='Food')]
      names = self.get_all_pol_to_names(abbrs, lx)
    elif ta == 'ener':
      abbrs = [r['abbr'] for r in app_tables.policies.search(ta='Energy')]
      names = self.get_all_pol_to_names(abbrs, lx)
#    print('len_pct '+ str(len(pct)))
#    print(names)
    slots = []
    for i in range(0, len(pct)):
#        print('i='+str(i))
        nw = pct[i] - tltl[i]
        nb = 0
        nt = gl[i] - tltl[i]
        pct_of_range = nw / (nt - nb)
        cost = round(maxc * pct_of_range, 2)
#        self.err_msg.text = self.err_msg.text + "\n-- inside calc_cost_home_ta pol_name=" + names[i] + ' pol_amount=' + str(cost)
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
    total_cost = round(cost_pov + cost_emp + cost_ener + cost_food + cost_ineq, 1)
    pct_of_budget = total_cost / bud * 100
    self.fut_bud_amount.text = round(bud, 0)
    self.fut_invest.text = total_cost
    within_budget = False
    if pct_of_budget > 100:
      pct_shown = str(int(pct_of_budget))
      self.fut_bud_amount.foreground = 'red'
      self.fut_invest.foreground = 'red'
      self.fut_invest_pct.foreground = 'red'
      self.submit_numbers.visible = False
      self.fut_invest_pct.text = pct_shown
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
    lx = mg.my_lang
    cid = mg.my_game_id
    role = 'fut'
    reg = mg.my_reg
    yr, runde = self.get_runde(cid)
    em = mg.my_email
    ro = app_tables.nutzer.get(email=em)
    self.err_msg.text = self.err_msg.text + "refresh_numbers_click with cid="+cid + " role="+role  + " reg="+reg  + " runde="+str(runde) + " yr="+str(yr) + " lx="+str(lx)  + " wo="+str(ro['wo'])  + " nutzer_game_ID="+(ro['game_id']) + " nutzer_reg="+(ro['reg'])
    self.do_future(cid, role, reg, runde, yr,lx)

  def all_reg_submitted(self, cid, step):
    rows = app_tables.step_done.search(game_id=cid, p_step_done=q.any_of(step, 99))
    if len(rows) == 10:
      return True 
    else:
      return False
    
  def submit_numbers_click(self, **event_args):
    # First, confirm submission
    lx = mg.my_lang
    result = alert(content=lu.confirm_submit_tx_str[lx],
                   title=lu.confirm_title_tx_str[lx],
                  large=False,
                  buttons=[(lu.nbr_confirm_t[lx], True), (lu.nbr_confirm_f[lx], False)])
    if not result :
      n = Notification(lu.nothing_submitted_tx_str[lx])
      n.show()
    else: ## submission confirmed, reg DID submit numbers
      my_cid = mg.my_personal_game_id
      cid = mg.my_game_id
      yr, runde = self.get_runde(cid)
      role = 'fut'  ## we're in the Future TA
      reg = mg.my_reg
      row = app_tables.step_done.get(game_id=cid, reg=reg)
#      pStepDone = row['p_step_done']
      cid_cookie = anvil.server.call('get_game_id_from_cookie')
      print(cid_cookie)
      ## show confirmation alert
      row_games_log = app_tables.games_log.get(game_id=cid_cookie)
      gm_status = row_games_log['gm_status']
      em = mg.my_email
      ro2 = app_tables.nutzer.get(email=em)
      self.err_msg.text = self.err_msg.text + "\n-------- submit_numbers_click cid=" + (cid_cookie) + ' gm_status=' + str(gm_status) + " runde="+str(runde) + " yr="+str(yr) + " lx="+str(lx)  + " wo="+str(ro2['wo'])  + " nutzer_game_ID="+(ro2['game_id']) + " nutzer_reg="+(ro2['reg'])
      self.cid_reg_role_info.text = my_cid + '  +++ ' + self.do_reg_to_longreg(reg) + '  - ' + self.do_ta_to_longmini(role)
      self.card_fut.visible = False
      self.p_card_graf_dec.visible = False
      self.p_after_submit.visible = True
      ## bump cookie for this round r_sub by one
      all_regs_sub = False
      if runde == 1:
        self.err_msg.text = self.err_msg.text + "\n---inside submit_numbers_click::bump cookie  runde=" + str(runde)
        anvil.server.call('set_cookie_sub', 'r1', 1, cid_cookie) 
        rc = app_tables.cookies.get(game_id=cid_cookie)
        if rc['r1sub'] == 10:
          all_regs_sub = True
        rosub = app_tables.submitted.get(game_id=cid_cookie, round=1,reg=reg)
        rosub['submitted'] = True
      elif runde == 2:
        self.err_msg.text = self.err_msg.text + "\n---inside submit_numbers_click::bump cookie  runde=" + str(runde)
        anvil.server.call('set_cookie_sub', 'r2', 1, cid_cookie)        
        rc = app_tables.cookies.get(game_id=cid_cookie)
        if rc['r2sub'] == 10:
          all_regs_sub = True
        rosub = app_tables.submitted.get(game_id=cid_cookie, round=2,reg=reg)
        rosub['submitted'] = True
      elif runde == 3:
        self.err_msg.text = self.err_msg.text + "\n---inside submit_numbers_click::bump cookie  runde=" + str(runde)
        anvil.server.call('set_cookie_sub', 'r3', 1, cid_cookie)        
        rc = app_tables.cookies.get(game_id=cid_cookie)
        if rc['r3sub'] == 10:
          all_regs_sub = True
        rosub = app_tables.submitted.get(game_id=cid_cookie, round=3,reg=reg)
        rosub['submitted'] = True
      ### update steps
      self.p_after_submit.visible = True
      self.wait_for_run_after_submit.content = lu.after_submit_tx_str[lx]
      self.p_advance_to_next_round.text = lu.p_advance_to_next_round_wait_str[lx]
      if not all_regs_sub: ## there is at least one region (of players) that has not yet submitted
        row2 = app_tables.step_done.get(game_id=cid_cookie, reg=reg)
        if runde == 1:
          my_p_step_done = 3
          row2.update(p_step_done=3) ## the region submitted decisions for round 2025-2040
        elif runde == 2:
          my_p_step_done = 5
          row2.update(p_step_done=5) ## the region submitted decisions for round 2040- 2060
        elif runde == 3:
          my_p_step_done = 7
          row2.update(p_step_done=7) ## the region submitted decisions for round 2060 - 2100
        n = Notification(lu.nicht_all_sub_p_tx_str[lx], timeout=2)
        n.show() 
        self.err_msg.text = self.err_msg.text + "\n---inside submit_numbers_click::step_done  my_p_step_done=" + str(my_p_step_done)
      else:  ## all HAVE submitted
        row = app_tables.games_log.get(game_id=cid_cookie)
        rc = app_tables.cookies.get(game_id=cid_cookie)
        self.err_msg.text = self.err_msg.text + "\n---inside submit_numbers_click::ALL submit  gmStatus=" + str(gm_status) + "rXsubs:" + str(rc['r1sub']) + ' ' + str(rc['r2sub']) + ' ' + str(rc['r3sub'])
        if row['gm_status'] == 4:
          row['gm_status'] = 5 ## off to run 2025 to 2040
          self.err_msg.text = self.err_msg.text + "\n---ALL submit  OLD gmStatus=4 NEW gmstatus=5"+ " rXsubs:" + str(rc['r1sub']) + ' ' + str(rc['r2sub']) + ' ' + str(rc['r3sub'])
        if row['gm_status'] == 6:
          row['gm_status'] = 7 ## all regs submitted for 2040 to 2060
          self.err_msg.text = self.err_msg.text + "\n---ALL submit  OLD gmStatus=6 NEW gmstatus=7"+ " rXsubs:" + str(rc['r1sub']) + ' ' + str(rc['r2sub']) + ' ' + str(rc['r3sub'])
        if row['gm_status'] == 9:
          row['gm_status'] = 10 ## all regs submitted for 2060 to 2100
          self.err_msg.text = self.err_msg.text + "\n---ALL submit  OLD gmStatus=9 NEW gmstatus=10"+ " rXsubs:" + str(rc['r1sub']) + ' ' + str(rc['r2sub']) + ' ' + str(rc['r3sub'])
#        rg = app_tables.games_log.get(game_id=cid_cookie)
        n = Notification(lu.all_submitted_p_tx_str[lx], timeout=3)
        n.show()
#        self.test_model.visible = False  ## this is a debug button
        ## give feedback
        ## after_submit_tx = "Your region's decisions have been submitted - thanks!\nOnce all regions have submitted their decisons, the model will be advanced for the next round. This will take a bit of time ..."
        self.card_fut.visible = False
        self.p_advance_to_next_round.visible = True 
        self.p_advance_to_next_round.text = lu.p_advance_to_next_round_wait_str[lx]
        self.err_msg.text = self.err_msg.text + "\n---inside submit_numbers_click:: p_advance_to_next_round_wait_str:" + lu.p_advance_to_next_round_wait_str[lx]
        if runde == 1:
          # p_advance_to_next_round_tx = "Get the results until 2040 and the decision sheet for 2040-2060 - your children's future"
          self.p_advance_to_next_round.text = lu.p_advance_to_next_round_tx_str[lx]
        elif runde == 2:
          # p_advance_to_1_tx = "Get the results until 2060 and the decision sheet for 2060-210 - your grandchildren's future"
          self.p_advance_to_next_round.text = lu.p_advance_to_1_tx_str[lx]
        elif runde == 3:
          # p_advance_to_2_tx = "Get the results until the end of the century"
          self.p_advance_to_next_round.text = lu.p_advance_to_2_tx_str[lx]
    for ug in range(0, len(mg.dbg_info)):
      self.err_msg.text = self.err_msg.text + '\n-dbg--' + mg.dbg_info[ug]
    mg.dbg_info = []

  def get_not_all_sub(self, cid, runde):
    reg = mg.my_reg
    rows = app_tables.submitted.search(game_id='',round=runde, reg=reg, submitted=False)
    not_sub_list = []
    for r in rows:
#      regshort = r['reg']
      longreg = self.do_reg_to_longreg(r['reg'])
      not_sub_list.append(longreg)
    pass
    
  def gm_start_round_click(self, **event_args):
    lx = mg.my_lang
    ## first, check if all regions have submitted
    self.gm_card_wait_1_rp.visible = False
    self.gm_wait_kickoff_r1.visible = False
    self.gm_wait_kickoff_r1_rp.visible = False
    self.gm_start_round.visible = False
    cid_cookie = anvil.server.call('get_game_id_from_cookie')
    em = mg.my_email
    ro2 = app_tables.nutzer.get(email=em)
    row = app_tables.games_log.get(game_id=cid_cookie)
    self.err_msg.text = self.err_msg.text + "\n-------- gm_start_round_click cid=" + (cid_cookie) + ' gm_status=' + str(row['gm_status']) + " runde=??" + " yr=??"+ " lx="+str(lx)  + " wo="+str(ro2['wo'])  + " nutzer_game_ID="+ro2['game_id'] + " nutzer_reg="+ro2['reg']
    if row['gm_status'] not in [5,7,10]:
      n = Notification(lu.nicht_all_sub_gm_tx_str[lx], timeout=2)
      n.show()
      self.err_msg.text = self.err_msg.text + "\n--inside gm_status' not in [5,7,10] line=1077"
      self.gm_start_round.visible = True
      return
    if row['gm_status'] == 5: ## 2025 to 2040 ready
      von = 2025
      bis = 2040
      runde = 1
      row = app_tables.cookies.get(game_id=cid_cookie)
      rxsub = row['r1sub']
      self.err_msg.text = self.err_msg.text + "\ngm_status'] == 5 rxsub="+str(rxsub)
      if rxsub < 10:
        not_all_sub_list = self.get_not_all_sub(cid_cookie, runde)
        lmsg = lu.nicht_all_sub_gm_tx_str[lx]
        for ii in range(0, len(not_all_sub_list)):
          lmsg = lmsg + "\n" + not_all_sub_list[ii]
        n = Notification(lmsg, style="warning", timeout=2)
        n.show()
        self.gm_start_round.visible = True
        return
    elif row['gm_status'] == 6:
      n = Notification(mg.gm_wait_sub2_tx, title=mg.waiting_tx, style="warning")
      n.show()
#      self.gm_start_round.visible = True      
      self.err_msg.text = self.err_msg.text + "\ngm_status'] == 6"
      return
    elif row['gm_status'] == 7:
      von = 2040
      bis = 2060
      runde = 2
      row = app_tables.cookies.get(game_id=cid_cookie)
      rxsub = row['r2sub']
      self.err_msg.text = self.err_msg.text + "\ngm_status'] == 7 rxsub="+str(rxsub)
      if rxsub < 10:
        not_all_sub_list = self.get_not_all_sub(cid_cookie, runde)
        lmsg = lu.nicht_all_sub_gm_tx_str[lx]
        for ii in range(0, len(not_all_sub_list)):
          lmsg = lmsg + "\n" + not_all_sub_list[ii]
        n = Notification(lmsg, style="warning", timeout=2)
        n.show()
        self.gm_start_round.visible = True        
        return
    elif row['gm_status'] == 10:
      von = 2060
      bis = 2100
      runde = 3
      row = app_tables.cookies.get(game_id=cid_cookie)
      rxsub = row['r3sub']
      self.err_msg.text = self.err_msg.text + "\ngm_status'] == 10 rxsub="+str(rxsub)
      if rxsub < 10:
        not_all_sub_list = self.get_not_all_sub(cid_cookie, runde)
        lmsg = lu.nicht_all_sub_gm_tx_str[lx]
        for ii in range(0, len(not_all_sub_list)):
          lmsg = lmsg + "\n" + not_all_sub_list[ii]
        n = Notification(lmsg, style="warning", timeout=4)
        n = Notification(lu.nicht_all_sub_gm_tx_str[lx], style="warning")
        n.show()
        self.gm_start_round.visible = True        
        return
    else:
      abc1 = str(row['gm_status'])
      abc2 = "row['gm_status'] not correct " + abc1
      alert(abc2)
      return
    self.gm_card_wait_1_info.visible = True
    # running_model_tx = "... advancing the model ..."
    # gm_wait_round_started_tx = 'The model has been started. Please wait until the simulation is done...'
    self.gm_card_wait_1_info.content = lu.gm_wait_round_started_tx_str[lx]
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
      self.err_msg.text = self.err_msg.text + "\n+++ launch_ugregmod done"
      # gm_wait_round_done_tx = 'The model has been advanced. Tell your players to click on the Start next round button.'
      self.gm_card_wait_1_info.content = lu.gm_wait_round_done_tx0_str[lx]
      row = app_tables.games_log.get(game_id=cid_cookie)
      if runde == 1:
        row['gm_status'] = 6 ## first round successfully done
        self.gm_start_round.visible = True
        self.gm_start_round.text = lu.gm_start_round_tx_2_str[lx]
        anvil.server.call('budget_to_db', 2040, cid_cookie)
        em = mg.my_email
        rn = app_tables.nutzer.get(email=em)
        rn['wo'] = 5 # succesfully ran to 2040
        self.err_msg.text = self.err_msg.text + "\n++ gm_start_round_click runde="+ str(runde)+' gm_status=6 - email='+em
      elif runde == 2:
        self.gm_card_wait_1_info.content = lu.gm_wait_round_done_tx2_str[lx]
        self.gm_start_round.visible = True
        row['gm_status'] = 10
        self.gm_start_round.text = lu.gm_start_round_tx_3_str[lx]
        anvil.server.call('budget_to_db', 2060, cid_cookie)
        em = mg.my_email
        rn = app_tables.nutzer.get(email=em)
        rn['wo'] = 7 # succesfully ran to 2060
        self.err_msg.text = self.err_msg.text + "\ng++ m_start_round:: "+str(runde)+' gm_status=10 - email='+em
      elif runde == 3:
        self.gm_card_wait_1_info.content = lu.gm_wait_round_done_tx3_str[lx]
        self.gm_start_round.visible = False
        row['gm_status'] = 12
        self.gm_start_round.text = lu.gm_start_round_tx_3_str[lx]
        em = mg.my_email
        rn = app_tables.nutzer.get(email=em)
        rn['wo'] = 9 # succesfully ran to 2100
        self.err_msg.text = self.err_msg.text + "\ngm_start_round:: "+str(runde)+' gm_status=12 - email='+em
        row_closed = app_tables.games_log.get(game_id=cid_cookie)
        row_closed['closed'] = datetime.datetime.now()

  def get_not_looked_at(self, rows_looked_at):
    lx = mg.my_lang
    l1 = []
    for r in rows_looked_at:
      ta = r['ta']
      if ta == 'us':
        longta = lu.reg_to_longreg_us_str[lx]
      elif ta == 'af':
        longta = lu.reg_to_longreg_af_str[lx]
      elif ta == 'cn':
        longta = lu.reg_to_longreg_cn_str[lx]
      elif ta == 'me':
        longta = lu.reg_to_longreg_me_str[lx]
      elif ta == 'sa':
        longta = lu.reg_to_longreg_sa_str[lx]
      elif ta == 'la':
        longta = lu.reg_to_longreg_la_str[lx]
      elif ta == 'pa':
        longta = lu.reg_to_longreg_pa_str[lx]
      elif ta == 'ec':
        longta = lu.reg_to_longreg_ec_str[lx]
      elif ta == 'eu':
        longta = lu.reg_to_longreg_eu_str[lx]
      elif ta == 'se':
        longta = lu.reg_to_longreg_se_str[lx]
      l1.append(longta)
    return l1
    
  def p_advance_to_next_round_click(self, **event_args):
    # Get the results until the end of the run for FUT
    # pcgd_advance (for non_fut) must set something for the current reg
    # and only if 5 have set it can fut advance
    cid = mg.my_game_id
    lx = mg.my_lang
    row = app_tables.games_log.get(game_id=cid)
    em = mg.my_email
    ro2 = app_tables.nutzer.get(email=em)
    self.err_msg.text = self.err_msg.text + "\n-------- p_advance_to_next_round_click cid=" + (cid) + ' gm_status=' + str(row['gm_status'])  + " lx="+str(lx)  + " wo="+str(ro2['wo'])  + " nutzer_game_ID="+(ro2['game_id']) + " nutzer_reg="+(ro2['reg']) + " nutzer_email="+(ro2['email'])
    if row['gm_status'] == 5:
      self.err_msg.text = self.err_msg.text + "\n--: gm_status="+str(row['gm_status'])
      alert(lu.p_waiting_model_run_tx_str[lx], title=lu.waiting_tx_str[lx])
    ### prepare graphs and decisions for round 2 if gm_status == 2
    elif row['gm_status'] == 6: ## 2025 to 2040 successfully run
#      reg = mg.my_reg
      reg = ro2['reg']
      runde = 2
      yr = 2040
      rows_looked_at = app_tables.pcgd_advance_looked_at.search(game_id=cid, round=1, reg=reg, looked_at=True)
      if len(rows_looked_at) < 5:
        not_looked_at_list = self.get_not_looked_at(rows_looked_at)
        lmsg = lu.not_all_looked_at_tx[lx]
        for ii in range(0, len(not_looked_at_list)):
          lmsg = lmsg + "\n" + not_looked_at_list[ii]
        alert(lmsg, title=lu.not_all_looked_at_title[lx])
        return
      self.err_msg.text = self.err_msg.text + "\n- KICKING OFF to 2040"
      self.p_card_graf_dec.visible = True
      self.p_choose_role.visible = False
      self.dec_card.visible = False
      self.p_after_submit.visible = False
      role = 'fut'
      self.err_msg.text = self.err_msg.text + "\n- runde=2 role="+role+' gm_status='+str(row['gm_status'])+' reg='+reg+ " runde="+str(runde) + " yr="+str(yr)
      self.pcgd_title.text = mg.fut_title_tx2 + lu.p_info_40_fut[lx]
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 2, lx)
      self.pcgd_generating.visible = True
      #      make something visible
      while not self.task.is_completed():
        pass
      else: ## background is done
        ### get runde, yr
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        self.card_fut.visible = True
        self.pcgd_info_rd1.content = lu.pcgd_rd1_info_short_str[lx]
        self.fut_info.content = lu.pcgd_rd1_info_fut_tx_str[lx]
        self.pcgd_info_rd1.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        self.do_future(cid, role, reg, runde, yr,lx )
        self.err_msg.text = self.err_msg.text + "\n- AFTER do_future (1550)"
    elif row['gm_status'] == 10: ## 2040 to 2060 successfully run
      #      reg = mg.my_reg
      reg = ro2['reg']
      runde = 3
      yr = 2060
      rows_looked_at = app_tables.pcgd_advance_looked_at.search(game_id=cid, round=2, reg=reg, looked_at=True)
      if len(rows_looked_at) < 5:
        not_looked_at_list = self.get_not_looked_at(rows_looked_at)
        lmsg = lu.not_all_looked_at_tx[lx]
        for ii in range(0, len(not_looked_at_list)):
          lmsg = lmsg + "\n" + not_looked_at_list[ii]
        alert(lmsg, title=lu.not_all_looked_at_title[lx])
        return
      self.err_msg.text = self.err_msg.text + "\n- KICKING OFF to 2060"
      self.p_card_graf_dec.visible = True
      self.p_choose_role.visible = False
      self.dec_card.visible = False
      self.p_after_submit.visible = False
      role = 'fut'
      self.err_msg.text = self.err_msg.text + "\n- runde="+str(runde)+' role='+role+' gm_status='+str(row['gm_status'])+' reg='+reg+ " runde="+str(runde) + " yr="+str(yr)
      self.pcgd_title.text = mg.fut_title_tx2 + lu.p_info_60_fut[lx]
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 3, lx)
      self.pcgd_generating.visible = True
      #      make something visible
      while not self.task.is_completed():
        pass
      else: ## background is done
        ### get runde, yr
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        self.card_fut.visible = True
        self.pcgd_info_rd1.content = lu.pcgd_rd1_info_short_str[lx]
        self.fut_info.content = lu.pcgd_rd1_info_fut_tx_str[lx]
        self.pcgd_info_rd1.visible = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        self.do_future(cid, role, reg, runde, yr ,lx)
        self.err_msg.text = self.err_msg.text + "\n- AFTER do_future (1587)"
    elif row['gm_status'] == 12: ## 2060 to 2100 successfully run
      #      reg = mg.my_reg
      reg = ro2['reg']
      runde = 4
      yr = 2100
      rows_looked_at = app_tables.pcgd_advance_looked_at.search(game_id=cid, round=3, reg=reg, looked_at=True)
      if len(rows_looked_at) < 5:
        not_looked_at_list = self.get_not_looked_at(rows_looked_at)
        lmsg = lu.not_all_looked_at_tx[lx]
        for ii in range(0, len(not_looked_at_list)):
          lmsg = lmsg + "\n" + not_looked_at_list[ii]
        alert(lmsg, title=lu.not_all_looked_at_title[lx])
        return
      self.err_msg.text = self.err_msg.text + "\n- KICKING OFF to 2100"
      self.p_card_graf_dec.visible = True
      self.p_choose_role.visible = False
      self.dec_card.visible = False
      self.card_fut.visible = False
      self.p_after_submit.visible = False
      role = 'fut'
      self.err_msg.text = self.err_msg.text + "\n- runde="+str(runde)+' role='+role+' gm_status='+str(row['gm_status'])+' reg='+reg+ " runde="+str(runde) + " yr="+str(yr)
      self.pcgd_title.text = mg.fut_title_tx2 + lu.p_info_21_fut[lx]
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 4, lx)
      self.pcgd_generating.visible = True
      #      make something visible
      while not self.task.is_completed():
        pass
      else: ## background is done
        ### get runde, yr
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        self.card_fut.visible = False ## no more budget at the end
        self.pcgd_info_rd1.content = lu.pcgd_rd1_infoend_tx_str[lx]
        self.fut_info.content = lu.pcgd_rd1_info_end_tx_str[lx]
        self.pcgd_info_rd1.visible = True
        self.fut_detail('hide')
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        self.do_future(cid, role, reg, runde, yr, lx )
        self.err_msg.text = self.err_msg.text + "\n- AFTER do_future(1626) "
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
    n= Notification("off to run the model from test_model_click", timeout=2)
    n.show()
    cid = mg.my_game_id
    self.task = anvil.server.call('launch_ugregmod', cid, 2025, 2040)
#      make something visible
    while not self.task.is_completed(): # model still running
      pass
    else: ## model is done
      Notification("Model is done", timeout=3)

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
      alert(" w < floor or w > gle")
#    print(pol+' min='+str(tle)+' max='+str(gle)+' wert='+str(w))
    return w

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    dummy=anvil.server.call_s('fe_keepalive')
    self.err_msg.text =  self.err_msg.text + '-- ticking away -- '+strftime('%Y-%m-%d %H:%M:%S', localtime(time.time()))+ ' '+dummy

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
#    reg = mg.my_reg
    row = app_tables.games_log.get(game_id=cid)
    rowc = app_tables.cookies.get(game_id=cid)
#    rowp = app_tables.step_done.get(game_id=cid, reg=reg)
#    regStatus = rowp['p_step_done']
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
    # something needs to be set here, by re and round and ta
#    my_cid = mg.my_game_id
    lx = mg.my_lang
    cid = mg.my_game_id
    reg = mg.my_reg
    row = app_tables.games_log.get(game_id=cid)
    gmStatus = row['gm_status']
    self.err_msg.text = self.err_msg.text + "\npcgd_advance_tx ++ gmStatus="+str(gmStatus)
    if gmStatus == 4:
      ### NOT all regs have submitted for round 2025 to 2040
      n = Notification(lu.nicht_all_sub_p_tx_str[lx], timeout=2, title=lu.waiting_tx_str[lx], style="info")
      n.show()
      return
    if gmStatus == 5:
      ### all regs HAVE submitted for round 2025 to 2040
      n = Notification(lu.all_submitted_p_tx_str[lx], timeout=3, title=lu.waiting_tx_str[lx], style="info")
      n.show()
      self.plot_card_rp.visible = True
      self.dec_card.visible = False
      return
#    if gmStatus == 6:
#      ### waiting for GM to start round 2025 to 2040
#      n = Notification(mg.waiting_for_gm_to_start_round, timeout=5, title=mg.waiting_tx, style="info")
#      n.show()
#      return
    self.err_msg.text = "\npcgd_advance_click -- gmStatus > 5: it is="+str(gmStatus)
    if gmStatus == 6:
      rc = app_tables.cookies.get(game_id=cid)
      if rc['r1sub'] < 10:
        n = Notification(lu.not_to_2060_str[lx], style="warning")
        n.show()
        return
      self.err_msg.text = self.err_msg.text + "\ngmStaus = 6 r1sub=10"
#      anfang = time.time()
      ### round 2025 to 2040 ran successfully
      n = Notification(lu.sim_success_tx40_str[lx], timeout=2, title=lu.sim_success_title_tx_str[lx], style="success")
      n.show()
      # prepare TA card for new round
      self.p_card_graf_dec.visible = True 
      self.pcgd_title.text = lu.player_board_tx_str[lx] + mg.my_personal_game_id + ', ' + self.do_reg_to_longreg(reg) + ', '+ mg.pov_to_Poverty[mg.my_ministry]
      self.pcgd_info_rd1.content = lu.pcgd_info_after_rd1_tx_str[lx]
      self.pcgd_advance.visible = True 
      self.pcgd_plot_card.visible = True 
      self.plot_card_rp.visible = True
      self.dec_card.visible = True 
      role = mg.my_ministry
      print("mg.my_ministry= "+role)
      yr, runde = self.get_runde(cid)
      self.pcgd_generating.visible = True
      self.pcgd_generating.text = lu.pcgd_generating_tx1_str[lx]
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 2, lx)
      while not self.task.is_completed():
        pass
      else: ## launch_create_plots_for_slots is done
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        if role == 'fut':
          self.dec_card.visible = False
          self.pcgd_info_rd1.visible = True
          self.card_fut.visible = True
          self.pcgd_info_rd1.content = lu.pcgd_rd1_info_short_str[lx]
          self.fut_info.content = lu.pcgd_rd1_info_fut_tx_str[lx]
        else:
          self.dec_card.visible = True
          self.pcgd_info_rd1.content = lu.pcgd_rd1_info_tx_str[lx]
          self.pcgd_info_rd1.visible = True
          row_looked_at = app_tables.pcgd_advance_looked_at.get(game_id=cid, reg= reg, ta=role, round=1)
          row_looked_at['looked_at'] = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        if role == 'fut':
          self.do_future(cid, role, reg, runde, yr ,lx)
        else:
          self.do_non_future(cid, role, reg, runde, yr, lx)      
#      dauer = round(time.time() - anfang, 0)
#      self.top_duration.text = dauer
      return
    if gmStatus == 7:  ## waiting for decisions until 2060
      rc = app_tables.cookies.get(game_id=cid)
      if rc['r2sub'] < 10:
        n = Notification(lu.not_to_2060_str[lx], style="warning")
        n.show()
        return
      else:
        n = Notification(lu.all_submitted_p_tx_str[lx], timeout=3, style="info")
        n.show()
        return
    if gmStatus == 10: ## 2040 to 2060 successfully run
      self.err_msg.text = self.err_msg.text + "\npcgd_advance_tx -- gmStatus is "+str(gmStatus)
#      anfang = time.time()
      ### round 2040 to 2060 ran successfully
      n = Notification(lu.sim_success_tx60_str[lx], timeout=2, title=lu.sim_success_title_tx_str[lx], style="success")
      n.show()
      # prepare TA card for new round
      self.p_card_graf_dec.visible = True 
      self.pcgd_title.text = lu.player_board_tx_str[lx] + mg.my_personal_game_id + ', ' + self.do_reg_to_longreg(reg) + ', '+ mg.pov_to_Poverty[mg.my_ministry]
      self.pcgd_info_rd1.content = lu.pcgd_info_after_rd1_tx_str[lx]
      self.pcgd_advance.visible = True 
      self.pcgd_plot_card.visible = True 
      self.plot_card_rp.visible = True
      self.dec_card.visible = True 
      role = mg.my_ministry
      print("mg.my_ministry= "+role)
      yr, runde = self.get_runde(cid)
      self.pcgd_generating.visible = True
      self.pcgd_generating.text = lu.pcgd_generating_tx2_str[lx]
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 3, lx)
      while not self.task.is_completed():
        pass
      else: ## launch_create_plots_for_slots is done
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        if role == 'fut':
          self.dec_card.visible = False
          self.pcgd_info_rd1.visible = True
          self.card_fut.visible = True
          self.pcgd_info_rd1.content = lu.pcgd_rd1_info_short_str[lx]
          self.fut_info.content = lu.pcgd_rd1_info_fut_tx_str[lx]
        else:
          self.dec_card.visible = True
          self.pcgd_info_rd1.content = lu.pcgd_rd1_info_tx_str[lx]
          self.pcgd_info_rd1.visible = True
          row_looked_at = app_tables.pcgd_advance_looked_at.get(game_id=cid, reg= reg, ta=role, round=2)
          row_looked_at['looked_at'] = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        if role == 'fut':
          self.do_future(cid, role, reg, runde, yr, lx )
        else:
          self.do_non_future(cid, role, reg, runde, yr, lx)      
#      dauer = round(time.time() - anfang, 0)
#      self.top_duration.text = dauer
      return
    if gmStatus == 12: ## 2060 to 2100 successfully run
      self.err_msg.text = self.err_msg.text + "\npcgd_advance_tx ++ gmStatus is "+str(gmStatus)
#      anfang = time.time()
      n = Notification(lu.sim_success_tx21_str[lx], timeout=2, title=lu.sim_success_title_txend_str[lx], style="success")
      n.show()
      # prepare TA card for new round
      self.p_card_graf_dec.visible = True 
      self.pcgd_title.text = lu.player_board_tx_str[lx] + mg.my_personal_game_id + ', ' + self.do_reg_to_longreg(reg) + ', '+ mg.pov_to_Poverty[mg.my_ministry]
      self.pcgd_info_rd1.content = lu.pcgd_info_after_rd1_tx_str[lx]
      self.pcgd_advance.visible = False 
      self.pcgd_plot_card.visible = True 
      self.plot_card_rp.visible = True
      self.dec_card.visible = False 
      role = mg.my_ministry
      print("mg.my_ministry= "+role)
      yr, runde = self.get_runde(cid)
      self.pcgd_generating.visible = True
      self.pcgd_generating.text = lu.pcgd_generating_tx2_str[lx]
      self.task = anvil.server.call('launch_create_plots_for_slots', cid, reg, role, 4, lx)
      while not self.task.is_completed():
        pass
      else: ## launch_create_plots_for_slots is done
        self.pcgd_generating.visible = False
        self.pcgd_plot_card.visible = True
        if role == 'fut':
          self.dec_card.visible = False
          self.pcgd_info_rd1.visible = True
          self.card_fut.visible = True
          self.pcgd_info_rd1.content = lu.pcgd_rd1_info_short_str[lx]
          self.fut_info.content = lu.pcgd_rd1_info_fut_tx_str[lx]
        else:
          self.dec_card.visible = False
          self.pcgd_info_rd1.content = lu.pcgd_rd1_info_end_tx_str[lx]
          self.pcgd_info_rd1.visible = True
          row_looked_at = app_tables.pcgd_advance_looked_at.get(game_id=cid, reg= reg, ta=role, round=3)
          row_looked_at['looked_at'] = True
        slots = [{key: r[key] for key in ["title", "subtitle", "cap", "fig"]} for r in app_tables.plots.search(game_id= cid, runde=runde, reg=reg, ta=role)]
        self.plot_card_rp.items = slots
        if role == 'fut':
          print()
          self.do_future(cid, role, reg, runde, yr, lx )
        else:
          self.do_non_future(cid, role, reg, runde, yr, lx)      
#      dauer = round(time.time() - anfang, 0)
#      self.top_duration.text = dauer
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
    my_lox = mg.my_lang
    alert(lu.credits_tx_str[my_lox], title=lu.credits_title_str[my_lox])

  def lang_lets_go_click(self, **event_args):
    """This method is called when the component is clicked."""
    my_lox = mg.my_lang
    self.lang_card.visible = False
    self.top_entry.visible = True 
    em = mg.my_email
    row = app_tables.nutzer.get(email=em)
    row['lang'] = my_lox
    self.top_join_game.text = lu.top_join_game_str[my_lox]
    self.top_start_game.text = lu.top_start_game_str[my_lox]

  def p_enter_id_pressed_enter(self, **event_args):
    ## correct game_id and gm_status = 4
    lx = mg.my_lang
    self.p_enter_id.character_limit = 8
    self.p_enter_id.focus()
    val = self.p_enter_id.text.upper()
    rows = app_tables.games_log.get(game_id=val, gm_status=4)
    if rows is None:
      enter_game_id = alert(lu.no_such_game_str[lx],title=lu.nsg_t[lx],
            buttons=[(lu.jga_t[lx], True), (lu.jga_f[lx], False)])
      if not enter_game_id:
        self.p_cp_choose_game.visible = False 
        self.top_entry.visible = True 
      return
    game_id_chosen = val
    mg.my_game_id = game_id_chosen
    self.set_lang(lx)
#    row = app_tables.status.get(game_id=game_id_chosen)
#    row.update(p_status=1) # he / she chose a game
    self.p_cp_choose_game.visible = False
#    self.card_select_reg_role.visible = True
    self.p_enter_id.visible = False 
    self.top_entry.visible = False
    self.p_choose_role.visible = True
    self.show_roles(rows['game_id'])

  def switch_1_change(self, **event_args):
    if self.switch_1.selected:
      self.err_msg.visible = True
    else:
      self.err_msg.visible = False

  def show_hide_plots_change(self, **event_args):
    if self.show_hide_plots.selected:
      self.plot_card_rp.visible = True
      self.dec_card.visible = True
    else:
      self.plot_card_rp.visible = False
      self.dec_card.visible = False

  def reset_db_click(self, **event_args):
    ## clear db
    app_tables.cookies.delete_all_rows()
    app_tables.submitted.delete_all_rows()
    app_tables.state_of_play.delete_all_rows()
    app_tables.step_done.delete_all_rows()
    app_tables.roles_assign.delete_all_rows()
    app_tables.game_files.delete_all_rows()
    app_tables.plots.delete_all_rows()
    app_tables.pcgd_advance_looked_at.delete_all_rows()
    rows = app_tables.games_log.search(game_id=q.not_("TEST"))
    for row in rows:
      row.delete()

  def adm_leave_click(self, **event_args):
    self.adm_card.visible = False 
    self.bye_card.background = "orange"
    self.bye_card.visible = True 
    self.bye_tx.text = "Admin: Ciao, Ade, Ha det ..."
    """This method is called when the component is clicked."""
    pass

  def reset_nutzer_click(self, **event_args):
    app_tables.nutzer.delete_all_rows()

  def ok_to_delete(self, nu):
    len_nu = len(nu)
    otd = 0 
    now = datetime.datetime.today()
    roundedNow = now.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    for n in nu:
      t = n['last_login_utc']
      if t is None:
        t = n['signed_up_utc']
      roundedB = t.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
      days = (roundedNow - roundedB).days
      if days + 1 > 90:
        otd = otd + 1
    if otd == len_nu: ## 1 gm and 6 nutzer
      cid = nu['game_id']
      rows = app_tables.cookies.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.budget.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.game_files.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.games_log.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.plots.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.submitted.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.state_of_play.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.step_done.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.roles_assign.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.pcgd_advance_looked_at.search(game_id=cid)
      for row in rows:
        row.delete()
      rows = app_tables.nutzer.search(game_id=cid)
      for row in rows:
        row.delete()
      alert("Game "+cid+" has been deleted")
      
  def del_90_click(self, **event_args):
    # from games_log get game_ids
    gids = app_tables.games_log.search()
    if len(gids) == 1:
      alert("Nothing to delete")
      return
    for gid in gids:
      if not gid['game_id'] == 'TEST':
        nutzers = app_tables.nutzer.search(game_id=gid['game_id'])
        ## last log in > 90 days or game_started > 90 days
        self.ok_to_delete(nutzers)


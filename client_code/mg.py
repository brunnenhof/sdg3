import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
#    from .. import mg
#    mg.say_hello()
#    mg = my_globs
###
### these are CLIENT globals, ie all forms on the client side can access them
my_game_id = ''
my_reg = ''
my_ministry = ''
my_personal_game_id = ''
my_step = 0
game_runde = 0
end_yr_start = 2025
end_yr_r1 = 2040
end_yr_r2 = 2060
end_yr_r3 = 2100
yr_picks_start = [1990, 2000, 2010, 2020]
yr_picks_r1 = [1990, 2000, 2010, 2020, 2030, 2040]
yr_picks_r2 = [1990, 2010, 2030, 2040, 2050, 2060]
yr_picks_r3 = [1990, 2025, 2060, 2080, 2100]
###
### comment this out in production and ask interactively
not_played_by_players = ['us', 'af', 'cn', 'sa', 'la', 'pa', 'eu', 'se']
###
### below does not change, evah!
roles = ['pov', 'ineq', 'emp', 'food', 'ener', 'fut']
ro_nbr = [0, 1, 2, 3, 4, 5]
regs = ['us', 'af', 'cn', 'me', 'sa', 'la', 'pa', 'ec', 'eu', 'se']
re_nbr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reg_to_longreg = {
  "us" : "USA",
  "af" : "Africa, South of Sahara",
  "cn" : "China",
  "me" : "Middle East & North Africa",
  "sa" : "South Asia",
  "la" : "Latin America",
  "pa" : "Pacific Rim",
  "ec" : "East Europe & Central Asia",
  "eu" : "Eurpe",
  "se" : "Southeast Asia"
}
ta_to_longmini = {
  "pov" : "Minister against Poverty",
  "ineq" : "Minister against Inequality",
  "emp" : "Minister for Empowerment",
  "food" : "Minister for Food & Agriculture",
  "ener" : "Minister for Energy",
  "fut" : "Minister for the Future"
}
pov_to_Poverty = {
  "pov": "Poverty",
  "ineq": "Inequality",
  "emp": "Empowerment",
  "food": "Food",
  "ener": "Energy",
  "fut": "Future"
}
Pov_to_pov = {
  "Poverty": "pov",
  "Inequality": "ineq",
  "Empowerment": "emp",
  "Food": "food",
  "Energy": "ener",
  "Future": "fut"
}
pol_to_ta = {"CCS" : "Energy",
"TOW" : "Poverty",
"FPGDC" : "Poverty",
"RMDR" : "Food",
"REFOREST" : "Food",
"FTPEE" : "Energy",
"LPBsplit" : "Poverty",
"ExPS" : "Poverty",
"FMPLDD " : "Poverty",
"StrUP" : "Inequality",
"Wreaction" : "Inequality",
"SGMP" : "Empowerment",
"FWRP" : "Food",
"ICTR" : "Inequality",
"XtaxCom" : "Inequality",
"Lfrac" : "Poverty",
"IOITR" : "Inequality",
"IWITR" : "Inequality",
"SGRPI" : "Inequality",
"FEHC" : "Empowerment",
"XtaxRateEmp" : "Empowerment",
"FLWR" : "Food",
"RIPLGF" : "Food",
"FC" : "Food",
"NEP" : "Energy",
"Ctax" : "Inequality",
"DAC" : "Energy",
"XtaxFrac" : "Inequality",
"LPBgrant" : "Poverty",
"LPB" : "Poverty",
"SSGDR" : "Poverty",
"ISPV" : "Energy"
}

top_title = 'END-times'
top_btn_thanks = 'Danke'
top_btn_start = 'Start a new game as organizer'
top_btn_join = 'JOIN a game as player'
top_btn_help = 'Help'
top_join_game = 'JOIN a game as player'
top_start_game = 'Start a game as organizer'
p_lb_choose_game = 'There are more than one open games. First select the one you want to join, then press the JOIN button:'
p_btn_select_game = 'JOIN'
gm_id_msg1 = "Your game ID is "
gm_id_msg2 =". Make a note of it and tell your players."
gm_id_title="Your game ID:"
top_thanks_msg ="... to our Alpha testers, the students in the SW101 course at the Realschule Baesweiler during April 2024 taught by René Langohr, and all the beta testers."
top_thanks_title="Thank you ... "
top_roles_setup_msg ="Roles template has been set up for "
title_you_are_joining = "You are joining: "
msg_game_not_started = "The game organizer has not yet started a game. Please wait until he/she does ..."
msg_gm_board = "Game Organizer Board"
msg_gm_board_info = "**Now, click on *all* the regions *not* played by your players (eg if there are not enough players for all roles)**"
cb_us_tx = 'USA'
cb_af_tx = 'Africa, South of Sahara'
cb_cn_tx = 'China'
cb_me_tx = 'Middle East - North Africa'
cb_sa_tx = 'South Asia'
cb_la_tx = 'Latin America'
cb_pa_tx = 'Pacific Rim'
cb_ec_tx = 'East Europe - Central Asia'
cb_eu_tx = 'Europe'
cb_se_tx = 'Southeast Asia'
cb_pov_tx = 'Poverty'
cb_ineq_tx = 'Inequality'
cb_emp_tx = 'Empowerment'
cb_food_tx = 'Food & agriculture'
cb_ener_tx = 'Energy'
cb_fut_tx = 'Future'
pcr_title_tx = 'Player Board Game '
pcr_col_left_title_tx = 'First, log into your region ...'
pcr_col_right_title_tx = '... then into your role as minister ...'
pcr_submit_tx = 'Once you have logged in to both your region and your ministry, click here to submit your choice'

gm_reg_npbp_tx = 'When you are done (and sure), click this button'
top_entry_label_tx = 'Hold on ... setting up all the necessary slots and tables for the game ...'
gm_card_wait_1_temp_title_tx = 'Still waiting for the following to log in ...'
gm_card_wait_1_info_tx = "All roles have been set up now. \nTell your players to log in, to look at the state of their region for last 45 years and discuss their decisions to improve the lives of their people. You can check if all have logged in by clicking on the **Check LogIn** button. Once they are ready to proceed to the next round **---** *this will take some time!* **---**, click on the **Advance the model for the next round** button."
gm_card_wait_1_btn_check_tx = 'Check LogIn'
gm_card_wait_1_btn_kick_off_round_1_tx = 'Advance model for the next round'
setup_npbp_label_tx = '... Hold on ... Role assignments are being set up ...'
#    msg = 'Role assignments are set up ... Now tell your players to join game ' + cid + ' and log in to their roles. You need to wait until all players have submitted their decisions for round 1, 2025 to 2040'
pcr_submit_msg1 = "Congratulations, you have been confirmed as "
pcr_submit_msg2 = ' in '
pcr_submit_msg3 = 'Your personal Game ID is: '

pcgd_rd1_info_tx = "You are responsible to better the lives of your people. In the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry - social unrest, and worse, is just around the corner!\nStudy all your indicators, see how they develop over the years, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, scroll down to the decisions you need to take as minister that hopefully improve the lives of your citizens in the next round."
pcgd_generating_tx = "... generating your graphs and decisionsheet ..."
show_hide_plots_hide_tx = "Hide graphs"
show_hide_plots_show_tx = "Show graphs"

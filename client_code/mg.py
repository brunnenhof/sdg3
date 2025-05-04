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
  "eu" : "Europe",
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
"FMPLDD" : "Poverty",
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
top_btn_thanks = 'Thanks'
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
fut_not_all_logged_in_tx = "Not all of your regional ministerial colleagues have logged in yet. Wait until they have done so."
no_active_game_to_join_tx = "no active game to join ... the game organizer has to start one"

gm_reg_npbp_tx = 'When you are done (and sure), click this button'
top_entry_label_tx = 'Hold on, setting up all the necessary slots, templates and tables for the game ...'
gm_card_wait_1_temp_title_tx = 'Still waiting for the following ministers to log in ... Ask if they need help ...'
gm_card_wait_1_temp_title_tx2 = 'All logged in! By clicking on the "Ready to advance" button, you can check if all your regions have submitted their policies. Tell them how much time they still have.'
gm_card_wait_1_info_tx = "All roles have been set up now. \nTell your players to log in, to look at the state of their region for last 45 years and discuss their decisions to improve the lives of their people. Check repeatedly if all your players have logged in by clicking the **Check LogIn** button. Once they are ready to proceed to the next round **---** *this will take some time!* **---** click on the **Advance the model for the next round** button. If the *advance* button does not show, your players are not ready yet."
gm_card_wait_1_btn_check_tx = 'Check LogIn'
gm_card_wait_1_btn_kick_off_round_1_tx = 'Ready to advance the model for the next round?'
gm_wait_kickoff_r1_tx = 'Still waiting for the region(s) below to submit their decisions ... You may want to ask if they need help ...'
gm_wait_round_done_tx = 'The model has been advanced. Tell your players to click on the \n"Get the results ... " or \n"Check if the game leader ..." button.'
gm_wait_round_done_tx2 = 'The model has been advanced. Tell your players to study and discuss their results, within and between regions. Are things going the right way? \nThen, they should decide on the policies for the next round. When they are ready, the Minister for the Future should submit their regional decisions. Tell them how much time they have.'
gm_wait_round_done_tx3 = 'The model has been advanced to the end, the year 2100. Tell your players to study and discuss their results, within and between regions. Are things going the right way? Are they safisfied? Are their citizens satisfied? Is the earth still habitable? \nFinally, take them out of the game back to the here and now; and start your debriefing.'
sim_success_tx1 = '...the model ran successfully to 2040, but we are waiting for the decisions for 2040-2060.\nHave you set all your policy decisions?'
sim_success_tx1 = '...the model ran successfully to 2060, but we are waiting for the decisions for 2060-2100.\nHave you set all your policy decisions?'
sim_success_title_tx = 'Waiting'
pcgd_generating_tx1 = "Generating graphs until 2040 and decision sheet for 2040"
pcgd_generating_tx2 = "Generating graphs until 2060 and decision sheet for 2060"
pcgd_generating_tx3 = "Generating graphs until 2100"

gm_wait_round_started_tx = 'The simulation started. Please wait until it is done...'
gm_start_round_tx_2 = "Check if all regions are ready to advance to 2060 ..."
gm_start_round_tx_3 = "Check if all regions are ready to advance to 2100 ..."
waiting_for_gm_to_start_round = "... for simulation to start ..."
gm_wait_sub2_tx = "... for all submissions for the round 2040 to 2060 ..."
gm_wait_sub3_tx = "... for all submissions for the round 2060 to 2100 ..."
setup_npbp_label_tx = 'Hold on, all roles are being prepared ...'
#    msg = 'Role assignments are set up ... Now tell your players to join game ' + cid + ' and log in to their roles. You need to wait until all players have submitted their decisions for round 1, 2025 to 2040'
pcr_submit_title = "Congratulations!"
pcr_submit_msg1 = "You have been confirmed as "
fut_title_tx2 = ""
pcr_submit_msg2 = ' in '
pcr_submit_msg3 = 'Your personal Game ID is: '
player_board_tx = "Player Board: "

pcgd_rd1_info_tx = "You are responsible to better the lives of your people. In the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry - social unrest, and worse, is just around the corner!\nStudy all your indicators, see how they develop over the years, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, scroll down to the decisions you need to take as minister that hopefully improve the lives of your citizens in the next round."
pcgd_rd1_info_short = "Together with your ministerial team, you are responsible to better the lives of your people. In the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry - social unrest, and worse, is just around the corner!\nStudy all your indicators, see how they develop over the years, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, scroll down to see the investment plans of your colleagues. Make sure they are within your regional budget. More instructions are below the graphs."
pcgd_rd1_info_end = "**Outfade**"
pcgd_rd1_info_fut_tx = "As Minister for the Future, you see the big picture. You also see how much your ministerial colleagues in your region plan to invest in total to improve the lives of your people and the health of the planet. \nIt is **your** task to keep the **total regional investment** within the budget. If *total investment* is **below** 100 % of the budget, all is well. Although if you invest too little, things may get worse, much worse possibly!\nIf it is **above** 100 % of your budget, you need to advise your ministerial colleagues to reduce some of their investments. This is a difficult task where your moderating skills are needed. Good luck!\nAs your ministerial colleagues decide on their investment plans, click on the **Refresh Numbers** button to see the most up to date choices of your colleagues.\nWhen you are all ready, **you**, as Minister for the Future, submit the policy choices from all your colleagues - **be sure to get all their OKs** before you hit the *Submit* button! (*Note:* if the Submit button does not show, it is because your region is above the the budget.\nMoney amounts are in constant (2025) Giga $ per year. A 'Giga' is 1,000,000,000 ----- US Americans call this a Billion, others call this a Milliarde."
pcgd_rd1_info_end_tx = "pcgd_rd1_info_end_tx *outtake*"
pcgd_generating_tx = "... generating your graphs and decisionsheet ..."
show_hide_plots_hide_tx = "Hide graphs"
show_hide_plots_show_tx = "Show graphs"
pcgd_advance_tx = "Check if the model has been advanced  "
pcgd_info_after_rd1_tx = "The model has been simulated until 2040. Again, in the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry!\nStudy all your indicators, see how they develop over the years. *Given your policy choices, did you expect something different? Are surprised?* Again, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, and in light of what happenend in the last round, scroll down to the decisions you need to take as minister that hopefully improve the lives of your citizens in the next round."
not_to_2060 = "The model has not yet been advanced to 2060."
dec_info_tx = "After looking at the situation for your people, you must enact several policies to improve the lives of your people **and** the health of the planet. You know that people cannot thrive on a sick planet. You set the policy by pulling the sliders. After coordinating with your ministerial colleagues, set the slider for each policy. \n\nEach policy has an **investment cost** attached to it. If you set a slider to its minimum, there is no cost, if you set a slider to its maximum, then the full investment cost is due. If you set the slider somewhere between minimum and maximum, the prorated investment cost is due. Your region also has a budget for **all** investments from **all** ministries. \n\nIf you exceed the budget, your colleague, the Minister for the Future, will tell you so and you must re-negotiate with your colleagues, until the total regional investment is below or equal to the budget.\n\nWhen the cabinet of your region is **a)** within the budget and **b)** you are **all** satisfied with your choices, the Minister for the Future will submit all your decisions to the game leader so that the model can be advanced for the next round."
dec_title_tx = "Set your policies"

fut_info_tx = "As Minister for the Future, you see the big picture. You also see how much your ministerial colleagues in your region plan to invest in total to improve the lives of your people and the health of the planet.\n\nIt is **your** task to keep the **total regional investment** within the budget. If *total investment* is **below** 100 % of the budget, all is well. Although if you invest too little, things may get worse, much worse possibly!\n\nIf it is **above** 100 % of your budget, you need to advise your ministerial colleagues to reduce some of their investments. This is a difficult task where your moderating skills are needed. Good luck!\n\nAs your ministerial colleagues decide on their investment plans, click on the **Refresh Numbers** button to see the most up to date choices of your colleagues.\n\nWhen you are all ready, **you**, as Minister for the Future, submit the policy choices from all your colleagues - **be sure to get all their OKs** before you hit the *Submit* button! (*Note:* if the Submit button does not show, it is because your region is above the the budget.\n\nMoney amounts are in constant (2025) Giga $ per year. A *Giga* is 1,000,000,000 ----- US Americans call this a Billion, others call this a Milliarde."
fut_bud_lb1_tx = "Your total budget:"
fut_bud_lb2_tx = "All the investment plans of all your fellow ministers summed up:"
fut_bud_lb3_tx = "Investment plans as % of your budget"
cfpov_tx = "Poverty"
cfpov_lb_tx = "Regional investment plans against poverty:"
cfineq_tx = "Inequality"
cfineq_lb_tx = "Regional investment plans against inequality:"
cfemp_tx = "Empowerment"
cfemp_lb_tx = "Regional investment plans for empowerment:"
cffood_tx = "Food & agriculture"
cffood_lb_tx = "Regional investment for food and agriculture:"
cfener_tx = "Energy"
cfener_lb_tx = "Regional investment for energy:"
refresh_numbers_tx = "RFRESH numbers"
submit_numbers_tx = "SUBMIT numbers"

confirm_submit_tx = "Yes to submit, No to go back"
confirm_title_tx = "Last chance to go back."
confirm_buttons_tx = [
                 ("Yes", "YES"),
                 ("No", "NO")
               ]
after_submit_tx = "Your region's decisions have been submitted - thanks!\nOnce all regions have submitted their decisons, the model will be advanced for the next round. This will take a bit of time ..."
nothing_submitted_tx = "Nothing was submitted ..."
p_advance_to_next_round_tx = "Get the results until 2040 and the decision sheet for 2040-2060 - your children's future"
p_advance_to_1_tx = "Get the results until 2060 and the decision sheet for 2060-2100 - your grandchildren's future"
p_advance_to_2_tx = "Get the results until the end of the century"
p_waiting_model_run_tx = "... still waiting for the GM to advance the model ..."
waiting_tx = "Waiting ..."

plot_glob_mg = ['Temp surface anomaly compared to 1850 degC', 'pH in surface', 'TROP with normal cover',
                          'Planetary risk']
plot_reg_mg = ['Energy footprint pp', 'Fraction of population undernourished',
                'Cost_per_regional_poverty_policy',
                'RoC in Forest land', 'Total energy use per GDP',
                'Years of schooling', 'All SDG Scores', 'RoC Populated land', 'Public services pp',
                'Safe sanitation',
                'Smoothed RoC in GDPpp', 'Fraction of population below existential minimum',
                'Regenerative cropland fraction',
                'Total government revenue as a proportion of GDP', 'El from wind and PV',
                'Labour share of GDP',
                'Cropland', 'Smoothed Social tension index with trust effect', 'LPB investment share',
                'Food footprint kgN ppy',
                'Life expectancy at birth', 'GenderEquality', 'Social trust',
                'Total CO2 emissions', 'Safe water', 'Access to electricity',
                'Carbon intensity', 'Disposable income pp post tax pre loan impact', 'Population',
                'Average wellbeing index',
                'Local private and govt investment share', 'Unemployment rate smoothed',
                'Renewable energy share in the total final energy consumption', 'GDP USED',
                'Nitrogen use per ha',
                'Budget_for_all_TA_per_region', 'Cost_per_regional_inequality_policy',
                'Cost_per_regional_empowerment_policy',
                'Cost_per_regional_food_policy', 'Cost_per_regional_energy_policy']
my_col_mg = ['blue', 'brown', 'red', 'mediumpurple', 'khaki', 'purple', 'darkgreen', 'magenta', 'green', 'orange']

not_all_submitted_tx = "Not all regions have submitted their decisions ..."
not_all_submitted_p_tx = "Not all regions have submitted their decisions, your game leader knows who we are waiting for ..."
not_all_submitted_gm_tx = "Not all regions have submitted their decisions ..."
all_submitted_p_tx = "ALL regions HAVE submitted their decisions, your game leader will advance the model shortly and let you know when your results are ready"
running_model_tx = "... advancing the model ..."

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

Pov_to_pov = {
  "Poverty": "pov",
  "Inequality": "ineq",
  "Empowerment": "emp",
  "Food": "food",
  "Energy": "ener",
  "Future": "fut"
}
pov_to_Poverty = {
  "pov": "Poverty",
  "ineq": "Inequality",
  "emp": "Empowerment",
  "food": "Food",
  "ener": "Energy",
  "fut": "Future"
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

#############
############# English
#############
reg_to_longreg_en = {
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
ta_to_longmini_en = {
  "pov" : "Minister against Poverty",
  "ineq" : "Minister against Inequality",
  "emp" : "Minister for Empowerment",
  "food" : "Minister for Food & Agriculture",
  "ener" : "Minister for Energy",
  "fut" : "Minister for the Future"
}
pol_to_expl_en = {
  "CCS" : "Percent of fossil use to be equipped with carbon capture and storage (CCS) at source.  This means that you still emit CO2 but it does not get to the atmosphere, where it causes warming,  because you capture it and store it underground.",
  "TOW" : "0 means no wealth tax,  80 means 80% of accrued owners wealth is taxed away each year,  50: half of it",
  "FPGDC" : "Cancels a percentage of Govt debt outstanding to public lenders. 0 means nothing is cancelled,  100 all is cancelled,  50 half is cancelled --- in the policy start year",
  "RMDR" : "Change in diet, esp. a reduction in red meat consumption. 0 means red meat is consumed as before, 50 means 50% is replaced with lab meat, 100 means 100% is replaced with lab meat  i.e. no more red meat is 'produced' by intensive livestock farming  aka factory farming.",
  "REFOREST" : "Policy to reforest land, i.e. plant new trees. 0 means no reforestation, 1 means you increase the forest area by 1â€° / yr (that is 1 promille), 3 = you increase the forest area by 3â€° / yr",
  "FTPEE" : "Annual percentage increase in energy efficiency; 1% per yr is the historical value over the last 40 years. Beware of the power of compound interest!",
  "LPBsplit" : "0 means all LBP funding goes to consumption (eg child support,  subsidies for food or energy,  etc.)  100 means all goes to public investment like infrastructure,  security,  etc. NOTE This only has an effect if LPB is NOT set to zero",
  "ExPS" : "Cancels a percentage of Govt debt outstanding to private lenders --- in the policy start year",
  "FMPLDD" : "Given your credit worthiness  you have an amount you you can borrow from private lenders. Here you choose the fraction of credit you actually draw down each year.",
  "StrUP" : "In any economy, the national income is shared between owners and workers. This policy changes the share going to workers. 1 multiplies the share with 1%,  2 with 2%,  etc ",
  "Wreaction" : "In any economy, there is a power struggle between workers and owners about the share of national income each gets. This policy strenghtens the workers negotiation position. 1 by 1%,  2 by 2%,  etc. ",
  "SGMP" : "To fight poverty in old age  you can introduce pensions for all. The size of the pension is expressed as the percent of the GDP you want to invest. 0 means you invest nothing and leave things as they are. 5 means you invest 5 % of GDP; 10 = 10 % of GDP  money is transferred to workers and paid for by owners",
  "FWRP" : "Here you decide how much the percentage of 'normal' waste, which is 30%, is to be reduced. I.e. 100 means  no more waste! 50 means waste is reduced by 50 %,  0 means waste continues as always",
  "ICTR" : "This policy is an increase in the consumption tax (aka sales tax, value added tax (VAT),  etc. 0 means no increase, 10 means an increase by 10 percentage points, 5 by 5 percentage points; the money raised goes to general govt revenue.",
  "XtaxCom" : "A universal basic dividend is created when a state taxes common goods  like fishing rights, mining rights, the right to use airwaves  etc. This policy sets this tax as a percent of GDP  i.e.  0 = 0 % of GDP  i.e. nothing; 5 = 5 % of GDP; 3 = 3 % of GDP  money is transferred to general govt tax revenue.",
  "Lfrac" : "Leakage describes the use of money for illicit purposes: Corruption,  bribery,  etc. The normal leakage is 20%  - so a value of 0 reduction means that those 20% do in fact disappear - a 50 % reduction means 10% disappear and 100% reduction means nothing disappears and everyone in your region is totally honest!",
  "IOITR" : "This is an increase in the income tax paid by owners. 0 means no increase,  10 means an increase by 10 percentage points, 5 by 5 percentage points; the money raised goes to general govt revenue.",
  "IWITR" : "This is an increase in the income tax paid by workers. 0 means no increase, 10 means an increase by 10 percentage points, 5 by 5 percentage points; the money raised goes to general govt revenue.",
  "SGRPI" : "Governments choose how to use their spending: primarily for consumption (eg child support, subsidies for food or energy, etc.) or for public investment (education, health care, infrastructure  etc.) This policy shifts spending from consumption to investment. 0 means no shift, 10= 10% of consumption shifted to investment, 25 = 25 % of consumption shifted to investment, etc",
  "FEHC" : "The higher the level of education  esp. of women,  in a society,  the lower the birth rate. Thus  education for all lowers the birth rate. By how much? You make an educated guess: 0 means no effect, 10 means a 10% reduction, 5 means a 5% reduction, etc.",
  "XtaxRateEmp" : "To support women to reach equality costs some money, esp. to close the pay gender gap. How much do you want to spend  as a pct of GDP? 0 means you spend nothing and leave things as they are; 5 means you spend= 5 % of GDP; 3 = 3 % of GDP. Money is transferred to general govt tax revenue",
  "FLWR" : "Here you decide the percentage of your cropland that is worked regeneratively (low or no tillage,  low or no fertilizers and pesticides  etc.)  50 means 50 % cropland worked is regeneratively, 100 = 100 % of cropland is worked regeneratively, etc. 0 leaves things as they are.",
  "RIPLGF" : "Reduction in food imports. 0 means no reduction,  10=10% reduction, 50=50% reduction This policy reduces food available from elsewhere but strenghtens local producers",
  "FC" : "Policy to limit forest cutting. 0 means no limitation on cutting,  10=10% reduction in the maximum amount that can be cut,  50=50% reduction in max cut, etc. all the way to 90 % reduction which is practically a ban on cutting",
  "NEP" : "Percent of fossil fuel (oil, gas, and coal) *not* used for electricity generation (mobility,  heating,  industrial use  etc.) that you want to electrify.",
  "Ctax" : "This is the carbon emission tax. 0 means no carbon tax,  25 = 25 $/ton of CO2 emitted  etc.",
  "DAC" : "Capturing CO2 that is already in the atmosphere and storing it underground   - in GtCO2/yr (Giga tons -  giga is 10^9); In 2020  regional emissions were roughly: USA 5,  Africa  south of Sahara 1,  China 12,  the rest all between 2 and 3 GtCO2/yr. You can capture more than you emit.",
  "XtaxFrac" : "The percentage of *extra* taxes paid by owners (owners pay 50% of extra taxes even under TLTL)  I.e. 90 means owners pay 90 % of extra taxes,  70 means owners pay 70 % of extra taxes, etc. Extra taxes are those for empowerment and to give women equal pay.",
  "LPBgrant" : "0 means all LPB funding is given as loans that must be repaid,  100 means all is given as grants that carry no interest and must not be repaid. NOTE This only has an effect if LPB is NOT set to zero",
  "LPB" : "The percentage of your GDP made available as financing from public bodies (WorldBank,  IMF,  off-balance funding) LPB= Lending from Public Bodies",
  "SSGDR" : "You can stretch repayment into the future  so that each year you pay less,  but you do have to pay for a longer time. 1 means no stretching - 2 doubles repayment time  - 3 trebles repayment time - and so on",
  "ISPV" : "Percent of electricity generation from renewable sources (40% is what we managed to achieve in the past)"
}
pol_to_name_en = {
  "CCS" : "CCS: Carbon capture and storage at source",
  "TOW" : "Taxing Owners Wealth",
  "FPGDC" : "Cancel debt from public lenders",
  "RMDR" : "Change diets",
  "REFOREST" : "Reforestation",
  "FTPEE" : "Energy system efficiency",
  "LPBsplit" : "LPB: Split the use of funds from public lenders",
  "ExPS" : "Expand policy space",
  "FMPLDD" : "Fraction of credit with private lenders NOT drawn down per y",
  "StrUP" : "Strengthen Unions",
  "Wreaction" : "Worker reaction",
  "SGMP" : "Pensions to all",
  "FWRP" : "Food waste reduction",
  "ICTR" : "Increase consumption tax rate",
  "XtaxCom" : "Introduce a Universal basic dividend",
  "Lfrac" : "Leakage fraction reduction",
  "IOITR" : "Increase owner income tax rate",
  "IWITR" : "Increase worker income tax rate",
  "SGRPI" : "Shift govt spending to investment",
  "FEHC" : "Education to all",
  "XtaxRateEmp" : "Female leadership",
  "FLWR" : "Regenerative agriculture",
  "RIPLGF" : "Reduce food imports",
  "FC" : "Max forest cutting",
  "NEP" : "Electrify everything",
  "Ctax" : "Introduce a Carbon tax",
  "DAC" : "Direct air capture",
  "XtaxFrac" : "Extra taxes paid by the super rich",
  "LPBgrant" : "LPB: funds given as loans or grants",
  "LPB" : "Lending from public bodies (LPB)",
  "SSGDR" : "Stretch repayment",
  "ISPV" : "Invest in Renewables"
}
sdgvarID_to_subtitle_en = {
  "13" : "Worker disposable income (1000 $/person-year)",
  "18" : "Fertilizer use per capita (Mt/y)",
  "26" : "Population (million people)",
  "19" : "Temperature rise (deg C above 1850)",
  "20" : "Total greenhouse gas emissions per year (GtCO2/yr)",
  "29" : "Number of SDGs met 17 can be met",
  "4" : "Average wellbeing index",
  "24" : "Trust in institutions (1980=1)",
  "31" : "Annual rate of change in city area (%)",
  "33" : "Annual change in forest area (%)",
  "35" : "Planetary boundaries breached",
  "30" : "Private and govt investment share (% of GDP)",
  "9" : "Percent of population with access to safe sanitation (%)",
  "16" : "Growth rate of GDP per capita (%/yr)",
  "17" : "Emissions per person (tCO2/p/y)",
  "34" : "Donor and off balance-sheet investment share (% of GDP)",
  "14" : "Million unemployed",
  "21" : "Ocean surface pH",
  "12" : "Energy intensity in terms of primary energy and GDP (kWh/$)",
  "22" : "Extent of tropical forest globally (Mha)",
  "23" : "Public services per person (1000 $/person-yr)",
  "2" : "Million people undernourished (Mp)",
  "5" : "Life expectancy (years)",
  "7" : "Female pre-tax labor income share (%)",
  "1" : "Million people living in poverty (Mp)",
  "3" : "Million hectars worked regeneratively",
  "6" : "Years in school",
  "8" : "Percent of population with access to safe water (%)",
  "10" : "Million people with no access to electricity (Mp)",
  "15" : "Carbon intensity of production (kgCO2/$)",
  "25" : "Total government revenue as a proportion of GDP (%)",
  "27" : "Labour share of GDP (%)",
  "28" : "Wind and PV energy electricity (TWh/yr)",
  "37" : "Cropland (Mha)",
  "11" : "Wind and PV energy electricity (TWh/yr)",
  "36" : "GDP (G2017ppp$/yr)",
  "32" : "Nitrogen use (kg/ha-year)",
  "39" : "nan",
  "38" : "nan"
}
sdgvarID_to_indicator_en = {
  "13" : "Worker disposable income (1000 USD/person-year)",
  "18" : "Fertilizer use per capita (Mt/y)",
  "26" : "Population (million people)",
  "19" : "Temperature rise (deg C above 1850)",
  "20" : "Total greenhouse gas emissions per year (GtCO2/yr)",
  "29" : "Number of SDGs met: 17 can be met",
  "4" : "Average wellbeing index",
  "24" : "Trust in institutions (1980=1)",
  "31" : "Annual rate of change in city area (%)",
  "33" : "Annual change in forest area (%)",
  "35" : "Planetary boundaries breached",
  "30" : "Private and govt investment share (% of GDP)",
  "9" : "Fraction of population with access to safe sanitation (%)",
  "16" : "Growth rate of GDP per capita (%/yr)",
  "17" : "Emissions per person (tCO2 per person-year)",
  "34" : "Donor and off balance-sheet investment share (% of GDP)",
  "14" : "Unemployment rate (%)",
  "21" : "Ocean surface pH",
  "12" : "Energy intensity in terms of primary energy and GDP (kWh/$)",
  "22" : "Extent of tropical forest globally (Mha)",
  "23" : "Public services per person (1000 $/person-yr)",
  "2" : "Fraction of population undernourished (%)",
  "5" : "Life expectancy (years)",
  "7" : "Female pre-tax labor income share (%)",
  "1" : "Fraction of population living below $6.85 per day (%)",
  "3" : "Proportion of agricultural area worked regeneratively (%)",
  "6" : "Years in school",
  "8" : "Fraction of population with access to safe water (%)",
  "10" : "Fraction of population with access to electricity (%)",
  "15" : "Carbon intensity of production (kgCO2 per USD)",
  "25" : "Total government revenue as a proportion of GDP (%)",
  "27" : "Labour share of GDP (%)",
  "28" : "Wind and PV energy electricity (TWh/yr)",
  "37" : "Cropland (Mha)",
  "11" : "Wind and PV energy share in total energy consumption (%)",
  "36" : "GDP (G2017ppp$/yr)",
  "32" : "Nitrogen use (kg/ha-year)",
  "39" : "(index)",
  "38" : "(index)"
}
sdgvarID_to_sdg_en = {
  "13" : "Decent work and economic growth",
  "18" : "Responsible consumption and production",
  "26" : "Total population",
  "19" : "Climate action",
  "20" : "Climate action",
  "29" : "SDG scores",
  "4" : "Good health and wellbeing",
  "24" : "Partnership for the Goals",
  "31" : "Sustainable cities and communities",
  "33" : "Life on land",
  "35" : "Planetary boundaries",
  "30" : "Industry innovation and infrastructure",
  "9" : "Access to clean sanitation",
  "16" : "Decent work and economic growth",
  "17" : "Sustainable cities and communities",
  "34" : "Industry innovation and infrastructure",
  "14" : "Decent work and economic growth",
  "21" : "Life below water",
  "12" : "Affordable and clean energy",
  "22" : "Life on land",
  "23" : "Peace justice and strong institutions",
  "2" : "No hunger",
  "5" : "Good health and wellbeing",
  "7" : "Gender equality",
  "1" : "No poverty",
  "3" : "No hunger",
  "6" : "Quality education",
  "8" : "Access to clean water",
  "10" : "Affordable and clean energy",
  "15" : "Industry innovation and infrastructure",
  "25" : "Partnership for the Goals",
  "27" : "Reduced inequalities",
  "28" : "Affordable and clean energy",
  "37" : "Cropland",
  "11" : "Affordable and clean energy",
  "36" : "GDP",
  "32" : "Responsible consumption and production",
  "39" : "Social tension",
  "38" : "Social trust"
}
top_title_en = 'LT Game'
top_btn_thanks_en = 'Thanks'
top_btn_start_en = 'Start a new game as organizer'
top_btn_join_en = 'JOIN a game as player'
top_btn_help_en = 'Help'
top_join_game_en = 'JOIN a game as player'
top_start_game_en = 'Start a game as organizer'
p_lb_choose_game_en = 'There are more than one open games. First select the one you want to join, then press the JOIN button:'
p_btn_select_game_en = 'JOIN'
gm_id_msg1_en = "Your game ID is "
gm_id_msg2_en = ". Make a note of it and tell your players."
gm_id_title_en = "Your game ID:"
top_thanks_msg_en = "... to our Alpha testers, the students in the SW101 course at the Realschule Baesweiler during April 2024 taught by René Langohr, and all the beta testers."
top_thanks_title_en = "Thank you ... "
top_roles_setup_msg_en = "Roles template has been set up for "
title_you_are_joining_en = "You are joining: "
msg_game_not_started_en = "The game organizer has not yet started a game. Please wait until he/she does ..."
msg_gm_board_en = "Game Organizer Board"
msg_gm_board_info_en = "**Now, click on *all* the regions *not* played by your players (eg if there are not enough players for all roles)**"
cb_us_tx_en = 'USA'
cb_af_tx_en = 'Africa, South of Sahara'
cb_cn_tx_en = 'China'
cb_me_tx_en = 'Middle East - North Africa'
cb_sa_tx_en = 'South Asia'
cb_la_tx_en = 'Latin America'
cb_pa_tx_en = 'Pacific Rim'
cb_ec_tx_en = 'East Europe - Central Asia'
cb_eu_tx_en = 'Europe'
cb_se_tx_en = 'Southeast Asia'
cb_pov_tx_en = 'Poverty'
cb_ineq_tx_en = 'Inequality'
cb_emp_tx_en = 'Empowerment'
cb_food_tx_en = 'Food & agriculture'
cb_ener_tx_en = 'Energy'
cb_fut_tx_en = 'Future'
pcr_title_tx_en = 'Player Board Game '
pcr_col_left_title_tx_en = 'First, log into your region ...'
pcr_col_right_title_tx_en = '... then into your role as minister ...'
pcr_submit_tx_en = 'Once you have logged in to both your region and your ministry, click here to submit your choice'
fut_not_all_logged_in_tx_en = "Not all of your regional ministerial colleagues have logged in yet. Wait until they have done so."
no_active_game_to_join_tx_en = "no active game to join ... the game organizer has to start one"
gm_reg_npbp_tx_en = 'When you are done (and sure), click this button'
top_entry_label_tx_en = 'Hold on, setting up all the necessary slots, templates and tables for the game ...'
gm_card_wait_1_temp_title_tx_en = 'Still waiting for the following ministers to log in ... Ask if they need help ...'
gm_card_wait_1_temp_title_tx2_en = 'All logged in! By clicking on the "Ready to advance" button, you can check if all your regions have submitted their policies. Tell them how much time they still have.'
gm_card_wait_1_info_tx_en = "All roles have been set up now. \nTell your players to log in, to look at the state of their region for last 45 years and discuss their decisions to improve the lives of their people. Check repeatedly if all your players have logged in by clicking the **Check LogIn** button. Once they are ready to proceed to the next round **---** *this will take some time!* **---** click on the **Advance the model for the next round** button. If the *advance* button does not show, your players are not ready yet."
gm_card_wait_1_btn_check_tx_en = 'Check LogIn'
gm_card_wait_1_btn_kick_off_round_1_tx_en = 'Ready to advance the model for the next round?'
gm_wait_kickoff_r1_tx_en = 'Still waiting for the region(s) below to submit their decisions ... You may want to ask if they need help ...'
gm_wait_round_done_tx_en = 'The model has been advanced. Tell your players to click on the \n"Get the results ... " or \n"Check if the game leader ..." button.'
gm_wait_round_done_tx2_en = 'The model has been advanced. Tell your players to study and discuss their results, within and between regions. Are things going the right way? \nThen, they should decide on the policies for the next round. When they are ready, the Minister for the Future should submit their regional decisions. Tell them how much time they have.'
gm_wait_round_done_tx3_en = 'The model has been advanced to the end, the year 2100. Tell your players to study and discuss their results, within and between regions. Are things going the right way? Are they safisfied? Are their citizens satisfied? Is the earth still habitable? \nFinally, take them out of the game back to the here and now; and start your debriefing.'
sim_success_tx1_en = '...the model ran successfully to 2040, but we are waiting for the decisions for 2040-2060.\nHave you set all your policy decisions?'
sim_success_tx1_en = '...the model ran successfully to 2060, but we are waiting for the decisions for 2060-2100.\nHave you set all your policy decisions?'
sim_success_title_tx_en = 'Waiting'
pcgd_generating_tx1_en = "Generating graphs until 2040 and decision sheet for 2040"
pcgd_generating_tx2_en = "Generating graphs until 2060 and decision sheet for 2060"
pcgd_generating_tx3_en = "Generating graphs until 2100"
gm_wait_round_started_tx_en = 'The simulation started. Please wait until it is done...'
gm_start_round_tx_2_en = "Check if all regions are ready to advance to 2060 ..."
gm_start_round_tx_3_en = "Check if all regions are ready to advance to 2100 ..."
waiting_for_gm_to_start_round_en = "... for simulation to start ..."
gm_wait_sub2_tx_en = "... for all submissions for the round 2040 to 2060 ..."
gm_wait_sub3_tx_en = "... for all submissions for the round 2060 to 2100 ..."
setup_npbp_label_tx_en = 'Hold on, all roles are being prepared ...'
#  msg_en = 'Role assignments are set up ... Now tell your players to join game ' + cid + ' and log in to their roles. You need to wait until all players have submitted their decisions for round 1, 2025 to 2040'
pcr_submit_title_en = "Congratulations!"
pcr_submit_msg1_en = "You have been confirmed as "
fut_title_tx2_en = ""
pcr_submit_msg2_en = ' in '
pcr_submit_msg3_en = 'Your personal Game ID is: '
player_board_tx_en = "Player Board: "
pcgd_rd1_info_tx_en = "You are responsible to better the lives of your people. In the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry - social unrest, and worse, is just around the corner!\nStudy all your indicators, see how they develop over the years, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, scroll down to the decisions you need to take as minister that hopefully improve the lives of your citizens in the next round."
pcgd_rd1_info_short_en = "Together with your ministerial team, you are responsible to better the lives of your people. In the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry - social unrest, and worse, is just around the corner!\nStudy all your indicators, see how they develop over the years, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, scroll down to see the investment plans of your colleagues. Make sure they are within your regional budget. More instructions are below the graphs."
pcgd_rd1_info_end_en = "**Outfade**"
pcgd_rd1_info_fut_tx_en = "As Minister for the Future, you see the big picture. You also see how much your ministerial colleagues in your region plan to invest in total to improve the lives of your people and the health of the planet. \nIt is **your** task to keep the **total regional investment** within the budget. If *total investment* is **below** 100 % of the budget, all is well. Although if you invest too little, things may get worse, much worse possibly!\nIf it is **above** 100 % of your budget, you need to advise your ministerial colleagues to reduce some of their investments. This is a difficult task where your moderating skills are needed. Good luck!\nAs your ministerial colleagues decide on their investment plans, click on the **Refresh Numbers** button to see the most up to date choices of your colleagues.\nWhen you are all ready, **you**, as Minister for the Future, submit the policy choices from all your colleagues - **be sure to get all their OKs** before you hit the *Submit* button! (*Note:* if the Submit button does not show, it is because your region is above the the budget.\nMoney amounts are in constant (2025) Giga $ per year. A 'Giga' is 1,000,000,000 ----- US Americans call this a Billion, others call this a Milliarde."
pcgd_rd1_info_end_tx_en = "pcgd_rd1_info_end_tx *outtake*"
pcgd_generating_tx_en = "... generating your graphs and decisionsheet ..."
show_hide_plots_hide_tx_en = "Hide graphs"
show_hide_plots_show_tx_en = "Show graphs"
pcgd_advance_tx_en = "Check if the model has been advanced "
pcgd_info_after_rd1_tx_en = "The model has been simulated until 2040. Again, in the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry!\nStudy all your indicators, see how they develop over the years. *Given your policy choices, did you expect something different? Are surprised?* Again, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, and in light of what happenend in the last round, scroll down to the decisions you need to take as minister that hopefully improve the lives of your citizens in the next round."
not_to_2060_en = "The model has not yet been advanced to 2060."
dec_info_tx_en = "After looking at the situation for your people, you must enact several policies to improve the lives of your people **and** the health of the planet. You know that people cannot thrive on a sick planet. You set the policy by pulling the sliders. After coordinating with your ministerial colleagues, set the slider for each policy. \n\nEach policy has an **investment cost** attached to it. If you set a slider to its minimum, there is no cost, if you set a slider to its maximum, then the full investment cost is due. If you set the slider somewhere between minimum and maximum, the prorated investment cost is due. Your region also has a budget for **all** investments from **all** ministries. \n\nIf you exceed the budget, your colleague, the Minister for the Future, will tell you so and you must re-negotiate with your colleagues, until the total regional investment is below or equal to the budget.\n\nWhen the cabinet of your region is **a)** within the budget and **b)** you are **all** satisfied with your choices, the Minister for the Future will submit all your decisions to the game leader so that the model can be advanced for the next round."
dec_title_tx_en = "Set your policies"
fut_info_tx_en = "As Minister for the Future, you see the big picture. You also see how much your ministerial colleagues in your region plan to invest in total to improve the lives of your people and the health of the planet.\n\nIt is **your** task to keep the **total regional investment** within the budget. If *total investment* is **below** 100 % of the budget, all is well. Although if you invest too little, things may get worse, much worse possibly!\n\nIf it is **above** 100 % of your budget, you need to advise your ministerial colleagues to reduce some of their investments. This is a difficult task where your moderating skills are needed. Good luck!\n\nAs your ministerial colleagues decide on their investment plans, click on the **Refresh Numbers** button to see the most up to date choices of your colleagues.\n\nWhen you are all ready, **you**, as Minister for the Future, submit the policy choices from all your colleagues - **be sure to get all their OKs** before you hit the *Submit* button! (*Note:* if the Submit button does not show, it is because your region is above the the budget.\n\nMoney amounts are in constant (2025) Giga $ per year. A *Giga* is 1,000,000,000 ----- US Americans call this a Billion, others call this a Milliarde."
fut_bud_lb1_tx_en = "Your total budget:"
fut_bud_lb2_tx_en = "All the investment plans of all your fellow ministers summed up:"
fut_bud_lb3_tx_en = "Investment plans as % of your budget"
cfpov_tx_en = "Poverty"
cfpov_lb_tx_en = "Regional investment plans against poverty:"
cfineq_tx_en = "Inequality"
cfineq_lb_tx_en = "Regional investment plans against inequality:"
cfemp_tx_en = "Empowerment"
cfemp_lb_tx_en = "Regional investment plans for empowerment:"
cffood_tx_en = "Food & agriculture"
cffood_lb_tx_en = "Regional investment for food and agriculture:"
cfener_tx_en = "Energy"
cfener_lb_tx_en = "Regional investment for energy:"
refresh_numbers_tx_en = "RFRESH numbers"
submit_numbers_tx_en = "SUBMIT numbers"
confirm_submit_tx_en = "Yes to submit, No to go back"
confirm_title_tx_en = "Last chance to go back."
confirm_buttons_tx_en = [  ("Yes", "YES"),  ("No", "NO")]
after_submit_tx_en = "Your region's decisions have been submitted - thanks!\nOnce all regions have submitted their decisons, the model will be advanced for the next round. This will take a bit of time ..."
nothing_submitted_tx_en = "Nothing was submitted ..."
p_advance_to_next_round_tx_en = "Get the results until 2040 and the decision sheet for 2040-2060 - your children's future"
p_advance_to_1_tx_en = "Get the results until 2060 and the decision sheet for 2060-2100 - your grandchildren's future"
p_advance_to_2_tx_en = "Get the results until the end of the century"
p_waiting_model_run_tx_en = "... still waiting for the GM to advance the model ..."
waiting_tx_en = "Waiting ..."
not_all_submitted_tx_en = "Not all regions have submitted their decisions ..."
not_all_submitted_p_tx_en = "Not all regions have submitted their decisions, your game leader knows who we are waiting for ..."
not_all_submitted_gm_tx_en = "Not all regions have submitted their decisions ..."
all_submitted_p_tx_en = "ALL regions HAVE submitted their decisions, your game leader will advance the model shortly and let you know when your results are ready"
running_model_tx_en = "... advancing the model ..."
not_all_submitted_tx_en = "Not all regions have submitted their decisions ..."
not_all_submitted_p_tx_en = "Not all regions have submitted their decisions, your game leader knows who we are waiting for ..."
not_all_submitted_gm_tx_en = "Not all regions have submitted their decisions ..."
all_submitted_p_tx_en = "ALL regions HAVE submitted their decisions, your game leader will advance the model shortly and let you know when your results are ready"
running_model_tx_en = "... advancing the model ..."
credits_btn_tx_en = "Credits"
credits_tx_en = "The model we use is the regional earth4all model developed by U Goluke and PE Stoknes. It, in turn, is based on the earth4all global model which J Randers developed. The game has been developed with anvil.works by U Goluke and countless alpha and beta testers. The rights to the game belong to ..."
credits_title_en = "Standing on shoulders of giants ..."
choose_lang_tx_en = "Change the language"


#######
####### Deutsch SIE
#######
reg_to_longreg_de_sie = {
  "us" : "USA",
  "af": "Afrika, südlich der Sahara",
  "cn" : "China",
  "me": "Naher Osten und Nordafrika",
  "sa" : "Südasien",
  "la" : "Lateinamerika",
  "pa" : "Pazifischer Raum",
  "ec" : "Osteuropa und Zentralasien",
  "eu" : "Europa",
  "se" : "Südostasien"
}
ta_to_longmini_de_sie = {
  "pov" : "Minister:in gegen Armut",
  "ineq" : "Minister:in gegen Ungleichheit",
  "emp" : "Minister:in für Empowerment/Befähigung",
  "food" : "Minister:in für Ernährung und Landwirtschaft",
  "ener" : "Minister:in für Energie",
  "fut" : "Minister:in für die Zukunft"
}
pol_to_expl_de_sie = {
  "CCS" : "Prozentsatz der fossilen Brennstoffe, der mit CO2-Abscheidung und -Speicherung (CCS) an der Quelle ausgestattet werden soll. Das bedeutet, dass zwar weiterhin CO2 ausgestossen wird, dieses aber nicht in die Atmosphäre gelangt, wo es Erwärmung verursacht, weil es vorher abgeschieden und unter der Erde gespeichert wird.",
  "TOW" : "0 bedeutet keine Vermögenssteuer, 80 bedeutet, dass jedes Jahr 80 % des angesammelten Vermögens des Eigentümers versteuert werden, 50 bedeutet, dass die Hälfte davon versteuert wird",
  "FPGDC" : "Diese Massnahme erlässt einen Prozentsatz der ausstehenden Staatsschulden gegenüber öffentlichen Kreditgebern. 0 bedeutet, dass nichts erlassen wird, 100 bedeutet, dass alles erlassen wird, 50 bedeutet, dass die Hälfte erlassen wird --- im ersten Jahr der Massnahmen.",
  "RMDR" : "Ernährungsumstellung, insbesondere Reduzierung des Fleischkonsums. 0 bedeutet, dass Fleisch wie bisher konsumiert wird, 50 bedeutet, dass 50 % durch Laborfleisch ersetzt werden, 100 bedeutet, dass 100 % durch Laborfleisch ersetzt werden, d. h. dass in der Massentierhaltung kein Fleisch mehr 'produziert' wird.",
  "REFOREST" : "Politik zur Wiederaufforstung, d.h. zum Pflanzen neuer Bäume. 0 bedeutet keine Wiederaufforstung, 1 bedeutet, dass Sie die Waldfläche um 1 â€° / Jahr (das ist 1 Promille) vergrössern, 3 = Sie vergrössern die Waldfläche um 3 â€° / Jahr",
  "FTPEE" : "Jährliche prozentuale Steigerung der Energieeffizienz; 1 % pro Jahr ist der historische Wert der letzten 40 Jahre. Vorsicht vor der Macht des Zinseszinses!",
  "LPBsplit" : "0 bedeutet, dass die gesamte LBP-Finanzierung in den Konsum fliesst (z. B. Kindergeld, Subventionen für Lebensmittel oder Energie usw.). 100 bedeutet, dass die gesamte Finanzierung in öffentliche Investitionen wie Infrastruktur, Sicherheit usw. fliesst. HINWEIS: Diese Massnahme hat nur dann eine Auswirkung, wenn LPB NICHT auf Null gesetzt ist.",
  "ExPS" : "Erlässt einen Prozentsatz der ausstehenden Staatsschulden gegenüber privaten Kreditgebern --- im ersten Jahr der Massnahmen",
  "FMPLDD" : "Angesichts Ihrer Kreditwürdigkeit steht Ihnen ein bestimmter Betrag zur Verfügung, den Sie von privaten Kreditgebern leihen können. Hier wählen Sie den Anteil des Kredits, den Sie tatsächlich jährlich in Anspruch nehmen.",
  "StrUP" : "In jeder Volkswirtschaft wird das Gesamtseinkommen zwischen Eigentümern und Arbeitnehmern aufgeteilt. Diese Politik verändert den Anteil, der den Arbeitnehmern zusteht. 1 multipliziert den Anteil mit 1 %, 2 mit 2 % usw.",
  "Wreaction": "In jeder Volkswirtschaft gibt es einen Machtkampf zwischen Arbeitnehmern und Eigentümern um den Anteil am Gesamteinkommen, den jeder erhält. Diese Politik stärkt die Verhandlungsposition der Arbeitnehmer. 1 um 1 %, 2 um 2 % usw. ",
  "SGMP": "Um Altersarmut zu bekämpfen, können Renten für alle eingeführt werden. Die Höhe der Rente wird als Prozentsatz des BIP ausgedrückt, den Sie investieren möchten. 0 bedeutet, dass Sie nichts investieren und alles so lassen, wie es ist. 5 bedeutet, dass Sie 5 % des BIP investieren. 10 bedeutet, dass 10 % des BIP an die Arbeitnehmer überwiesen und von den Eigentümern bezahlt werden.",
  "FWRP" : "Hier legen Sie fest, um wie viel der Anteil des 'normalen' Nahrungsverlustes von 30% reduziert werden soll. D.h. 100 bedeutet keinen Verlust mehr! 50 bedeutet, dass der Verlust um 50 % reduziert wird, 0 bedeutet, dass der Verlust wie immer weitergeht",
  "ICTR" : "Bei dieser Massnahme handelt es sich um eine Erhöhung der Verbrauchssteuer (auch Umsatzsteuer, Mehrwertsteuer usw. genannt). 0 bedeutet keine Erhöhung, 10 bedeutet eine Erhöhung um 10 Prozentpunkte, 5 um 5 Prozentpunkte; die eingenommenen Gelder fliessen in die allgemeinen Staatseinnahmen.",
  "XtaxCom": "Eine universelle Grunddividende entsteht, wenn ein Staat öffentliche Güter wie Fischereirechte, Bergbaurechte, das Recht zur Nutzung des Frequenzsprektrums usw. besteuert. Diese Richtlinie legt diese Steuer als Prozentsatz des BIP fest, d. h. 0 = 0 % des BIP, also nichts; 5 = 5 % des BIP; 3 = 3 % des BIP. Das Geld wird in die allgemeinen Steuereinnahmen des Staates überführt.",
  "Lfrac" : "Leakage beschreibt das 'Versickern' von Geldern in illegale Kanäle: Korruption, Bestechung usw. Der normale Verlust liegt bei 20 % - ein Wert von 0 bedeutet also, dass diese 20 % tatsächlich verschwinden - eine Reduzierung von 50 % bedeutet, dass 10 % verschwinden und eine Reduzierung von 100 % bedeutet, dass nichts versickert und jeder in Ihrer Region absolut ehrlich ist!",
  "IOITR" : "Dies ist eine Erhöhung der von Eigentümern gezahlten Einkommensteuer. 0 bedeutet keine Erhöhung, 10 bedeutet eine Erhöhung um 10 Prozentpunkte, 5 um 5 Prozentpunkte; das eingenommene Geld fliesst in die allgemeinen Staatseinnahmen.",
  "IWITR" : "Dies ist eine Erhöhung der von Arbeitnehmern gezahlten Einkommenssteuer. 0 bedeutet keine Erhöhung, 10 bedeutet eine Erhöhung um 10 Prozentpunkte, 5 um 5 Prozentpunkte; das eingenommene Geld fliesst in die allgemeinen Staatseinnahmen.",
  "SGRPI" : "Regierungen entscheiden, wie sie ihre Ausgaben einsetzen: vorrangig für Konsum (z. B. Kindergeld, Subventionen für Nahrungsmittel oder Energie usw.) oder für öffentliche Investitionen (Bildung, Gesundheitswesen, Infrastruktur usw.). Diese Politik verlagert die Ausgaben vom Konsum auf Investitionen. 0 bedeutet keine Verschiebung, 10 = 10 % des Konsums werden auf Investitionen umgeleitet, 25 = 25 % des Konsums werden auf Investitionen umgeleitet usw.",
  "FEHC": "Je höher das Bildungsniveau, insbesondere der Frauen, in einer Gesellschaft ist, desto niedriger ist die Geburtenrate. Bildung für alle senkt also die Geburtenrate. Um wie viel? Sie können eine fundierte Schätzung abgeben: 0 bedeutet keine Auswirkung, 10 bedeutet eine Verringerung um 10 %, 5 bedeutet eine Verringerung um 5 % usw..",
  "XtaxRateEmp" : "Die Gleichstellung von Frauen zu fördern, insbesondere die Verringerung des geschlechtsspezifischen Lohngefälles, kostet Geld. Wie viel Prozent des BIP möchten Sie dafür ausgeben? 0 bedeutet, Sie geben nichts aus und lassen alles so, wie es ist; 5 bedeutet, Sie geben 5 % des BIP aus; 3 bedeutet 3 % des BIP. Das Geld fliesst in die allgemeinen Steuereinnahmen des Staates.",
  "FLWR" : "Hier legen Sie den Prozentsatz Ihrer Ackerfläche fest, der regenerativ bearbeitet wird (geringe oder keine Bodenbearbeitung, geringe oder keine Dünge- und Pestizidverwendung usw.). 50 bedeutet, dass 50 % der Ackerfläche regenerativ bearbeitet werden, 100 = 100 % der Ackerfläche werden regenerativ bearbeitet usw. 0 lässt alles so, wie es ist.",
  "RIPLGF" : "Reduzierung der Lebensmittelimporte. 0 bedeutet keine Reduzierung, 10=10% Reduzierung, 50=50% Reduzierung. Diese Politik reduziert die Verfügbarkeit von Lebensmitteln aus anderen Ländern, stärkt aber die lokalen Produzenten.",
  "FC" : "Politik zur Begrenzung der Abholzung. 0 bedeutet keine Begrenzung der Abholzung, 10 = 10 % Reduzierung der maximalen Abholzungsmenge, 50 = 50 % Reduzierung der maximalen Abholzungsmenge usw. bis hin zu 90 % Reduzierung, was praktisch einem Abholzungsverbot entspricht.",
  "NEP" : "Prozentsatz der fossilen Brennstoffe (Öl, Gas und Kohle), die *nicht* zur Stromerzeugung (Mobilität, Heizung, industrielle Nutzung usw.) verwendet werden und die Sie elektrifizieren möchten.",
  "Ctax" : "Dies ist die CO2-Emissionssteuer. 0 bedeutet keine CO2-Steuer, 25 = 25 $/Tonne emittiertes CO2 usw.",
  "DAC" : "Rückgewinnung von CO2, das sich bereits in der Atmosphäre befindet, und dessen unterirdische Speicherung & in GtCO2/Jahr (Gigatonnen & Giga ist 10^9); Im Jahr 2020 betrugen die regionalen Emissionen ungefähr: USA 5, Afrika südlich der Sahara 1, China 12, der Rest jeweils zwischen 2 und 3 GtCO2/Jahr. Man kann mehr rück gewinnen, als man ausstösst.",
  "XtaxFrac" : "Der Prozentsatz der *zusätzlichen* Steuern, die von Eigentümern gezahlt werden (Eigentümer zahlen 50 % der zusätzlichen Steuern, sogar unter TLTL). D. h. 90 bedeutet, dass Eigentümer 90 % der zusätzlichen Steuern zahlen, 70 bedeutet, dass Eigentümer 70 % der zusätzlichen Steuern zahlen usw. Zusätzliche Steuern dienen der Stärkung der Selbstbestimmung und der gleichen Bezahlung von Frauen.",
  "LPBgrant" : "0 bedeutet, dass die gesamte LPB-Finanzierung als Darlehen gewährt wird, das sowohl zurückgezahlt als auch verzinst werden muss. 100 bedeutet, dass die gesamte Finanzierung als zinslose Zuschüsse gewährt wird, die nicht zurückgezahlt werden müssen. HINWEIS: Diese Massnahme hat nur dann Auswirkungen, wenn LPB NICHT auf Null gesetzt ist.",
  "LPB" : "Der Prozentsatz Ihres BIP, der als Finanzierung von öffentlichen Stellen (Weltbank, IWF, ausserbilanzielle Finanzierung, Sondervermögen) zur Verfügung gestellt wird. LPB = Kreditvergabe von öffentlichen Stellen (lending from public bodies)",
  "SSGDR" : "Sie können die Rückzahlung in die Zukunft strecken, so dass Sie jedes Jahr weniger zahlen, aber die Rückzahlungsdauer länger wird. 1 bedeutet keine Streckung - 2 verdoppelt die Rückzahlungsdauer - 3 verdreifacht die Rückzahlungsdauer - und so weiter",
  "ISPV": "Anteil der Stromerzeugung aus erneuerbaren Energien (40 % haben wir in der Vergangenheit erreicht)"
}
pol_to_name_de_sie = {
  "CCS" : "CCS: CO2-Abscheidung und -Speicherung an der Quelle",
  "TOW" : "Besteuerung des Vermögens von Superreichen",
  "FPGDC" : "Schuldenerlass von öffentlichen Kreditgebern",
  "RMDR" : "Ernährung umstellen",
  "REFOREST" : "Wiederaufforstung",
  "FTPEE" : "Energieeffizienz des Energiesystems",
  "LPBsplit" : "LPB: Aufteilung der Mittelverwendung öffentlicher Kreditgeber",
  "ExPS" : "Den politischen Handlungsspielraum erweitern",
  "FMPLDD" : "Anteil der Kredite bei privaten Kreditgebern, die pro Jahr NICHT in Anspruch genommen werden",
  "StrUP" : "Gewerkschaften stärken",
  "Wreaction" : "Verhandlungsmacht der Arbeitnehmer",
  "SGMP" : "Renten für alle",
  "FWRP" : "Reduzierung von Lebensmittelabfällen",
  "ICTR" : "Erhöhung der Mehrwertsteuer",
  "XtaxCom" : "Einführung einer allgemeine Grunddividende",
  "Lfrac" : "Reduzierung des Versickern von Geldern in illegale Kanäle",
  "IOITR" : "Erhöhung des Einkommensteuersatzes für Eigentümer",
  "IWITR" : "Erhöhung des Einkommensteuersatzes für Arbeitnehmer",
  "SGRPI" : "Staatliche Ausgaben auf Investitionen umstellen",
  "FEHC" : "Bildung für alle",
  "XtaxRateEmp" : "Förderung weiblicher Führungskräfte",
  "FLWR" : "Regenerative Landwirtschaft",
  "RIPLGF" : "Lebensmittelimporte reduzieren",
  "FC" : "Waldrodung",
  "NEP" : "Alles elektrifizieren",
  "Ctax" : "Eine CO2-Steuer einführen",
  "DAC" : "Rückgewinnung von CO2 aus der Luft ",
  "XtaxFrac" : "Zusätzliche Steuern, die von den Superreichen gezahlt werden",
  "LPBgrant" : "LPB: Mittel, die als Darlehen oder Zuschüsse gewährt werden",
  "LPB" : "Finanzierungen von öffentlichen Geldgebern (LPB)",
  "SSGDR" : "Strecken von Rückzahlung",
  "ISPV": "In Erneuerbare Energien investieren"
}
sdgvarID_to_subtitle_de_sie = {
  "13" : "Verfügbares Einkommen der Arbeitnehmer (1000 $/Personenjahr)",
  "18" : "Düngemittelverbrauch pro Kopf (Mt/Jahr)",
  "26" : "Bevölkerung (Millionen Menschen)",
  "19" : "Temperaturanstieg (°C im Vergleich zu 1850)",
  "20" : "Gesamt-Treibhausgasemissionen pro Jahr (GtCO2/Jahr)",
  "29" : "Anzahl der erreichten SDGs: 17 können erreicht werden",
  "4" : "Durchschnittlicher Wohlbefinden-index",
  "24" : "Vertrauen in Institutionen (1980=1)",
  "31" : "Jährliche Veränderungsrate der versiegelten Fläche (%)",
  "33" : "Jährliche Veränderung der Waldfläche (%)",
  "35" : "Planetarische Grenzen überschritten",
  "30" : "Anteil privater und staatlicher Investitionen (% des BIP)",
  "9" : "Prozent der Bevölkerung mit Zugang zu sicheren Sanitäreinrichtungen (%)",
  "16" : "Wachstumsrate des BIP pro Kopf (%/Jahr)",
  "17" : "Emissionen pro Person (tCO2/p/a)",
  "34" : "Anteil der Geber und ausserbilanziellen Investitionen (% des BIP)",
  "14" : "Millionen Arbeitslose",
  "21" : "pH-Wert der Meeresoberfläche",
  "12" : "Energieintensität in Bezug auf Primärenergie und BIP (kWh/$)",
  "22" : "Ausdehnung des tropischen Waldes weltweit (Mha)",
  "23" : "Öffentliche Dienstleistungen pro Person (1000 $/Person-Jahr)",
  "2" : "Millionen unterernährte Menschen (Mp)",
  "5" : "Lebenserwartung (Jahre)",
  "7" : "Anteil weiblicher Erwerbseinkommen vor Steuern (%)",
  "1" : "Millionen Menschen, die in Armut leben (Mp)",
  "3" : "Millionen Hektar regenerativ bewirtschaftet",
  "6" : "Schuljahre",
  "8" : "Prozent der Bevölkerung mit Zugang zu sauberem Wasser (%)",
  "10" : "Millionen Menschen ohne Zugang zu Elektrizität (Mp)",
  "15" : "Kohlenstoffintensität der Produktion (kgCO2/$)",
  "25" : "Gesamteinnahmen des Staates als Anteil des BIP (%)",
  "27" : "Arbeitnehmeranteil am BIP (%)",
  "28" : "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "37" : "Ackerland (Mha)",
  "11" : "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "36" : "BIP (G2017ppp$/Jahr)",
  "32" : "Stickstoffverbrauch (kg/ha-Jahr)",
  "39" : "nan",
  "38" : "nan"
}
sdgvarID_to_indicator_de_sie = {
  "13" : "Verfügbares Einkommen der Arbeitnehmer (1000 USD/Personenjahr)",
  "18" : "Düngemittelverbrauch pro Kopf (Mt/Jahr)",
  "26" : "Bevölkerung (Millionen Menschen)",
  "19" : "Temperaturanstieg (°C im Vergleich zu 1850)",
  "20" : "Gesamt-Treibhausgasemissionen pro Jahr (GtCO2/Jahr)",
  "29" : "Anzahl der erreichten SDGs: 17 können erreicht werden",
  "4" : "Durchschnittlicher Wohlbefinden-index",
  "24" : "Vertrauen in Institutionen (1980=1)",
  "31" : "Jährliche Veränderungsrate der Stadtfläche (%)",
  "33" : "Jährliche Veränderung der Waldfläche (%)",
  "35" : "Planetarische Grenzen überschritten",
  "30" : "Anteil privater und staatlicher Investitionen (% des BIP)",
  "9" : "Anteil der Bevölkerung mit Zugang zu sicheren Sanitäreinrichtungen (%)",
  "16" : "Wachstumsrate des BIP pro Kopf (%/Jahr)",
  "17" : "Emissionen pro Person (tCO2 pro Personenjahr)",
  "34" : "Anteil der Geber und ausserbilanziellen Investitionen (% des BIP)",
  "14" : "Arbeitslosenquote (%)",
  "21" : "pH-Wert der Meeresoberfläche",
  "12" : "Energieintensität in Bezug auf Primärenergie und BIP (kWh/$)",
  "22" : "Ausdehnung des tropischen Waldes weltweit (Mha)",
  "23" : "Öffentliche Dienstleistungen pro Person (1000 $/Person-Jahr)",
  "2" : "Anteil der unterernährten Bevölkerung (%)",
  "5" : "Lebenserwartung (Jahre)",
  "7" : "Anteil der weiblichen Erwerbseinkommen vor Steuern (%)",
  "1" : "Anteil der Bevölkerung, der weniger als 6,85 US-Dollar pro Tag verdient (%)",
  "3" : "Anteil der regenerativ bewirtschafteten landwirtschaftlichen Fläche (%)",
  "6" : "Schuljahre",
  "8" : "Anteil der Bevölkerung mit Zugang zu sauberem Wasser (%)",
  "10" : "Anteil der Bevölkerung mit Zugang zu Elektrizität (%)",
  "15" : "Kohlenstoffintensität der Produktion (kgCO2 pro USD)",
  "25" : "Gesamteinnahmen des Staates als Anteil des BIP (%)",
  "27" : "Arbeitsanteil am BIP (%)",
  "28" : "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "37" : "Ackerland (Mha)",
  "11" : "Anteil von Wind- und Photovoltaikenergie am Gesamtenergieverbrauch (%)",
  "36" : "BIP (G2017ppp$/Jahr)",
  "32" : "Stickstoffverbrauch (kg/ha-Jahr)",
  "39" : "(Index)",
  "38" : "(Index)"
}
sdgvarID_to_sdg_de_sie = {
  "13" : "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "18" : "Verantwortungsvoller Konsum und Produktion",
  "26" : "Gesamtbevölkerung",
  "19" : "Massnahmen zum Klimaschutz",
  "20" : "Massnahmen zum Klimaschutz",
  "29" : "SDG-Ergebnisse",
  "4" : "Gute Gesundheit und Wohlbefinden",
  "24" : "Partnerschaft zur Erreichung der Ziele",
  "31" : "Nachhaltige Städte und Gemeinden",
  "33" : "Leben an Land",
  "35" : "Planetarische Grenzen",
  "30" : "Industrielle Innovation und Infrastruktur",
  "9" : "Zugang zu sauberen Sanitäranlagen",
  "16" : "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "17" : "Nachhaltige Städte und Gemeinden",
  "34" : "Industrielle Innovation und Infrastruktur",
  "14" : "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "21" : "Leben unter Wasser",
  "12" : "Bezahlbare und saubere Energie",
  "22" : "Leben an Land",
  "23" : "Frieden, Gerechtigkeit und starke Institutionen",
  "2" : "Kein Hunger",
  "5" : "Gute Gesundheit und Wohlbefinden",
  "7" : "Gleichstellung der Geschlechter",
  "1" : "Keine Armut",
  "3" : "Kein Hunger",
  "6" : "Hochwertige Bildung",
  "8" : "Zugang zu sauberem Wasser",
  "10" : "Bezahlbare und saubere Energie",
  "15" : "Industrielle Innovation und Infrastruktur",
  "25" : "Partnerschaft zur Erreichung der Ziele",
  "27" : "Verringerte Ungleichheiten",
  "28" : "Bezahlbare und saubere Energie",
  "37" : "Ackerland",
  "11" : "Bezahlbare und saubere Energie",
  "36" : "BIP",
  "32" : "Verantwortungsvoller Konsum und Produktion",
  "39" : "Soziale Spannungen",
  "38" : "Soziales Vertrauen"
}
top_title = 'LT Spiel'
top_btn_thanks_de_sie = 'Danke'
top_btn_start_de_sie = "Starten Sie ein neues Spiel als Spielleiter:in"
top_btn_join_de_sie = 'Als Spieler einem Spiel beitreten'
top_btn_help_de_sie = 'Hilfe'
top_join_game_de_sie = 'Als Spieler einem Spiel beitreten'
top_start_game_de_sie = 'Starten Sie ein Spiel als Spielleiter:in'
p_lb_choose_game_de_sie = 'Es sind mehrere Spiele geöffnet. Wählen Sie zunächst das Spiel aus, dem Sie beitreten möchten, und klicken Sie dann auf die Schaltfläche TEILNEHMEN:'
p_btn_select_game_de_sie = 'TEILNEHMEN'
gm_id_msg1_de_sie = "Ihre Spiel-ID ist "
gm_id_msg2_de_sie = ". Notieren Sie die ID und geben Sie sie an ihre Spieler weiter."
gm_id_title_de_sie = "Ihre Spiel-ID:"
top_thanks_msg_de_sie = "... an unsere Alpha-Tester, die Schüler des Kurses SW101 an der Realschule Baesweiler im April 2024, der von René Langohr unterrichtet wird, und alle Beta-Tester."
top_thanks_title_de_sie = "Vielen Dank ..."
top_roles_setup_msg_de_sie = "Rollenvorlage wurde eingerichtet für "
title_you_are_joining_de_sie = "Sie treten bei: "
msg_game_not_started_de_sie = "Der/Die Spielleiter:in hat noch kein Spiel gestartet. Bitte warten Sie, bis er/sie das tut ..."
msg_gm_board_de_sie = "Spielleiter:in-Brett"
msg_gm_board_info_de_sie = "**Klicken Sie jetzt auf *alle* Regionen, die *nicht* von Ihren Spielern gespielt werden (z. B. wenn nicht genügend Spieler für alle Rollen vorhanden sind)**"
cb_us_tx_de_sie = 'USA'
cb_af_tx_de_sie = 'Afrika, südlich der Sahara'
cb_cn_tx_de_sie = 'China'
cb_me_tx_de_sie = 'Naher Osten & Nordafrika'
cb_sa_tx_de_sie = 'Südasien'
cb_la_tx_de_sie = 'Lateinamerika'
cb_pa_tx_de_sie = 'Pazifischer Raum'
cb_ec_tx_de_sie = 'Osteuropa & Zentralasien'
cb_eu_tx_de_sie = 'Europa'
cb_se_tx_de_sie = 'Südostasien'
cb_pov_tx_de_sie = 'Armut'
cb_ineq_tx_de_sie = 'Ungleichheit'
cb_emp_tx_de_sie = 'Ermächtigung'
cb_food_tx_de_sie = 'Nahrung und Landwirtschaft'
cb_ener_tx_de_sie = 'Energie'
cb_fut_tx_de_sie = 'Zukunft'
pcr_title_tx_de_sie = 'Spieler-Brett'
pcr_col_left_title_tx_de_sie = "Melden Sie sich zunächst in Ihrer Region an ..."
pcr_col_right_title_tx_de_sie = '... dann in Ihrer Rolle als Minister:in ...'
pcr_submit_tx_de_sie = "Nachdem Sie sich sowohl bei Ihrer Region als auch bei Ihrem Ministerium angemeldet haben, klicken Sie hier."
fut_not_all_logged_in_tx_de_sie = "Noch sind nicht alle Ihrer regionalen Ministerkolleg:innen eingeloggt. Warten Sie, bis sie das getan haben."
no_active_game_to_join_tx_de_sie = "Kein aktives Spiel zum Beitreten ... der/die Spielleiter:in muss erst eins starten"
gm_reg_npbp_tx_de_sie = "Wenn Sie fertig sind (und sicher sind), klicken Sie auf diese Schaltfläche."
top_entry_label_tx_de_sie = "Moment, alle erforderlichen Slots, Vorlagen und Tabellen für das Spiel werden eingerichtet ..."
gm_card_wait_1_temp_title_tx_de_sie = "Wir warten immer noch darauf, dass sich die folgenden Minister:innen anmelden ... Fragen Sie, ob sie Hilfe benötigen ..."
gm_card_wait_1_temp_title_tx2_de_sie = 'Alle sind eingelogged! Klicken Sie auf "Bereit zum Fortfahren", um zu prüfen, ob alle Ihre Regionen ihre Richtlinien übermittelt haben. Teilen Sie ihnen mit, wie viel Zeit ihnen noch bleibt.'
gm_card_wait_1_info_tx_de_sie = "Alle Rollen wurden nun eingerichtet. \nBitten Sie Ihre Spieler, sich einzuloggen, den Zustand ihrer Region in den letzten 45 Jahren zu betrachten und ihre Entscheidungen zur Verbesserung des Lebens ihrer Bevölkerung zu diskutieren. Ãœberprüfen Sie wiederholt, ob sich alle Ihre Spieler angemeldet haben, indem Sie auf die Schaltfläche **Anmeldung prüfen** klicken. Sobald sie bereit sind, mit der nächsten Runde fortzufahren, **---** *das kann dauern!* **---** klicken Sie auf die Schaltfläche **Modell für die nächste Runde laufen lassen**. Wenn die Schaltfläche * Modell für die nächste Runde laufen lassen* nicht angezeigt wird, sind Ihre Spieler noch nicht soweit."
gm_card_wait_1_btn_check_tx_de_sie = 'Anmeldung prüfen'
gm_card_wait_1_btn_kick_off_round_1_tx_de_sie = "Modell für die nächste Runde laufen lassen"
gm_wait_kickoff_r1_tx_de_sie = "Warten immer noch darauf, dass die unten aufgeführten Regionen ihre Entscheidungen übermitteln ... Sie können fragen, ob sie Hilfe benötigen ..."
gm_wait_round_done_tx_de_sie = 'Das Modell wurde fortgeschrieben. Bitten Sie Ihre Spieler, auf die Schaltfläche \n"Ergebnisse abrufen ..." oder \n"Ãœberprüfen, ob der/die Spielleiter:in ..." zu klicken.'
gm_wait_round_done_tx2_de_sie = 'Das Modell wurde fortgeschrieben. Bitten Sie Ihre Spieler:innen, die Ergebnisse innerhalb und zwischen den Regionen anzuschauen und zu diskutieren. Läuft alles in die richtige Richtung? Sind sie zufrieden?\nAnschliessend sollten sie über die Massnahmen für die nächste Runde entscheiden. Sobald sie bereit sind, sollte der/die ZukunftsMinister:in die regionalen Entscheidungen übermitteln. Sagen sie deutlich, wie viel Zeit ihnen zur Verfügung steht.'
gm_wait_round_done_tx3_de_sie = 'Das Modell wurde bis zum Ende, dem Jahr 2100, fortgeschrieben. Bitten Sie Ihre Spieler:innen, ihre Ergebnisse innerhalb und zwischen den Regionen anzuschauen und zu diskutieren. Läuft alles nach Plan? Sind sie zufrieden? Sind ihre Bürger zufrieden? Ist die Erde noch bewohnbar? \nZum Schluss nehmen Sie sie aus dem Spiel zurück ins Hier und Jetzt und beginnen Sie mit der Nachbesprechung.'
sim_success_tx1_de_sie = '...das Modell lief erfolgreich bis 2040, aber wir warten noch auf alle Entscheidungen für 2040-2060.\nHaben Sie alle Ihre politischen Entscheidungen getroffen?'
sim_success_tx1_de_sie = '...das Modell lief erfolgreich bis 2060, aber wir warten noch auf alle Entscheidungen für 2060-2100.\nHaben Sie alle Ihre politischen Entscheidungen getroffen?'
sim_success_title_tx_de_sie = 'Warten'
pcgd_generating_tx1_de_sie = "Diagramme bis 2040 und Entscheidungsblatt für 2040 werden erstellt"
pcgd_generating_tx2_de_sie = "Diagramme bis 2060 und Entscheidungsblatt für 2060 werden erstellt"
pcgd_generating_tx3_de_sie = " Diagramme bis 2100 werden erstellt"
gm_wait_round_started_tx_de_sie = 'Die Simulation hat begonnen. Bitte warten Sie, bis sie abgeschlossen ist...'
gm_start_round_tx_2_de_sie = "Ãœberprüfen Sie, ob alle Regionen ihre Massnahmen bis 2060 übermittelt haben ..."
gm_start_round_tx_3_de_sie = " Ãœberprüfen Sie, ob alle Regionen ihre Massnahmen bis 2100 übermittelt haben ..."
waiting_for_gm_to_start_round_de_sie = "... bis die Simulation beginnt ..."
gm_wait_sub2_tx_de_sie = "... für alle Massnahmen für die Runde 2040 bis 2060 ..."
gm_wait_sub3_tx_de_sie = "... für alle Massnahmen für die Runde 2060 bis 2100 ..."
setup_npbp_label_tx_de_sie = "Warten Sie bis alle Rollen vorbereitet sind ..."
# msg_de_sie = 'Die Rollenzuweisungen sind eingerichtet ... Sagen Sie Ihren Spielern:innen nun, dass sie dem Spiel ' + cid + ' beitreten und sich in ihre Rollen einloggen sollen. Sie selbst müssen warten, bis alle Spieler:innen ihre Entscheidungen für Runde 1 (2025 bis 2040) übermittelt haben.'
pcr_submit_title_de_sie = "Herzlichen Glückwunsch!"
pcr_submit_msg1_de_sie = "Sie wurden bestätigt als "
fut_title_tx2_de_sie = ""
pcr_submit_msg2_de_sie = ' in '
pcr_submit_msg3_de_sie = 'Ihre persönliche Spiel-ID lautet: '
player_board_tx_de_sie = "Spieltafel: "
pcgd_rd1_info_tx_de_sie = "Sie sind dafür verantwortlich, das Leben Ihrer Bevölkerung zu verbessern. In den folgenden Diagrammen ist die Lage gut, wenn die Linie im **grünen** Bereich liegt. Wenn sie im **roten** Bereich liegt, müssen Sie sich Sorgen machen & soziale Unruhen oder Schlimmeres stehen unmittelbar bevor!\nSchauen Sie alle Ihre Indikatoren an, beobachten Sie deren Entwicklung über die Jahre und tauschen Sie sich aus mit Kollegen:innen, zunächst in Ihrer Region, aber auch in den anderen Regionen.\nWenn Sie bereit sind, scrollen Sie nach unten zu den Entscheidungen, die Sie als Minister:in treffen müssen, um das Leben Ihrer Bürger in der nächsten Runde hoffentlich zu verbessern."
pcgd_rd1_info_short_de_sie = "Gemeinsam mit Ihrem Minister:innen Team tragen Sie die Verantwortung, das Leben Ihrer Bevölkerung zu verbessern. In den folgenden Grafiken ist die Lage gut, wenn die Linie im **grünen** Bereich liegt. Liegt sie im **roten** Bereich, besteht Grund zur Sorge & soziale Unruhen oder Schlimmeres stehen unmittelbar bevor!\ nSchauen Sie alle Ihre Indikatoren an, beobachten Sie deren Entwicklung über die Jahre und tauschen Sie sich aus mit Kollegen:innen, zunächst in Ihrer Region, aber auch in den anderen Regionen.\nWenn Sie bereit sind, scrollen Sie nach unten, um die Investitionspläne Ihrer Kollegen:innen zu sehen. Stellen Sie sicher, dass diese im Rahmen Ihres regionalen Budgets liegen. Weitere Anweisungen finden Sie unter den Grafiken."
pcgd_rd1_info_end_de_sie = "**Ausblenden**"
pcgd_rd1_info_fut_tx_de_sie = "Als ZukunftsMinister:in sehen Sie das grosse Ganze. Sie sehen auch, wie viel Ihre Minister:innenkollegen in Ihrer Region insgesamt investieren wollen, um das Leben Ihrer Bevölkerung und die Gesundheit des Planeten zu verbessern. \nEs ist **Ihre** Aufgabe, die **regionalen Gesamtinvestitionen** im Rahmen des Budgets zu halten. Liegen die *Gesamtinvestitionen* **unter** 100 % des Budgets, ist alles in Ordnung. Investieren Sie jedoch zu wenig, kann es schlimmer werden, möglicherweise sogar noch viel schlimmer!\nLiegen sie **über** 100 % Ihres Budgets, müssen Sie Ihre Minister:innenkollegen anweisen, ihre Investitionen zu kürzen. Dies ist eine schwierige Aufgabe, bei der Ihre Moderationsfähigkeiten gefragt sind. Viel Erfolg!\nWährend Ihre Minister:innenkollegen ihre Investitionspläne beschliessen, klicken Sie wiederholt auf die Schaltfläche **Zahlen aktualisieren**, um die aktuellsten Entscheidungen Ihrer Kollegen anzuzeigen.\nWenn Sie fertig sind, **reichen Sie** als ZukunftsMinister:in die politischen Entscheidungen aller Ihrer Kollegen ein. **Achten Sie darauf, dass alle ihre Zustimmung geben** bevor Sie auf *Übermitteln* klicken! (*Hinweis:* Wenn die Schaltfläche *Übermitteln* nicht angezeigt wird, liegt das daran, dass Ihre Region das Budget überschreitet.\n\nGeldbeträge werden in konstanten (2025) Giga-Dollar pro Jahr angegeben. Ein *Giga* entspricht 1.000.000.000 & US-Amerikaner nennen dies eine Billion, andere eine Milliarde.)"
pcgd_rd1_info_end_tx_de_sie = "pcgd_rd1_info_end_tx *Ausgang*"
pcgd_generating_tx_de_sie = "... Ihre Diagramme und Entscheidungsblätter werden generiert..."
show_hide_plots_hide_tx_de_sie = "Diagramme ausblenden"
show_hide_plots_show_tx_de_sie = "Diagramme anzeigen"
pcgd_advance_tx_de_sie = "Ãœberprüfen, ob das Modell fortgeschrieben wurde"
pcgd_info_after_rd1_tx_de_sie = "Das Modell wurde bis 2040 fortgeschrieben. Auch in den folgenden Grafiken ist alles gut, wenn die Linie im **grünen** Bereich liegt. Wenn sie im **roten** Bereich liegt, besteht Grund zur Sorge!\nSchauen Sie sich Sie alle Ihre Indikatoren und beobachten Sie, wie sie sich im Laufe der Jahre entwickeln. *Haben Sie angesichts Ihrer politischen Entscheidungen etwas anderes erwartet? Sind Sie überrascht?* Besprechen Sie dies erneut mit Kollegen:innen, zuerst in Ihrer Region, aber auch in den anderen Regionen.\nWenn Sie bereit sind und im Lichte der Ergebnisse der letzten Runde, scrollen Sie nach unten zu den Entscheidungen, die Sie als Minister:in treffen müssen, um hoffentlich das Leben Ihrer Bürger in der nächsten Runde zu verbessern."
not_to_2060_de_sie = "Das Modell wurde noch nicht bis zum Jahr 2060 fortgeschrieben."
dec_info_tx_de_sie = "Nachdem Sie die Situation Ihrer Bevölkerung analysiert haben, müssen Sie verschiedene Massnahmen ergreifen, um das Leben Ihrer Bevölkerung **und** die Gesundheit des Planeten zu verbessern. Sie wissen, dass Menschen auf einem kranken Planeten nicht leben können. Sie legen die Massnahmen fest, indem Sie die Schieberegler ziehen. Nach Abstimmung mit Ihren Minister:innenkollegen stellen Sie den Schieberegler für jede Massnahme ein. \n\nJede Massnahme ist mit **Investitionskosten** verbunden. Stellen Sie den Schieberegler auf das Minimum, entstehen keine Kosten. Stellen Sie den Schieberegler auf das Maximum, werden die vollen Investitionskosten fällig. Stellen Sie den Schieberegler irgendwo zwischen Minimum und Maximum ein, werden die anteiligen Investitionskosten fällig. Ihre Region verfügt ausserdem über ein Budget für **alle** Investitionen **aller** Minister:innen. \n\nSollten Sie das Budget überschreiten, wird Ihr Kollege, der/die Minister:in für die Zukunft, Sie darüber informieren, und Sie müssen mit Ihren Kollegen:innen neu verhandeln, bis die gesamten regionalen Investitionen unter oder gleich dem Budget liegen.\n\nWenn das Kabinett Ihrer Region **a)** innerhalb des Budgets liegt und **b)** Sie **alle** mit Ihren Entscheidungen zufrieden sind, wird der/die ZukunftsMinister:in alle Ihre Entscheidungen dem/der Spielleiter:in übermitteln, damit das Modell für die nächste Runde fortgeschrieben wird."
dec_title_tx_de_sie = "Entscheiden Sie über ihre Massnahmen"
fut_info_tx_de_sie = "Als ZukunftsMinister:in sehen Sie das grosse Ganze. Sie sehen auch, wie viel Ihre Minister:inkollegen in Ihrer Region insgesamt investieren wollen, um das Leben Ihrer Bevölkerung und die Gesundheit des Planeten zu verbessern.\n\nEs ist **Ihre** Aufgabe, die **regionalen Gesamtinvestitionen** im Rahmen des Budgets zu halten. Liegen die *Gesamtinvestitionen* **unter** 100 % des Budgets, ist alles in Ordnung. Investieren Sie jedoch zu wenig, kann es schlimmer werden, möglicherweise sogar noch viel schlimmer!\n\nLiegen sie **über** 100 % Ihres Budgets, müssen Sie Ihre Minister:innenkollegen anweisen, ihre Investitionen zu reduzieren. Dies ist eine schwierige Aufgabe, bei der Ihre Moderationsfähigkeiten gefragt sind. Viel Erfolg!\n\nWährend Ihre Minister:innenkollegen ihre Investitionspläne beschliessen, klicken Sie wiederholt auf die Schaltfläche **Zahlen aktualisieren**, um die aktuellsten Entscheidungen Ihrer Kollegen anzuzeigen.\n\nWenn Sie fertig sind, **reichen Sie** als ZukunftsMinister:in die politischen Entscheidungen aller Ihrer Kollegen ein & **holen Sie sich unbedingt deren Zustimmung**, bevor Sie auf die Schaltfläche *Ãœbermitteln* klicken! (*Hinweis:* Wenn die Schaltfläche *Übermitteln* nicht angezeigt wird, liegt das daran, dass Ihre Region das Budget überschreitet.\n\nDie Geldbeträge werden in konstanten (2025) Giga-Dollar pro Jahr angegeben. Ein *Giga* entspricht 1.000.000.000 --- US-Amerikaner nennen dies eine Billion, andere eine Milliarde."
fut_bud_lb1_tx_de_sie = "Ihr Gesamtbudget:"
fut_bud_lb2_tx_de_sie = "Alle Investitionspläne aller Ihrer Minister:innenkollegen zusammengefasst:"
fut_bud_lb3_tx_de_sie = "Investitionspläne als % Ihres Budgets"
cfpov_tx_de_sie = "Armut"
cfpov_lb_tx_de_sie = "Regionale Investitionspläne gegen Armut:"
cfineq_tx_de_sie = "Ungleichheit"
cfineq_lb_tx_de_sie = "Regionale Investitionspläne gegen Ungleichheit:"
cfemp_tx_de_sie = "Empowerment/Befähigung"
cfemp_lb_tx_de_sie = "Regionale Investitionspläne zur Stärkung der Selbstbestimmung:"
cffood_tx_de_sie = "Ernährung und Landwirtschaft"
cffood_lb_tx_de_sie = "Regionale Investitionen für Ernährung und Landwirtschaft:"
cfener_tx_de_sie = "Energie"
cfener_lb_tx_de_sie = "Regionale Investitionen für die Energiewende:"
refresh_numbers_tx_de_sie = "Zahlen aktualisieren"
submit_numbers_tx_de_sie = "Zahlen übermitteln"
confirm_submit_tx_de_sie = "Ja zum Absenden, Nein zum Zurückgehen"
confirm_title_tx_de_sie = "Letzte Chance zurückzugehen."
confirm_buttons_tx_de_sie = [  ("Ja", "YES"),  ("Nein", "NO") ]
after_submit_tx_de_sie = "Die Entscheidungen Ihrer Region wurden übermittelt - Danke!\nSobald alle Regionen ihre Entscheidungen übermittelt haben, wird das Modell für die nächste Runde fortgeschrieben. Das wird etwas dauern ..."
nothing_submitted_tx_de_sie = "Es wurde nichts übermittelt"
p_advance_to_next_round_tx_de_sie = "Laden Sie sich die Ergebnisse bis 2040 und den Entscheidungsbogen für 2040-2060 - die Zukunft Ihrer Kinder"
p_advance_to_1_tx_de_sie = "Laden Sie sich die Ergebnisse bis 2060 und den Entscheidungsbogen für 2060-2100 - die Zukunft Ihrer Enkelkinder"
p_advance_to_2_tx_de_sie = "Ergebnisse bis zum Ende des Jahrhunderts laden"
p_waiting_model_run_tx_de_sie = "wir warten immer noch darauf, dass der/die Spielleiter:in das Modell fortschreibt"
waiting_tx_de_sie = "Warten ..."
not_all_submitted_tx_de_sie = "Noch haben nicht alle Regionen ihre Entscheidungen übermittelt ..."
not_all_submitted_p_tx_de_sie = "Noch haben nicht alle Regionen ihre Entscheidungen übermittelt, ihr:e Spielleiter:in weiss, auf wen wir warten ..."
not_all_submitted_gm_tx_de_sie = "Noch haben nicht alle Regionen ihre Entscheidungen übermittelt"
all_submitted_p_tx_de_sie = "ALLE Regionen haben jetzt ihre Entscheidungen übermittelt. Ihr:e Spielleiter:in wird das Modell in Kürze fortschreiben und Sie informieren, wenn Ihre Ergebnisse vorliegen."
running_model_tx_de_sie = "... das Modell fortschreiben ..."

choose_lang_tx_de_sie = "Ändern der Sprache"

#######
####### Deutsch DU
#######
choose_lang_tx_de_du = "Ändere die Sprache"

#######
####### Francais
#######
choose_lang_tx_fr = "Changer de langue"
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
my_lang = ''
my_step = 0
game_runde = 0
dbg_info = []
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

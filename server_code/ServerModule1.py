import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import random
import string
import datetime
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import anvil.mpl_util
import anvil.tz
from . import mg

@anvil.server.callable
def generate_id():
  app_tables.status.delete_all_rows()
  not_allowed = ['FUCK', 'SHIT']
  cid = ''.join(random.choices(string.ascii_uppercase, k=3))
  a = random.randint(10, 99)
  while a == 88:
    a = random.randint(10, 99)
  cid = cid + '-' + str(a) 
  while app_tables.status.has_row(q.like(cid)):
    cid = ''.join(random.choices(string.ascii_uppercase, k=4))
    a = random.randint(10, 99)
    while a == 88:
      a = random.randint(10, 99)
    cid = cid + '-' + str(a) 
  return f"{cid}"

@anvil.server.callable
def launch_set_roles(game_id):
  task = anvil.server.launch_background_task('set_roles', game_id)
  return task

#@anvil.server.callable
@anvil.server.background_task
def set_roles(game_id):
  app_tables.roles_assign.delete_all_rows()
  app_tables.budget.delete_all_rows()
  regs = mg.regs
  pols = [r['abbr'] for r in app_tables.policies.search()]
  for runde in range(1,4):
    for re in regs:
      for p in pols:
        my_role = mg.Pov_to_pov[mg.pol_to_ta[p]]
        app_tables.roles_assign.add_row(game_id=game_id,role=my_role, taken = 4, reg=re, round=runde, pol=p)
        ## set up future which has no policies
      app_tables.roles_assign.add_row(game_id=game_id,role='fut', taken=0, reg=re, round=runde, pol='nopol')
  jetzt = datetime.datetime.now(anvil.tz.tzlocal(anvil.tz.tzlocal()))
  row = app_tables.status.get(game_id=game_id)
  row.update(started=jetzt,game_status=1)
  
@anvil.server.callable
def upload_csv_reg(rows, re):
  app_tables.policies.delete_all_rows()
  for r in range(1, len(rows)):
    r = rows[r]
    rr = r.split(",")
    r0 = int(rr[0])
    r5 = int(rr[5])
    app_tables.regions.add_row(id=r0, abbr=rr[1], name=rr[2], col=rr[3], colhex=rr[4], pyidx=r5)

@anvil.server.callable
def upload_csv_mini(rows, re):
  for r in range(1, len(rows)):
    r = rows[r]
    rr = r.split(",")
    app_tables.ministries.add_row(id=int(rr[0]), ministry=rr[1], long=rr[2], mini=rr[3])

@anvil.server.callable
def upload_csv_sdg(rows, re):
  for r in range(1, len(rows)):
    r = rows[r]
    rr = r.split(",")
    app_tables.sdg.add_row(id=int(rr[0]), sdgNbr=rr[1], sdg=rr[2], sdg_dt=rr[3] )

@anvil.server.callable
def upload_csv_pols(rows, re):
  app_tables.policies.delete_all_rows()
  for r in range(1, len(rows)):
    r = rows[r]
    rr = r.split(",")
    app_tables.policies.add_row(id=int(rr[0]), abbr=rr[1], name=rr[2], tltl=float(rr[3]), gl=float(rr[4]), expl=rr[5], ta=rr[6] )

@anvil.server.callable
def upload_csv_mpv(rows, re):
  app_tables.mdf_play_vars.delete_all_rows()
  for r in range(1, len(rows)):
    r = rows[r]
    rr = r.split(",")
    print(rr)
    app_tables.mdf_play_vars.add_row(var_name=rr[0], col_idx=int(rr[1]) )

@anvil.server.callable
def upload_csv_sdg_vars(rows, re):
  app_tables.sdg_vars.delete_all_rows()
  for r in range(1, len(rows)):
    r = rows[r]
    rr = r.split(",")
    print(rr)
    app_tables.sdg_vars.add_row(id=int(rr[0]), sdg_nbr= int(rr[1]), sdg=rr[2], indicator=rr[3],vensim_name=rr[4],green=float(rr[5]),
                               red=float(rr[6]), lowerbetter=int(rr[7]), ymin=float(rr[8]), ymax=float(rr[9]),
                               subtitle=rr[10], ta=rr[11], pct=int(rr[12]))

@anvil.server.callable
def launch_set_npbp(game_id, npbp):
  task = anvil.server.launch_background_task('set_npbp', game_id, npbp)
  return task

@anvil.server.background_task
def set_npbp(cid, npbp):
  app_tables.state_of_play.delete_all_rows()
  app_tables.step_done.delete_all_rows()
  pol_list = [r['abbr'] for r in app_tables.policies.search()]
#  print(pol_list)
  tltl_list = [r['tltl'] for r in app_tables.policies.search()]
#  print(tltl_list)
  gl_list = [r['gl'] for r in app_tables.policies.search()]
#  print(gl_list)
  w_list = []
  for i in range(0,len(tltl_list)):
    mymin = tltl_list[i]
    mymax = gl_list[i]
    myrange = (mymax - mymin) 
    w = mymin + random.uniform(0, myrange)
    w_list.append(w)  # random policy value biased towards GL
  regs = mg.regs
#  print(w_list)
  for re in regs: # set up regs_state_of_play
    if re in npbp:
      app_tables.step_done.add_row(game_id=cid, reg=re, p_step_done=99) # p_state 99: played by computer
    else:
      app_tables.step_done.add_row(game_id=cid, reg=re, p_step_done=0) # p_state 0: data set up
  roles = mg.roles
  for ro in roles:
    for re in regs: # set up regs_state_of_play
      if re in npbp:
        app_tables.state_of_play.add_row(game_id=cid, reg=re, p_state=99, ta=ro) # p_state 99: played by computer
      else:
        app_tables.state_of_play.add_row(game_id=cid, reg=re, p_state=0, ta=ro) # p_state 0: data set up
  for runde in range(1,4):  # set up roles_assign
    for re in regs:
      j = 0
      for p in pol_list:
        ta = mg.Pov_to_pov[mg.pol_to_ta[p]]
        row = app_tables.roles_assign.get(game_id=cid, round=runde, reg=re, pol=p, role=ta)
        if re in npbp:
          taken = 2
          w2 = w_list[j]
#          print(cid,' ' + str(runde)+' '+re+' '+p+' '+ta+' '+str(w2))
        else:
          taken = 0
          w2 = tltl_list[j]
        row.update(taken=taken, wert=w2)
        j += 1
      # setup fut which has no policy
      row = app_tables.roles_assign.get(game_id=cid, round=runde, reg=re, role='fut')
      if re in npbp:
        row.update(taken=2)
      else:
        row.update(taken=0)
  rs = app_tables.status.get(game_id=cid)
  rs.update(gm_status=1)

def read_mdfplay25(datei, runde):
#  print('APRIL IN read_mdfplay25 loading: ' + datei)
  f = data_files[datei]
  mdf_play = np.load(f)
  if runde == 1:
    mdf_play = mdf_play[320:1440, :]
  elif runde == 2:
    mdf_play = mdf_play[320:1920, :]
  return mdf_play

def pick(ys, x, y):
    o = []
    ys_len = len(ys)
    ys_cnt = 0
    ys_check = ys[ys_cnt]
    for i in range(0, len(x)):
        if ys_check == x[i]:
            o.append(y[i])
            ys_cnt += 1
            if ys_cnt == ys_len:
                ys_check = 1952
            else:
                ys_check = ys[ys_cnt]
        else:
            o.append(np.nan)
    return o

def make_png(df, row, pyidx, end_yr, my_title):
    fig, ax = plt.subplots()
    pct = row['pct']
    x = df[:, 0]
    y = df[:, 1] * pct
    data_max = y.max() * 1.1
    data_min = y.min()
    plot_max = row['ymax']
    plot_min = row['ymin']
    ymin = min(data_min, plot_min)
    ymax = max(data_max, plot_max)
    if ymin > 0:
        ymin = 0
    if ymax < 0:
        ymax = 0
    if int(row['id']) in [27, 5]:  # Labour share of GDP | life expectancy
        ymin = plot_min  # red min
    if int(row['id']) in [26]:  # population | 
        ymax = data_max
    if int(row['id']) in [32]:  # Nitrogen use
        ymax = max(25, data_max)
    if int(row['id']) in [21]:  # pH  |
        ymin = plot_min
        ymax = plot_max
    abc = app_tables.regions.get(pyidx=pyidx)
    my_colhex = abc['colhex']
    my_lab = abc['name']
    plt.plot(x, y, color=my_colhex, linewidth=2.5, label=my_lab)
    if end_yr==2025:
      yr_picks = mg.yr_picks_start
    elif end_yr == 2040:
      yr_picks = mg.yr_picks_r1
    elif end_yr == 2060:
      yr_picks = mg.yr_picks_r2
    elif end_yr == 2100:
      yr_picks = mg.yr_picks_r3
    else:
      print("problem with yr_picks")
    ys = pick(yr_picks, x, y)
    plt.scatter(x, ys, color=my_colhex, s=300, alpha=0.55)
    if int(row['lowerbetter']) == 1:
        grn_min = row['ymin']  # 8
        grn_max = row['green']  # vars_df.iloc[varx, 4]
        red_min = row['red']  # vars_df.iloc[varx, 5]
        if int(row['id']) == 16:  # Emissions per person
            red_max = max(data_max, 8)
            ymax = red_max
        else:
            red_max = row['ymax']  # vars_df.iloc[varx, 9]
        if red_max < ymax:
            red_max = ymax
        yel_min = grn_max
        yel_max = red_min
    else:
        red_min = row['ymin']  # vars_df.iloc[varx, 8]
        if int(row['id']) == 10:  # Access to electricity
            if red_min > ymin:
                ymin = red_min
        red_max = row['red']  # vars_df.iloc[varx, 5]
        grn_min = row['green']  # vars_df.iloc[varx, 4]
        grn_max = row['ymax']  # vars_df.iloc[varx, 9]
        yel_min = red_max
        yel_max = grn_min
    plt.ylim(ymin, ymax)
    xmin = 1990
    xmax = end_yr
    if not int(row['id']) == 26:  # population
        opa = 0.075
        poly_coords = [(xmin, grn_max), (xmax, grn_max), (xmax, grn_min), (xmin, grn_min)]
        ax.add_patch(plt.Polygon(poly_coords, color='green', alpha=opa))
        poly_coords = [(xmin, red_max), (xmax, red_max), (xmax, red_min), (xmin, red_min)]
        ax.add_patch(plt.Polygon(poly_coords, color='red', alpha=opa))
        poly_coords = [(xmin, yel_max), (xmax, yel_max), (xmax, yel_min), (xmin, yel_min)]
        ax.add_patch(plt.Polygon(poly_coords, color='yellow', alpha=opa))
    plt.grid(color='gainsboro', linestyle='-', linewidth=.5)
    plt.box(False)
    return anvil.mpl_util.plot_image()

def build_plot(var_row, regidx, cap, cid, runde):
  # find out for which round
  if runde == 1:
    yr = 2025
  mdf_play = read_mdfplay25('mdf_play.npy', runde)
  print(mdf_play.shape)
  var_l = var_row['vensim_name']
  var_l = var_l.replace(" ", "_") # vensim uses underscores not whitespace in variable name
  varx = var_row['id']
  print('starting new plot ...')
  print('... build plot 272 var_l: ' + var_l)
  rowx = app_tables.mdf_play_vars.get(var_name=var_l)
  print('--- build plot 274 rowx: on next line')
  print (rowx)
  idx = rowx['col_idx']
  print(idx)
  if varx in[19, 21, 22, 35]: # global variable
    lx = idx # find location of variable in mdf
  else:
    lx = idx + regidx # find location of variable in mdf with reg offset
  print(var_l+' '+str(lx))
  dfv = mdf_play[:, [0, lx]]
  dfv_pd = pd.DataFrame(dfv)
#  print(dfv_pd)
  cur_title = 'ETI-' + str(int(var_row['sdg_nbr'])) + ': ' +var_row['sdg']
  cur_sub = var_row['indicator']
  cur_fig = make_png(dfv, var_row, regidx, yr, cur_sub)
  fdz = {'title' : cur_title, 'subtitle' : cur_sub, 'fig' : cur_fig, 'cap' : cap}
  return fdz

@anvil.server.callable
def launch_create_plots_for_slots(game_id, reg, ta, runde):
  task = anvil.server.launch_background_task('create_plots_for_slots', game_id, reg, ta, runde)
  return task

def get_all_vars_for_ta(ta):
  ta1 = mg.pov_to_Poverty[ta]
  print('get_all_vars_for_ta +++++ '+ta1)
  v_row = app_tables.sdg_vars.search(ta=ta1)
  vars = [r['vensim_name'] for r in app_tables.sdg_vars.search(ta=ta1)]
  return vars, v_row

@anvil.server.background_task
def create_plots_for_slots(game_id, region, single_ta, runde):
    cid = game_id
    if runde == 1:
      yr = 2025
    else:
      print('In put_plots_for_slots: We dont know which runde')
  # generate a dictionary of 
    regrow = app_tables.regions.get(abbr=region)
    regidx = int(regrow['pyidx'])
    my_time = datetime.datetime.now().strftime("%a %d %b %G")
    foot1 = 'mov240906 mppy GAME e4a 10reg.mdl'
    cap = foot1 + ' on ' + my_time
    vars_info_l, vars_info_rows = get_all_vars_for_ta(single_ta)
    for var_row in vars_info_rows:
      fdz = build_plot(var_row, regidx, cap, cid, runde)
#      print(fdz)
      app_tables.plots.add_row(game_id=game_id, title=fdz['title'], subtitle=fdz['subtitle'],
                              fig=fdz['fig'], cap=cap, runde=runde, ta=single_ta, reg=region)

@anvil.server.callable
def budget_to_db(yr, cid):
  print('IN budget_to_db ...')
  app_tables.budget.delete_all_rows()
  regs = mg.regs
  if yr == 2025:
    rx = 1440 - 321
    runde = 1
  else:
    print("Forgot to add reading later mdfs")
  mdf_bud = read_mdfplay25('mdf_play.npy', runde)
  ba = []
  rowx = app_tables.mdf_play_vars.get(var_name='Budget_for_all_TA_per_region')
  idx = rowx['col_idx']
  for i in range(0,10):
    ba.append(mdf_bud[rx, idx + i])
  print('IN put_budget ... ba ')
  print(ba)
  cpov = []
  rowx = app_tables.mdf_play_vars.get(var_name='Cost_per_regional_poverty_policy')
  idx = rowx['col_idx']
  for i in range(10):
    cpov.append(mdf_bud[rx, idx + i]) # poverty
  print('IN put_budget ... cpov ')
  print(cpov)
  
  cineq = [] 
  rowx = app_tables.mdf_play_vars.get(var_name='Cost_per_regional_inequality_policy')
  idx = rowx['col_idx']
  for i in range(10):
    cineq.append(mdf_bud[rx, idx + i]) # inequality
  print('IN put_budget ... cineq ')
  print(cineq)
  
  cemp = []
  rowx = app_tables.mdf_play_vars.get(var_name='Cost_per_regional_empowerment_policy')
  idx = rowx['col_idx']
  for i in range(10):
    cemp.append(mdf_bud[rx, idx + i]) # empowerment
  print('IN put_budget ... cemp ')
  print(cemp)
  
  cfood = []
  rowx = app_tables.mdf_play_vars.get(var_name='Cost_per_regional_food_policy')
  idx = rowx['col_idx']
  for i in range(10):
    cfood.append(mdf_bud[rx, idx + i]) # food
  print('IN put_budget ... cfood ')
  print(cfood)
  
  cener = []
  rowx = app_tables.mdf_play_vars.get(var_name='Cost_per_regional_energy_policy')
  idx = rowx['col_idx']
  for i in range(10):
    cener.append(mdf_bud[rx, idx + i]) # energy
  print('IN put_budget ... cener ')
  print(cener)

  for i in range(0,10):
    row = app_tables.budget.add_row(yr=yr, game_id=cid,reg=regs[i], runde=runde, bud_all_tas = ba[i],
          c_pov=cpov[i], c_ineq=cineq[i], c_emp=cemp[i], c_food=cfood[i], c_ener=cener[i])

@anvil.server.callable
def get_policy_budgets(reg, ta, yr, cid):
  TA = mg.pov_to_Poverty[ta]
  pol_list = []
  pols = app_tables.policies.search(ta=TA)
  for pol in pols:
    print(pol)
    pol_name = pol['name']
    pol_expl = pol['expl']
    pol_tltl = pol['tltl']
    pol_gl = pol['gl']
    pol_abbr = pol['abbr']
    fdz = {'pol_name' : pol_name, 'pol_expl' : pol_expl, 'pol_tltl' : pol_tltl, 'pol_gl' : pol_gl, 'pol_abbr' : pol_abbr}
    pol_list.append(fdz)
  return pol_list

import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import random
import string
import datetime
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
  regs = mg.regs
  pols = [r['abbr'] for r in app_tables.policies.search()]
  for runde in range(1,4):
    for re in regs:
      for p in pols:
        my_role = mg.Pov_to_pov[mg.pol_to_ta[p]]
        app_tables.roles_assign.add_row(game_id=game_id,role=my_role, taken = 4, reg=re, round=runde, pol=p)
        ## set up future which has no policies
      app_tables.roles_assign.add_row(game_id=game_id,role='fut', taken=0, reg=re, round=runde, pol='nopol')
  jetzt = datetime.datetime.now()
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
  pol_list = [r['abbr'] for r in app_tables.policies.search()]
  print(pol_list)
  tltl_list = [r['tltl'] for r in app_tables.policies.search()]
  print(tltl_list)
  gl_list = [r['gl'] for r in app_tables.policies.search()]
  print(gl_list)
  w_list = []
  for i in range(0,len(tltl_list)):
    mymin = tltl_list[i]
    mymax = gl_list[i]
    myrange = (mymax - mymin) 
    w = mymin + random.uniform(0, myrange)
    w_list.append(w)  # random policy value biased towards GL
  regs = mg.regs
  print(w_list)
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
          print(cid,' ' + str(runde)+' '+re+' '+p+' '+ta+' '+str(w2))
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

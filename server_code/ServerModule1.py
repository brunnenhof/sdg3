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

def get_tltl_or_random(pol):
  row = app_tables.policies.get(abbr=pol)
  tltl = row['tltl']
  gl = row['gl']
  mymin = tltl
  mymax = gl
  myhalf = (mymax - mymin) / 2
  wert = random.uniform(myhalf, mymax)  # random policy value biased towards GL
  return tltl, wert

@anvil.server.callable
def set_npbp(cid, npbp):
  #app_tables.roles_assign.delete_all_rows()
  pol_list = [r['abbr'] for r in app_tables.policies.search()]
  regs = mg.regs
  for runde in range(1,4):
    for re in regs:
        for p in pol_list:
          ta = mg.Pov_to_pov[mg.pol_to_ta[p]]
          row = app_tables.roles_assign.get(game_id=cid, round=runde, reg=re, pol=p, role=ta)
          tltl, wert = get_tltl_or_random(p)
          if re in npbp:
            taken = 2
            w2 = wert
          else:
            taken = 0
            w2 = tltl
          row.update(taken=taken, wert=w2)
  rs = app_tables.status.get(game_id=cid)
  rs.update(gm_status=1)

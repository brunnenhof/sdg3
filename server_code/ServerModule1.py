import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import random
import string
from . import mg

@anvil.server.callable
def generate_id():
  cid = ''.join(random.choices(string.ascii_uppercase, k=3))
  a = random.randint(10, 99)
  cid = cid + '-' + str(a) 
  while app_tables.status.has_row(q.like(cid)):
    cid = ''.join(random.choices(string.ascii_uppercase, k=4))
    a = random.randint(10, 99)
    d = random.randint(10, 99)
    cid = cid + '-' + str(d) + '-' + str(a) 
  return f"{cid}"

@anvil.server.callable
def set_roles(game_id):
  roles = mg.roles
  regs = mg.regs
  ro_nbr = mg.ro_nbr
  re_nbr = mg.re_nbr
  for re in regs:
    for ro_n in ro_nbr:
      for runde in range(1,4):
        app_tables.roles_taken.add_row(game_id=game_id,role_nbr=ro_n,role=roles[ro_n], taken = 4, reg=re, round=runde)

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
    app_tables.sdg.add_row(id=int(rr[0]), sdgNbr=int(rr[])  )

@anvil.server.callable
def upload_csv_pols(rows, re):
  app_tables.policies.delete_all_rows()
  for r in range(1, len(rows)):
    r = rows[r]
    rr = r.split(",")
    app_tables.policies.add_row(id=int(rr[0]), abbr=rr[1], name=rr[2], tltl=float(rr[3]), gl=float(rr[4]), expl=rr[5], ta=rr[6] )

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
  
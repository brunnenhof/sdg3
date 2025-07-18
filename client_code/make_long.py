import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from . import lu
from . import mg

def do_ta_to_longmini(role, lx):
  if role == "pov":
    return lu.ta_to_longmini_pov_str[lx]
  if role == "ineq":
    return lu.ta_to_longmini_ineq_str[lx]
  if role == "emp":
    return lu.ta_to_longmini_emp_str[lx]
  if role == "food":
    return lu.ta_to_longmini_food_str[lx]
  if role == "ener":
    return lu.ta_to_longmini_ener_str[lx]
  if role == "fut":
    return lu.ta_to_longmini_fut_str[lx]

def do_reg_to_longreg(reg, lx):
    if reg == "us":
      return lu.reg_to_longreg_us_str[lx]
    if reg == "af":
      return lu.reg_to_longreg_af_str[lx]
    if reg == "cn":
      return lu.reg_to_longreg_cn_str[lx]
    if reg == "me":
      return lu.reg_to_longreg_me_str[lx]
    if reg == "pa":
      return lu.reg_to_longreg_pa_str[lx]
    if reg == "la":
      return lu.reg_to_longreg_la_str[lx]
    if reg == "sa":
      return lu.reg_to_longreg_sa_str[lx]
    if reg == "ec":
      return lu.reg_to_longreg_ec_str[lx]
    if reg == "eu":
      return lu.reg_to_longreg_eu_str[lx]
    if reg == "se":
      return lu.reg_to_longreg_se_str[lx]

def get_user_detail():
    em = mg.my_email
    ro = app_tables.nutzer.get(email=em)
    cid = ro['game_id']
    mg.my_game_id = cid
    role = ro['role']
    mg.my_ministry = role
    reg = ro['reg']
    mg.my_reg = reg
    lx = ro["lang"]
    mg.my_lang = lx
    where = ro['where']
    return em, cid, reg, role, lx, where

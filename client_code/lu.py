import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#########
######### lu = language used
#########

top_thanks_msg = ''
top_thanks_title = ''
top_btn_help = ''
top_btn_thanks.text = mg.top_btn_thanks_en
top_btn_poc.text = 'PoC'
top_join_game.text = mg.top_join_game_en
top_start_game.text = mg.top_start_game_en
p_lb_choose_game.text = mg.p_lb_choose_game_en
p_btn_select_game.text = mg.p_btn_select_game_en
gm_board.text = mg.msg_gm_board_en
gm_board_info.content = mg.msg_gm_board_info_en
cb_af.text = mg.cb_af_tx_en
cb_us.text = mg.cb_us_tx_en
cb_cn.text = mg.cb_cn_tx_en
cb_me.text = mg.cb_me_tx_en
cb_sa.text = mg.cb_sa_tx_en
cb_la.text = mg.cb_la_tx_en
cb_pa.text = mg.cb_pa_tx_en
cb_ec.text = mg.cb_ec_tx_en
cb_eu.text = mg.cb_eu_tx_en
cb_se.text = mg.cb_se_tx_en
gm_reg_npbp.text = mg.gm_reg_npbp_tx_en
gm_card_wait_1_info.content = mg.gm_card_wait_1_info_tx_en
gm_card_wait_1_btn_check.text = mg.gm_card_wait_1_btn_check_tx_en
gm_start_round.text = mg.gm_card_wait_1_btn_kick_off_round_1_tx_en
setup_npbp_label.text = mg.setup_npbp_label_tx_en
pcr_rb_af.text = mg.cb_af_tx_en
pcr_rb_us.text = mg.cb_us_tx_en
pcr_rb_cn.text = mg.cb_cn_tx_en
pcr_rb_me.text = mg.cb_me_tx_en
pcr_rb_sa.text = mg.cb_sa_tx_en
pcr_rb_la.text = mg.cb_la_tx_en
pcr_rb_pa.text = mg.cb_pa_tx_en
pcr_rb_ec.text = mg.cb_ec_tx_en
pcr_rb_eu.text = mg.cb_eu_tx_en
pcr_rb_se.text = mg.cb_se_tx_en
pcr_rb_pov.text = mg.cb_pov_tx_en
pcr_rb_ineq.text = mg.cb_ineq_tx_en
pcr_rb_emp.text = mg.cb_emp_tx_en
pcr_rb_food.text = mg.cb_food_tx_en
pcr_rb_ener.text = mg.cb_ener_tx_en
pcr_rb_fut.text = mg.cb_fut_tx_en
pcr_title.text = mg.pcr_title_tx_en
pcr_col_left_title.text = mg.pcr_col_left_title_tx_en
pcr_col_right_title.text = mg.pcr_col_right_title_tx_en
pcr_submit.text = mg.pcr_submit_tx_en
fut_not_all_logged_in.text = mg.fut_not_all_logged_in_tx_en
pcgd_title.text = mg.pcr_title_tx_en
pcgd_info_rd1.content = mg.pcgd_rd1_info_tx_en
pcgd_generating.text = mg.pcgd_generating_tx_en
dec_info.content = mg.dec_info_tx_en
dec_title.text = mg.dec_title_tx_en
pcgd_advance.text = mg.pcgd_advance_tx_en
refresh_numbers.text = mg.refresh_numbers_tx_en
submit_numbers.text = mg.submit_numbers_tx_en
fut_info.content = mg.fut_info_tx_en
fut_bud_lb1.text = mg.fut_bud_lb1_tx_en
fut_bud_lb2.text = mg.fut_bud_lb2_tx_en 
fut_but_lb3.text = mg.fut_bud_lb3_tx_en 
cpf_lb.text = mg.cfpov_tx_en
cpf_lb2.text = mg.cfpov_lb_tx_en 
cpf_ineq_lb.text = mg.cfineq_tx_en
cpf_ineq_lb2.text = mg.cfineq_lb_tx_en 
cpf_emp_lb.text = mg.cfemp_tx_en
cpf_emp_lb2.text = mg.cfemp_lb_tx_en 
cpf_food_lb.text = mg.cffood_tx_en
cpf_food_lb2.text = mg.cffood_lb_tx_en 
cpf_ener_lb.text = mg.cfener_tx_en
cpf_ener_lb2.text = mg.cfener_lb_tx_en 
gm_card_wait_1_temp_title.text = mg.gm_card_wait_1_temp_title_tx_en
credits.text = mg.credits_btn_tx_en

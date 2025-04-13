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
game_step = 0
###
### comment this out in production and ask interactively
not_played_by_players = ['us', 'af', 'cn', 'sa', 'la', 'pa', 'eu', 'se']
###
### below does not change, evah!
roles = ['pov', 'ineq', 'emp', 'food', 'ener', 'fut']
ro_nbr = [0, 1, 2, 3, 4, 5]
regs = ['us', 'af', 'cn', 'me', 'sa', 'la', 'pa', 'ec', 'eu', 'se']
re_nbr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
top_title = 'END-times'
top_btn_thanks = 'Danke'
top_btn_start = 'Start a new game as organizer'
top_btn_join = 'JOIN a game as player'
top_btn_help = 'Help'
top_join_game = 'JOIN a game as player'
top_start_game = 'Start a game as organizer'

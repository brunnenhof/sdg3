from ._anvil_designer import homeTemplate
from anvil import *
from .. import mg
import webbrowser
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import mg


class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.top_title.text = mg.top_title
    self.top_btn_help.text = mg.top_btn_help
    self.top_btn_thanks.text = mg.top_btn_thanks
    self.top_btn_poc.text = 'PoC'
    self.top_join_game.text = mg.top_join_game
    self.top_start_game.text = mg.top_start_game
    self.p_lb_choose_game.text = mg.p_lb_choose_game
    self.p_btn_select_game.text = mg.p_btn_select_game

  def top_btn_thanks_click(self, **event_args):
    alert(content="... to our Alpha testers, the students in the SW101 course at the Realschule Baesweiler during April 2024 taught by René Langohr, and all the beta testers.", title="Thank you", large=True)

  def top_btn_poc_click(self, **event_args):
    alert("Neither the user interface nor the server code is elegant nor efficient. Contact us if you can help making either or all better.",
         title="So far, this app is a Proof of Concept")

  def top_btn_help_click(self, **event_args):
    webbrowser.open_new("http://sdggamehelp.blue-way.net")

  def top_start_game_click(self, **event_args):
    game_id = anvil.server.call('generate_id')
    app_tables.status.add_row(game_id=game_id, closed=0, current_gm=0, current_p=0, roles_avail=4)
    msg = mg.gm_id_msg1 + game_id + mg.gm_id_msg2
    alert(msg, title=mg.gm_id_title)
    anvil.server.call('set_roles', game_id)
    msg = mg.top_roles_setup_msg + game_id
    alert(msg)

  def top_join_game_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    #print(f"The file's name is: {file.name}")
    #print(f"The number of bytes in the file is: {file.length}")
    #print(f"The file's content type is: {file.content_type}")
#    print(f"The file's contents are: '{file.get_bytes()}'")
    b = file.get_bytes()
    bb = b.decode("utf-8")
    bbb = bb.splitlines()
    print(bbb)
    anvil.server.call('upload_csv_sdg', bbb, 'regs')

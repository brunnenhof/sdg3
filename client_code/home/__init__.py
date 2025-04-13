from ._anvil_designer import homeTemplate
from anvil import *
from .. import mg
import webbrowser


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
    """This method is called when the button is clicked"""
    pass

  def top_join_game_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

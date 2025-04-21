from ._anvil_designer import cpf_emp_templateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class cpf_emp_template(cpf_emp_templateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.pol_emp_name.text = self.item['pol_emp_name']
    self.pol_emp_amount.text = self.item['pol_emp_amount']

# Copyright (c) 2021, moo and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Moomembership(Document):
	def before_save(self):
     	 m = self.fullname 

# Copyright (c) 2025, asd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Demo_Server(Document):
	pass

@frappe.whitelist()
def insert_record():
	data = frappe.new_doc("Demo_Server")
	data.first_name = 'Jake'
	data.last_name = 'Jay'
	

	data.insert()
	
	# data.db.commit()
	return "Record inserted successfully"
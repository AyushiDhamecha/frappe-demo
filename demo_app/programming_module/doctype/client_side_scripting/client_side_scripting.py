# # Copyright (c) 2025, asd and contributors
# # For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

# ------------------------------------ frappe_call------------------------------
class ClientSideScripting(Document):
		pass

@frappe.whitelist()
def insert_record():
	data = frappe.new_doc("Client Side Scripting")
	data.first_name = 'Jake'
	data.last_name = 'Jay'
	

	data.insert()

	# data.db.commit()
	return "Record inserted successfully"

# 	def validate(self):
# 		self.pass

	

# # @frappe.whitelist()
# # def frappe_call(msg):

# # 		# frappe.msgprint(msg)
# # 		# self.mobail_no = 76546267367
# # 	return "Hii this massege from frappe_call"

# @frappe.whitelist()
# def new_document(self):
# 	doc = frappe.new_doc('Client Side Scripting')
# 	doc.first_name = 'Jake'
# 	doc.last_name = 'Jay'
# 	doc.age = 54
# 	# doc.append("family_members",{ "name1":"meena", "relation":"sister", "age":14})
# 	doc.insert()
# 	doc.db.commit()






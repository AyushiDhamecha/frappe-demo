# Copyright (c) 2025, asd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StudentDoc(Document):
	pass

@frappe.whitelist()
def new_document(student_name ,email,age ):
	doc = frappe.new_doc('Student Doc')
	doc.student_name = student_name
	doc.email = email
	doc.age = age
	# doc.append("family_members",{ "name1":"meena", "relation":"sister", "age":14})
	doc.insert()
	frappe.db.commit()

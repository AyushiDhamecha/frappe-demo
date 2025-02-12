# Copyright (c) 2025, asd and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document	


# --------------------------- Events -------------------------------------------

class ServerSideScripting(Document):
# --------------------------------- frm call -----------------------------------------
	# @frappe.whitelist()
	# def frm_call(self,msg): 

	# 	# frappe.msgprint(msg)
	# 	# self.mobail_no = 76546267367
	# 	return "Hii this massege from frm_call"

	# def validate(self):
	# 	frappe.msgprint("Hello")	


# --------------------------------- fetching value ---------------------------------
	# def validate(self):

	# 	frappe.msgprint(_("Hello My full name is '{0}'").format(self.first_name+" "+self.middle_name+" "+self.last_name))

	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(_(
	# 			"{0}. The family member is '{1}' and relation is '{2}'"
	# 		).format(row.idx,row.name1,row.relation))

# ------------------------------- getting doc-------------------------------------


	# def validate(self):
	# 	frappe.msgprint(_("Hello My full name is '{0}'").format(self.first_name+" "+self.middle_name+" "+self.last_name))
	# 	self.get_document()
		

	# def get_document(self):
	# 	# ---------------------(doctype name )-------(doctype field name)-----
	# 	doc = frappe.get_doc('Client Side Scripting',self.client_side_doc)

	# 	frappe.msgprint(_("The First name is {0} and Age is {1}".format(doc.first_name,doc.age)))

	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(_(
	# 			"{0}. The family member is '{1}' and relation is '{2}'"
	# 		).format(row.idx,row.name1,row.relation))


# ---------------------------- New doc and delete doc --------------------------

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Jake'
	# 	doc.last_name = 'Jay'
	# 	doc.age = 13
	# 	doc.append("family_members",{ "name1":"Jain", "relation":"sister", "age":14})
	# 	doc.insert()

# ------------------------------- Delete Doc -------------------------------------

	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting','PR-0011')

# --------------------------------	get list ------------------------------------

	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting',
	# 			filters = {
	# 				'enable':1
	# 			},
	# 			fields = ['first_name','age']
	# 			)

	# 	for d in doc:
	# 		frappe.msgprint(_("The First name is {0} and Age is {1}".format(d.first_name,d.age)))


# -----------------------------------get value and set value -------------------------------

	# ---------------getting value---------------
	# def validate(self):
	# 	self.get_value()
	
	# def get_value(self):
	# 	first_name,age = frappe.db.get_value('Client Side Scripting','PR-0010',['first_name','age'])

	# 	frappe.msgprint(_("The parent first name is {0} and age is {1}").format(first_name,age))


	# ------------------set value-----------------------
	# def validate(self):
	# 	self.set_value()
	
	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting','PR-0010','age',25,)
	# 	first_name,age = frappe.db.get_value('Client Side Scripting','PR-0010',['first_name','age'])
	# 	frappe.msgprint(_("The parent first name is {0} and new age is {1}").format(first_name,age))


# -------------------------------------    SQL    ----------------------------------------------

	# def validate(self):
	# 	self.sql()

	# def sql(self):

	# 	data  = frappe.db.sql("""
	# 							SELECT
	# 							   first_name,
	# 							   age
	# 							FROM
	# 								`tabClient Side Scripting`
	# 							WHERE
	# 								enable = 1
	# 						""",as_dict = 1)

	# 	for d in data:
	# 		frappe.msgprint(_("The enabled first name is {0} and age is {1}").format(d.first_name,d.age))


# ----------------------------------------------------------------------------------------------------

# --------------------------------------------Controllers----------------------------------------------

	# def validate(self):
	# 	self.get_full_name()

	# def get_full_name(self):
    #     """Returns the person's full name"""
    #     return  f"{self.first_name} {self.last_name}"



    def validate(self):
        if self.age <= 18:
            frappe.throw("Person's age must be at least 18")

	# def before_save(self):
	# 	self.full_name = f'{self.first_name} {self.last_name}'

	# def after_insert(self):
	# 	frappe.msgprint("Thank you for registering")
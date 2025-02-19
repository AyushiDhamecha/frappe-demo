import frappe
from frappe import _

# @frappe.whitelist(allow_guest=True)
# def get_document(student_name,age,email):
       
#         doc = frappe.get_doc({
#         "doctype": "Student",
#         "student_name": student_name,
#         "age": age,
#         "email": email
#         })
#         doc.insert()
#         frappe.db.commit()
#         return doc
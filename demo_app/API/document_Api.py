import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
# def test():
#     return frappe.rename_doc('Demo_Client', 'melm3dcat9', 'demo-Client-001')

# def test():
#     doc = frappe.new_doc('Demo_Client')
#     doc.title = 'New Doc'
#     doc.insert()
#     return frappe.get_last_doc('Demo_Client',filters={"first_name": "aayu"})


# def get_document(docname):
#     # """Fetch a document from a specific Doctype"""

#         return frappe.get_doc('Demo_Client', docname)

# def get_document(doctype):
       
#         return frappe.get_all(doctype, fields=["first_name", "full_name", "age"])


# def get_document(name):
       
#         return frappe.get_doc('Server Side Scripting',name, fields=["first_name", "full_name", "age"])

def new_document(Doctype):
        doc = frappe.new_doc(Doctype)
        doc.title = 'New Doc'
        doc.insert()
        frappe.db.commit() 
        return doc
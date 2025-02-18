import frappe

def get_context(context):
    context.users = frappe.get_list("Server Side Scripting", fields=["first_name", "date"])
 
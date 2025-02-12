import frappe

def get_context(context):
    context.title = "Dynamic Page"
    context.message = "This is a dynamically generated page in Frappe." 
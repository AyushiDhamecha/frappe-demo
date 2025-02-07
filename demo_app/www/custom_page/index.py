import frappe

def get_context(context):
    context.title = "Custom Page"
    context.message = "Hello from Frappe Web View!"
    return context
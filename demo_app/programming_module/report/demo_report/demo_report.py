# Copyright (c) 2025, asd and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns=[
		{"fieldname": "name", "label": _("Account ID"), "fieldtype": "Data", "width": 150},
		{"fieldname": "account_name", "label": _("Account Name"), "fieldtype": "Data", "width": 200},
        {"fieldname": "balance", "label": _("Balance"), "fieldtype": "Currency", "width": 120},
        {"fieldname": "account_type", "label": _("Account Type"), "fieldtype": "Data", "width": 150},
	],

	data = [
		{
		'account': 'Application of Funds (Assets)',
		'currency': 'INR',
		'balance': '15182212.738'
		},
		{
		'account': 'Current Assets - GTPL',
		'currency': 'INR',
		'balance': '17117932.738'
		},
	]
	return columns, data

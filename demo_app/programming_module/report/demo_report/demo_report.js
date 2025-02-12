// Copyright (c) 2025, asd and contributors
// For license information, please see license.txt

frappe.query_reports["demo-report"] = {
	"filters": [
		{
			'fieldname': 'account',
			'label': _('Account'),
			'fieldtype': 'Link',
			'options': 'Account'
			},
			{
			'fieldname': 'currency',
			'label': _('Currency'),
			'fieldtype': 'Link',
			'options': 'Currency'
			},
			{
			'fieldname': 'balance',
			'label': _('Balance'),
			'fieldtype': 'Currency',
			'options': 'currency'
			}
	]
};

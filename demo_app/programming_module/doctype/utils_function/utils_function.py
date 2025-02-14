# Copyright (c) 2025, asd and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import today, now, add_days, add_months, add_years, get_datetime, formatdate, add_to_date,date_diff, money_in_words,month_diff, getdate,validate_phone_number,pretty_date
from frappe.model.document import Document


class UtilsFunction(Document):

	def validate(self):
		# self.date_1 = today()
		d1 = getdate('2000-03-18')
		d2 = getdate('2000-05-18')
		self.date_diffrence = date_diff(d2, d1)
		self.month_diffrence = month_diff(d2, d1)
		self.money_in_words = money_in_words(self.money)
		
		# self.read_only_wgox = validate_phone_number(self.phone_no)	

	# print(pretty_date(now()))
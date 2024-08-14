# Copyright (c) 2020, Vesper Solutions Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document

# import frappe
import verp


class IncomeTaxSlab(Document):
	def validate(self):
		if self.company:
			self.currency = verp.get_company_currency(self.company)

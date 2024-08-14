# Copyright (c) 2018, Vesper Solutions Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document

from hrms.hr.utils import validate_active_employee


class TravelRequest(Document):
	def validate(self):
		validate_active_employee(self.employee)

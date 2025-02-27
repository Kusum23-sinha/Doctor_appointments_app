# Copyright (c) 2024, kusum and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Appointment(Document):
	def after_insert(self):
		print("Your queue number is: ", self.add_to_appointment_queue())

	def add_to_appointment_queue(self):
		q = frappe.get_doc("Appointment Queue", {
			"date": self.date,
			"shift": self.shift,
			"clinic": self.clinic,
		})	

		q.append("queue", {"appointment": self.name, "status": "Pending"})
		q.save(ignore_permissions=True)

		return len(q.queue)
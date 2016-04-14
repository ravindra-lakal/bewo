from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Master"),
			"items": [
				{
					"type": "doctype",
					"name": "Category"
				},
				{
					"type": "doctype",
					"name": "Sub Category"
				},
				{
					"type": "doctype",
					"name": "Group Store"
				},
				{
					"type": "doctype",
					"name": "Store"
				},
				{
					"type": "doctype",
					"name": "Item Supplier Mapping"
				},
				{
					"type": "doctype",
					"name": "Warehouse"
				},
			]

		},
		{
			"label": _("Setup"),
			"icon": "icon-facetime-video",
			"items": [
				{
					"type": "doctype",
					"name": "BEWO POS Configurations"
				},
			]
		},
		{
			"label": _("Report"),
			"icon": "icon-facetime-video",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"doctype": "Item",
					"icon": "icon-eye-open",
					"name": "Item Variant Price List"
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype": "Store",
					"icon": "icon-eye-open",
					"name": "Store Details"
				},
			]
		}
	]

# Copyright (c) 2013, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	data = get_data()
	return columns, data

def get_data():
	if 1==1:
		result = frappe.db.sql("""select 
		    CASE WHEN b.variant_of != "" then (select variant_of from `tabItem` a where a.item_code=b.item_code)
		    ELSE (select item_code from `tabItem` a where a.item_code=b.item_code)
		    END AS "Item:Link/Item:150",
		    inventory_maintained_by as "Inventory Maintained By::100",
		    c_barcode as "Barcode::100",
		    shortcode as "Shortcode::100",
		    category as "Category::120",
		    sub_category as "Sub Category::120",
		    brand as "Brand::80",
		    mrp as "MRP:Currency:100",
		    retail_rate as "Retail Price:Currency:100",
		    wholesale_rate as "Wholesale Price:Currency:100"
		from
		 `tabItem` b where b.has_variants=0
		order by item_code""",as_list=1,debug=1)

		total_item = frappe.db.sql("""select count(name) from tabItem where ISNULL(variant_of)""",as_list=1,debug=1)

		abc = total_item[0][0]
		# result.append([])
		# result.append(["Total Item",str(total_item[0][0])])
		return result
	else:
		result = []
		return result	

def get_total_item():
	return "11"

# def get_conditions(filters):
# 	cond = ''
# 	if filters.get('checklist_requisition') and filters.get('status') and filters.get('user'):
# 		cond = "where project = '{0}' and status = '{1}' and user = '{2}'".format(filters.get('checklist_requisition'),filters.get('status'),filters.get('user'))

# 	elif filters.get('checklist_requisition') and filters.get('status'):
# 		cond = "where project = '{0}' and status = '{1}'".format(filters.get('checklist_requisition'),filters.get('status'))

# 	elif filters.get('checklist_requisition') and filters.get('user'):
# 		cond = "where project = '{0}' and user = '{1}'".format(filters.get('checklist_requisition'),filters.get('user'))

# 	elif filters.get('status') and filters.get('user'):
# 		cond = "where status = '{0}' and user = '{1}'".format(filters.get('status'),filters.get('user'))

# 	elif filters.get('user'):
# 		cond = "where user = '{0}'".format(filters.get('user'))

# 	elif filters.get('checklist_requisition'):
# 		cond = "where project = '{0}' ".format(filters.get("checklist_requisition"))

# 	elif filters.get('status'):
# 		cond = "where status='{0}'".format(filters.get("status"))	
# 	return cond


def  get_colums():
	columns = ["Item:Link/Item:160"]+ ["Inventory Maintained By::100"] +["Barcode::100"]\
		+["Shortcode::100"]+ ["Category::130"] +["Sub Category::130"]\
		+ ["Brand::100"]+ ["MRP:Currency:100"]+ ["Retail Price:Currency:100"] +["Wholesale Price:Currency:100"]
	return columns




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
	    `tabGroup Store`.name as group_store,
	    `tabStore`.name as store_name,
	    `tabWarehouse List`.warehouse as warehouse,
	    CASE WHEN 5!=6 then (select name from `tabTill` a where a.store=`tabStore`.name)
	    ELSE " "
	    END AS till
		from
		 `tabStore`, `tabWarehouse List`, `tabStore List`, `tabGroup Store`
		where 
		   `tabWarehouse List`.parent = `tabStore`.name and
		   `tabStore List`.parent = `tabGroup Store`.name and
		   `tabStore List`.store =  `tabStore`.name
		order by `tabStore`.name""",as_list=1,debug=1)

		total_item = frappe.db.sql("""select count(name) from tabItem where ISNULL(variant_of)""",as_list=1,debug=1)

		abc = total_item[0][0]
		result.append([])
		result.append(["Total Item",str(total_item[0][0])])
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
	columns = [_("Group Store") + ":Link/Group Store:150"]\
	+ [_("Store") + ":Link/Store:150"]\
	+ [_("Warehouse") + ":Link/Warehouse:140"] + [_("Till") + ":Link/Till:140"] \
	
	return columns




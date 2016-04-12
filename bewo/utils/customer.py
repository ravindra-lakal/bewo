import frappe

def on_trash(doc, method):
	is_valid_customer(doc.name)

def before_rename(doc, method, old_doc, new_doc, mearge):
	is_valid_customer(old_doc)

def is_valid_customer(docname):
	default_customer = frappe.db.get_value("BEWO POS Configurations", "BEWO POS Configurations", "default_customer")
	if docname == default_customer:
		frappe.throw("Can not delete the default customer '%s'"%docname)
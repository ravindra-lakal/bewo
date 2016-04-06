import frappe
import json

from store import validate_store
from device import validate_device
from request import validate_request

@frappe.whitelist()
def addSalesRecords(data):
	"""parse sales data from bewo pos devices and create sales log"""
	try:
		args = json.loads(data)
		validate_request("add_sales", args)

		store = args.pop("store")
		device = args.pop("device")

		if all([store, device]):
			validate_store(store)
			validate_device(store, device)

			return create_invoices(args)
		else:
			raise Exception("Invalid Store / Device ID")

	except Exception, e:
		raise e

def create_invoices(args):
	""" validate and save invoices """
	sales = args.pop("sales")
	if not sales:
		raise Exception("Sales Record not found")

	for record in sales:
		validate_sales_record(record)
	return "success"

def validate_sales_record(sales_order):
	""" validate product, product stock, bill number """
	validate_bill_number(sales_order.get("strBillNumber"))
	validate_products(sales_order.get("products"))

def validate_bill_number(bill_no):
	""" check if with same bill no already one invoice is available """
	pass

def validate_products(products):
	""" check if product is available and check the stock """

	if not products:
		raise Exception("Invalid Products value")

	invalid_items = []
	invalid_stock_balance_item = []

	for item in products:
		print frappe.db.get_value("Item", item.get("strProductCode"), "name")
		if not frappe.db.get_value("Item", item.get("strProductCode"), "name"):
			invalid_items.append(item.get("strProductCode"))
		else:
			# valid item check stock balance
			pass

	if any([invalid_items, invalid_stock_balance_item]):
		return False
	else:
		return True
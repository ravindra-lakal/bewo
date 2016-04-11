import frappe
import json

from store import validate_store
from device import validate_device
from request import validate_request
from bewo.utils.sales_utils import validate_sales_record, create_sales_return_invoice

@frappe.whitelist()
def addSalesReturnRecords(data):
	"""parse sales data from bewo pos devices and create sales log"""
	try:
		args = json.loads(data)
		validate_request("add_sales_return", args)

		store = args.pop("store")
		device = args.pop("device")

		if all([store, device]):
			validate_store(store)
			validate_device(store, device)

			return validate_create_sales_return(args, device)
		else:
			raise Exception("Invalid Store / Device ID")

	except Exception, e:
		import traceback
		print traceback.print_exc()
		raise e

def validate_create_sales_return(args, device):
	""" validate and save invoices """
	response = []
	sales_return = args.pop("salesReturn")
	if not sales_return:
		raise Exception("Sales Return Record not found")

	for record in sales_return:
		res = validate_sales_record(record, is_sales_return=True)
		
		if not res.get("is_valid"):
			bill_no = record.get("strBillNumber")
			response.append({
				bill_no: {
					"invStatus": 500,
					"errors": res.get("errors")
				}
			})
		else:
			res = create_sales_return_invoice(record, device, res.get("sales_invoice"))
			response.append(res)

	return response
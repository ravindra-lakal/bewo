import frappe
from test_records import records, index_mapping

@frappe.whitelist()
def get(resource):
	store_id = txn = txn_id = None

	if not resource:
		report_error(417,"Input not provided")

	if len(resource) >= 1:
		store_id = resource[0]

	if len(resource) >= 2:
		txn = resource[1]

	if len(resource) >= 3:
		txn_id = resource[2]

	if all([txn, txn_id]):
		transactions = records.get(store_id).get(txn) if records.get(store_id) else {}
		if not transactions:
			return {}
		else:
			key = index_mapping.get(txn)
			return filter((lambda rec: rec.get(key) == txn_id), transactions)
	elif txn and not txn_id:
		return records.get(store_id).get(txn) if records.get(store_id) else {}
	else:
		return records.get(store_id) or {}

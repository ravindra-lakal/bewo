import frappe
from test_records import records, index_mapping

@frappe.whitelist()
def get(resource):
	store_id = txn = txn_id = None
	if not resource:
		return report_error(417,"Input not provided")

	if len(resource) >= 1:
		store_id = resource[0]

	if len(resource) >= 2:
		txn = resource[1]

	if len(resource) >= 3:
		txn_id = resource[2]

	# validate store id
	# validate txn type

	if "count" in [txn, txn_id]:
		return get_count(store_id=store_id, txn=txn, txn_id=txn_id)
	else:
		return get_records(store_id=store_id, txn=txn, txn_id=txn_id)

def get_count(store_id=None, txn=None, txn_id=None):
	""" get total count of records"""
	from test_records import records, index_mapping

	if txn == txn_id:
		return report_error(417, "Invalid Input / URL")

	if all([txn, txn_id]):
		if txn == "count":
			return report_error(417, "Invalid URL")
		elif txn_id == "count":
			transactions = records.get(store_id).get(txn) if records.get(store_id) else {}
			if not transactions:
				return { "total_records": { txn: 0 } }
			else:
				return { "total_records": { txn: len(transactions) } }

	elif txn and not txn_id:
		result = { txn:0 for txn in index_mapping }
		transactions = records.get(store_id) if records.get(store_id) else {}
		
		for txn, records in transactions.iteritems():
			result.update({ txn: len(records) })

		return { "total_records": result }

def get_records(store_id=None, txn=None, txn_id=None):
	""" get the total records """
	from test_records import records, index_mapping

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

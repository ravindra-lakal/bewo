import frappe
from api_handler.api_handler.exceptions import *
from test_records import records, index_mapping
import json

@frappe.whitelist()
def get(resource):
	print ("Resource is",resource)
	print "Length of resource is",len(resource)
	
	store_id = txn = txn_id = None
	if not resource:
		raise InvalidDataError("Input not provided")

	if len(resource) >= 1:
		store_id = resource[0]

	if len(resource) >= 2:
		txn = resource[1]

	if len(resource) >= 3:
		txn_id = resource[2]

	validate_store(store_id)
	# validate txn type

	if "count" in [txn, txn_id]:
		return get_count(store_id=store_id, txn=txn, txn_id=txn_id)
	else:
		return get_records(store_id=store_id, txn=txn, txn_id=txn_id)
		# a=[txn,txn_id]
		# print "List is",a

def get_count(store_id=None, txn=None, txn_id=None):
	""" get total count of records"""
	# from test_records import records, index_mapping

	# if txn == txn_id:
	# 	return InvalidURL("Invalid Input / URL")

	# if all([txn, txn_id]):
	# 	if txn == "count":
	# 		return InvalidURL("Invalid URL")
	# 	elif txn_id == "count":
	# 		transactions = records.get(store_id).get(txn) if records.get(store_id) else {}
	# 		if not transactions:
	# 			return { "total_records": { txn: 0 } }
	# 		else:
	# 			return { "total_records": { txn: len(transactions) } }

	# elif txn and not txn_id:
	# 	result = { txn:0 for txn in index_mapping }
	# 	transactions = records.get(store_id) if records.get(store_id) else {}
		
	# 	for txn, records in transactions.iteritems():
	# 		result.update({ txn: len(records) })

	# 	return { "total_records": result }
	filters=json.loads(filters)
	print "type of filters is",type(filters)
	filters.append({"variant_of":""})
	items=frappe.db.get_all("Item",fields=["item_name","brand","disabled","category","inventory_maintained_by","mrp","wholesale_rate","retail_rate","purchase_rate","variant_of"],
		filters=filters)
	count=0
	for item in items:
		count+=1
	return count


def get_records(store_id=None, txn=None, txn_id=None):
	""" get the total records """
	# from test_records import records, index_mapping

	# if all([txn, txn_id]):
	# 	transactions = records.get(store_id).get(txn) if records.get(store_id) else {}
	# 	if not transactions:
	# 		print "transactions are",transactions
	# 		return {}
	# 	else:
	# 		key = index_mapping.get(txn)
	# 		return filter((lambda rec: rec.get(key) == txn_id), transactions)
	# elif txn and not txn_id:
	# 	return records.get(store_id).get(txn) if records.get(store_id) else {}
	# else:
	# 	return records.get(store_id) or {}
	# Format1
	# try:
	# 	items=frappe.db.get_all("Item",fields=["item_name","brand","disabled","category","inventory_maintained_by","mrp","wholesale_rate","retail_rate","purchase_rate","variant_of"],
	# 	filters={"variant_of":""})
	# 	products=[]
	# 	# product={}

	# 	for item in items:
	# 		product={}
	# 		product.update({
	# 			"strProductName":item.get("item_name"),
	# 			"strBrand":item.get("brand"),
	# 			"strcategory":item.get("category"),
	# 			"type":item.get("inventory_maintained_by"),
	# 			"price":[{"dblmrp":item.get("mrp"),"dblSellingPrice_Wholesale":item.get("wholesale_rate"),"dblSellingPrice_Retail":item.get("retail_rate"),"dblPurchasePrice":item.get("purchase_rate")}]
	# 			})
			
			

	# 		products.append(product)
	# 	return products


		
		
	# except Exception, e:
	# 	print e
		 
	# return items
	# Format 2
	try:
		products=[]
		status=None
		product={}
		items=frappe.db.get_all("Item",fields=["item_name","brand","disabled","category","inventory_maintained_by","mrp","wholesale_rate","retail_rate","purchase_rate","variant_of","has_variants"],
		filters={})
		# var = item.get("item_name")
		# items=frappe.db.get_all("Item",fields=["item_name","variant_of","mrp"],
		# filters={"item_name":var})
        
		# products=[]
		# status=None
		# product={}
		
		 
		for item in items:
			# mrp=str(item.get("wholesale_rate"))+str(item.get("retail_rate"))+str(item.get("purchase_rate"))
			if  item.get("variant_of")==None:
				if item.get("disabled")==0:
					status="Active"
				else:
					status="Disabled"
				product={}
				
				# mrp = ",".join([str(item.get("wholesale_rate")), str(item.get("retail_rate")), str(item.get("purchase_rate"))])

				mrp=",".join([str(item.get("mrp"))])
				product.update({
					"strProductName":item.get("item_name"),
					"strBrand":item.get("brand"),
					"strcategory":item.get("category"),
					"type":item.get("inventory_maintained_by"),
					# "dblmrp":item.get("mrp"),
					"status":status,
					"dblPurchasePrice":item.get("purchase_rate"),
					"dblSellingPrice_Retail":item.get("retail_rate"),
					"dblSellingPrice_Wholesale":item.get("wholesale_rate"),
					"dblMRP":[mrp]
					# "dblMRP":[mrp]
					})
				products.append(product)
			if item.get("has_varients")==1:
				print "Inside variants"
				product={}
				item_name=item.get("name")
				variants=frappe.db.get_all("Item",fields=["mrp"],
				filters={"variant_of":item_name})
				for variant in variants:
					mrp+=[str(variant.get("mrp"))]

				product.update({
					"strProductName":item.get("item_name"),
					"strBrand":item.get("brand"),
					"strcategory":item.get("category"),
					"type":item.get("inventory_maintained_by"),
					# "dblmrp":item.get("mrp"),
					"status":status,
					"dblPurchasePrice":item.get("purchase_rate"),
					"dblSellingPrice_Retail":item.get("retail_rate"),
					"dblSellingPrice_Wholesale":item.get("wholesale_rate"),
					"dblMRP":[mrp]
					})
				products.append(product)
		return products




			
	except Exception, e:
		print e

    
    

def validate_store(store):
	""" validate store """
	# create Store Profile Single DocType save store ID to validate
	pass
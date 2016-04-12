import json
import frappe
from schema.schema import get_request_schema

def validate_request(method, request):
	""" validate request schema """
	schema = get_request_schema(method)
	if not schema:
		raise Exception("Invalid Request : Schema Not Found")

	validate_request_schema(schema, "request_header", request)
	# headers = schema.get("request_headers")
	# for key, value in args.iteritems():
	# 	print key, value
	# pass

def validate_request_schema(schema, _meta_key, args):
	validate_manditory_field(schema.get(_meta_key), args)
	validate_field_type(schema.get(_meta_key), args)
	
	to_validate = { field: _meta for field, _meta in schema.get(_meta_key).iteritems() if _meta.get("fieldtype") in ["list", "dict"] and _meta.get("schema")}
	for field, _meta in to_validate.iteritems():
		for request in args.get(field):
			validate_request_schema(schema, _meta.get("schema"), request)

def validate_manditory_field(schema, args):
	""" check manditory and extra fields in request """
	missing_fields = [field for field in schema.keys() if field not in args.keys() and schema.get(field).get("reqd")]
	extra_fields = [field for field in args.keys() if field not in schema.keys()]

	if any([missing_fields, extra_fields]):
		err_msg = "Invalid request parameters"
		if missing_fields: err_msg += ", Missing Fields : (%s)"%(",".join(missing_fields))
		if extra_fields: err_msg += ", Extra Fields : (%s)"%(",".join(extra_fields))

		raise Exception(err_msg)

def validate_field_type(schema, args):
	""" check field type """
	err_msg = "Invalid DataType for field : {} expected type : {}"

	for field, value in args.iteritems():
		if not all([schema.get(field), schema.get(field).get("fieldtype")]):
			raise Exception("Invalid Schema")
		
		fieldtype = schema.get(field).get("fieldtype")
		if fieldtype == "int":
			if not isinstance(value, int): raise Exception(err_msg.format(field, "Int"))
		elif fieldtype == "float":
			if not isinstance(value, float): raise Exception(err_msg.format(field, "Float"))
		elif fieldtype == "basestring":
			if not isinstance(value, basestring): raise Exception(err_msg.format(field, "String"))
		elif fieldtype == "list":
			if not isinstance(value, list): raise Exception(err_msg.format(field, "List"))
		elif fieldtype == "date":
			if not isinstance(value, basestring) and valid_date(value):
				raise Exception(err_msg.format(field, "Valid String Date"))

def is_valid_date(date):
	""" validate date format """
	return True
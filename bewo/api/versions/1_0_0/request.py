import json
import frappe
from schema.schema import get_request_schema

def validate_request(method, request):
	""" validate request schema """
	schema = get_request_schema(method)
	if not schema:
		raise Exception("Invalid Request : Schema Not Found")

	validate_request_schema(schema, "request_header", request)

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
		reqfieldtype = schema.get(field).get("reqfieldtype") or fieldtype
		parseType = schema.get(field).get("parseType")

		print field, fieldtype, reqfieldtype, parseType

		if reqfieldtype == "int":
			if not isinstance(value, int):
				raise Exception(err_msg.format(field, "Int"))
			if parseType:
				args.update({ field: parse_fieldtype(value, fieldtype)})
		elif reqfieldtype == "float":
			if not isinstance(value, float):
				raise Exception(err_msg.format(field, "Float"))
			if parseType:
				args.update({ field: parse_fieldtype(value, fieldtype)})
		elif reqfieldtype == "basestring":
			if not isinstance(value, basestring):
				raise Exception(err_msg.format(field, "String"))
			if parseType:
				args.update({ field: parse_fieldtype(value, fieldtype)})
		elif reqfieldtype == "list":
			if not isinstance(value, list):
				raise Exception(err_msg.format(field, "List"))
			if parseType:
				args.update({ field: parse_fieldtype(value, fieldtype)})
		elif reqfieldtype == "date":
			if not isinstance(value, basestring) and valid_date(value):
				raise Exception(err_msg.format(field, "Date"))
			if parseType:
				args.update({ field: parse_fieldtype(value, fieldtype)})

def is_valid_date(date):
	""" validate date format """
	return True

def parse_fieldtype(value, fieldtype):
	""" change the type to *fieldtype """
	try:
		if fieldtype == "int":
			return int(value)
		elif fieldtype == "float":
			return float(value)
		elif fieldtype == "basestring":
			return str(value)
		elif fieldtype == "list":
			raise Exception("Can't parse value to list type")
		elif fieldtype == "dict":
			return json.loads(value)
		elif fieldtype == "date":
			# to date object
			return value
	except Exception, e:
		raise e
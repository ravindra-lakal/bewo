# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import logging
import string
import datetime
import re
import json

from frappe.utils import getdate, flt,validate_email_add, cint
from frappe.model.naming import make_autoname
from frappe import throw, _, msgprint
import frappe.permissions
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

_logger = logging.getLogger(frappe.__name__)


@frappe.whitelist(allow_guest=True)
def update_price_list(self, method):
        # prices = ["MRP","Retail","Wholesale"]
        prices = {"MRP":"mrp","":"Retail Rate","":"Wholesale Rate"}

        prices = [{"price_list_name":"mrp","rate":self.mrp}, 
                {"price_list_name":"Retail","rate":self.retail_rate},
                {"price_list_name":"Wholesale","rate":self.wholesale_rate},
                {"price_list_name":"Purchase","rate":self.purchase_rate}]

        for i in prices:  
                if i["rate"]:
                        set_price_list(self,i["price_list_name"],i["rate"])

def set_price_list(self,price_list_name,rate):
        price_list = frappe.db.get_value("Price List",{"name":price_list_name},"name")
        if not price_list:
                price_list = frappe.new_doc("Price List")
                price_list.price_list_name = price_list_name
                price_list.currency = frappe.db.get_value("Company",
                        frappe.db.get_default("Company"), "default_currency", cache=True)
                if price_list_name == "Purchase":
                        price_list.buying = True
                else: 
                        price_list.selling = True
                price_list.save(ignore_permissions = True)
        item_price = frappe.db.get_value("Item Price", {"price_list": price_list_name,
                "item_code": self.item_code})
        if item_price:
                frappe.db.set_value("Item Price", item_price, "price_list_rate", rate)
        else:
                item_price = frappe.new_doc("Item Price")
                item_price.price_list = price_list_name
                item_price.item_code = self.item_code
                item_price.price_list_rate = rate
                item_price.save(ignore_permissions = True)

def new_item_group(self, category_name):
        group = frappe.db.get_value("Item Group",{"name":self.sub_category_name},"name")
        if not group:
                group = frappe.new_doc("Item Group")
                group.item_group_name = self.sub_category_name
                group.parent_item_group = "All Item Groups"
                group.is_group = "No"
                group.save(ignore_permissions = True)
                return "True"

@frappe.whitelist(allow_guest=True)
def get_total_item(customer):
        total_item = frappe.db.sql("""select count(name) from tabItem where ISNULL(variant_of)""",as_list=1,debug=1)
        abc = str(total_item[0][0])
        print abc
        return abc      

@frappe.whitelist(allow_guest=True)
def update_purchase_rate(self, method):
        print "Stock Entry Updated"
        for i in self.items:  
                print i.basic_rate
                purchase_rate = frappe.db.get_value("Item",{"name":i.item_code},"purchase_rate")
                print purchase_rate
                if not i.basic_rate:
                        i.basic_rate = purchase_rate;
        self.calculate_rate_and_amount()

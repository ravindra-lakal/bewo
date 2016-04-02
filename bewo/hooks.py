# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "bewo"
app_title = "BEWO"
app_publisher = "makarand.b@indictranstech.com"
app_description = "BEWO"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "makarand.b@indictranstech.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bewo/css/bewo.css"
# app_include_js = "/assets/bewo/js/bewo.js"

# include js, css files in header of web template
# web_include_css = "/assets/bewo/css/bewo.css"
# web_include_js = "/assets/bewo/js/bewo.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "bewo.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bewo.install.before_install"
# after_install = "bewo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bewo.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bewo.tasks.all"
# 	],
# 	"daily": [
# 		"bewo.tasks.daily"
# 	],
# 	"hourly": [
# 		"bewo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bewo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bewo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bewo.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bewo.event.get_events"
# }


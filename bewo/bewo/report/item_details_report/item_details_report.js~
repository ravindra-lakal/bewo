var abc = 0;
frappe.call({
		type: "GET",
		method: "bewo.custom_method.item_price.get_total_item",
		freeze: true,
		async:false,
		freeze_message: __("Loading"),
		args: {
			"customer": "abc"
		},
		callback: function(r) {
			abc = r.message;
			abc = "Total Item :  " + abc;
			console.log(r.message);
		}
	});
// msgprint(abc)
frappe.query_reports["Item Details Report"] = {
	"filters": [
		{
			"fieldname":"total_item",
			"label": __("Total Item"),
			"fieldtype": "Data",
			"width": "100",
			"default": abc,
		},
	],
}




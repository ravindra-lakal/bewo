//For Backup
// it will help if one can make mistake while exporting fixtures

// Dotype: Stock Entry

frappe.ui.form.on("Stock Entry", "custom_purpose", function(frm) {
	if(frm.doc.custom_purpose =="Inward"){
		frm.set_value("purpose", "Material Receipt");
	}
	else if(frm.doc.custom_purpose == "Outward"){
		frm.set_value("purpose", "Material Issue");
	}
	else if(frm.doc.custom_purpose == "Transfer"){
		frm.set_value("purpose", "Material Transfer");
	}
});

// Dotype: Item
frappe.ui.form.on("Item", "sub_category", function(frm) {
   frm.doc.item_group=frm.doc.sub_category;
});
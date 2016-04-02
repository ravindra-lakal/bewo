records = {
	"BST000210":{
		"inventory" : [
			{
				"strProductCode":"80829292029",
				"strProductName":"Pepsodent",
				"strBrand":"Pepsodent Brand",
				"strCompany" : "P&G",
				"strCategory": "Personal Care",
				"dblMRP":"60",
				"dblSellingPrice_Retail":"60",
				"dblSellingPrice_Wholesale":"60",
				"dblPurchasePrice":"60",
				"dblVAT":"14.5",
				"type":"sku",
				"staus":"Active"
			},
			{
				"strProductCode":"80829292030",
				"strProductName":"coalgate",
				"strBrand":"coalgate Brand",
				"strCompany" : "P&G",
				"strCategory": "Personal Care",
				"dblMRP":"70",
				"dblSellingPrice_Retail":"70",
				"dblSellingPrice_Wholesale":"70",
				"dblPurchasePrice":"70",
				"dblVAT":"14.5",
				"type":"sku",
				"staus":"Active"
			},
			{
				"strProductCode":"80829292031",
				"strProductName":"dabur",
				"strBrand":"dabur Brand",
				"strCompany" : "P&G",
				"strCategory": "Personal Care",
				"dblMRP":"60",
				"dblSellingPrice_Retail":"60",
				"dblSellingPrice_Wholesale":"60",
				"dblPurchasePrice":"60",
				"dblVAT":"14.5",
				"type":"sku",
				"staus":"Active"
			}
		],
		# "sales_order": [
		# 	{
		# 		"strBillnumber":"I0001",
		# 		"items":[
		# 			{
		# 				"strProductCode":"80829292029",
		# 				"dblMRP":"60",
		# 				"strQty":"2"
		# 			}
		# 		],
		# 		"date":"2015-02-01",
		# 	},
		# 	{
		# 		"strBillnumber":"I0002",
		# 		"items":[
		# 			{
		# 				"strProductCode":"80829292030",
		# 				"dblMRP":"70",
		# 				"strQty":"2"
		# 			},
		# 			{
		# 				"strProductCode":"80829292031",
		# 				"dblMRP":"60",
		# 				"strQty":"2"
		# 			}
		# 		],
		# 		"date":"2015-02-02",
		# 	},
		# ],
		# "sales_return":[
		# 	{
		# 		"strBillnumber":"I0001",
		# 		"items":[
		# 			{
		# 				"strProductCode":"80829292029",
		# 				"dblMRP":"60",
		# 				"strQty":"2"
		# 			}
		# 		],
		# 		"date":"2015-02-01",
		# 	}
		# ]
	}
}

index_mapping = {
	"inventory": "strProductCode",
	"sales_order": "strBillnumber",
	"sales_return": "strBillnumber"
}
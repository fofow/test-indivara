# __manifest__.py in custom_addons/inventory_api
{
    'name': 'API Product',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Test Indivara no 6',
    'description': '''Install Odoo Community on Local using 17 - Rest API Test'''
                   '''Please install New Odoo Community on Local using 17 - Then make API from custom module for inventory modules to get products '''
    '''Note: 
- Extra points 
  * Make validation if Rest API method HTTP is not GET - Response error HTTP code 405 error 
  METHOD : GET
URL : /get/products

{
    "data": [
        {
            "nama_produk": "10% on your order",
            "kategori": "All",
            "internal_reference": "1cf452256850",
            "sales_price": 0.0,
            "cost_price": 0.0
        },
    ]
}

'''

    ,
    'depends': ['base', 'product'],
    'data': [],
    'installable': True,
    'application': False,
}

from odoo import http
from odoo.http import request, Response
import json

class InventoryAPIController(http.Controller):



    @http.route('/get/products', type='http', auth='public', methods=['GET'])
    def get_products(self, **kwargs):
        if request.httprequest.method != 'GET':
            return Response("Method Not Allowed", status=405)

        products = request.env['product.product'].search([])
        data = []

        for product in products:
            data.append({
                'nama_produk': product.name,
                'kategori': product.categ_id.name if product.categ_id else '',
                'internal_reference': product.default_code or '',
                'sales_price': product.list_price,
                'cost_price': product.standard_price,
            })

        return request.make_response(
            headers={'Content-Type': 'application/json'},
            data=json.dumps({"data": data})
        )

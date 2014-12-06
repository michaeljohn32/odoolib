import connection
import odobject


odoo = odobject.OdooObject()
search_res = odoo.search('product.product',[], {'limit': 5})
print search_res
print odoo.search_count('product.product')
read_res = odoo.read('res.partner',search_res)#, {'fields': ['name', 'country_id', 'comment']})
#read_res = odoo.read('res.partner',search_res)
#print read_res
#attrs = odoo.field_attribs('res.partner', ['mobile','category_id'], ['string', 'type', 'help'])
#print attrs
#
#search_read_res = odoo.search_read('res.partner',[], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
#print search_read_res
#
#created_id = odoo.create('res.partner', {'name': 'Jacoby Wanna'})
#print created_id
#search_for_new_guy = odoo.search_read('res.partner',['id', '=', created_id])
#print search_for_new_guy
## now let's set his title
#sir = odoo.search('res.partner.title',['name','=','Mister'])
#print sir
#update_new_guy = odoo.update('res.partner',[created_id],{'street2': 'Terrrily Way', 'title': sir[0]})
#print update_new_guy
#search_read_res = odoo.search_read('res.partner',['id', '=', created_id], {'fields': ['name', 'street2','title'], 'limit': 5})
#print search_read_res
#
## delete the creation
#delete = odoo.delete('res.partner', [created_id])
#print delete
#search_read_res = odoo.search_read('res.partner',['id', '=', created_id], {'fields': ['name', 'street2','title'], 'limit': 5})
#print search_read_res
#
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

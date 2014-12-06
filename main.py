import connection
import odobject

# instantiate the odoo object
odoo = odobject.OdooObject()

# conn
conn = connection.Connection()
print 'Partner edits'
attrs = odoo.field_attribs('res.partner', ['mobile','category_id'], ['string', 'type', 'help'])
print attrs

search_read_res = odoo.search_read('res.partner',[], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print search_read_res

created_id = odoo.create('res.partner', {'name': 'Jacoby Wanna'})
print created_id

search_for_new_guy = odoo.search_read('res.partner',['id', '=', [created_id]], {'fields': ['name', 'country_id', 'title'], 'limit': 5})
print search_for_new_guy
# now let's set his title
sir = odoo.search('res.partner.title',['name','=','Mister'])
print "title search:" + str(sir)
update_new_guy = odoo.update('res.partner',[created_id],{'street2': 'Terrrily Way', 'title': sir[0]})
print update_new_guy
search_read_res = odoo.search_read('res.partner',['id', '=', created_id], {'fields': ['name', 'street2','title'], 'limit': 5})
print search_read_res

# delete the creation
delete = odoo.delete('res.partner', [created_id])
print 'is the id deleted?:' + str(delete)
search_read_res = odoo.search_read('res.partner',['id', '=', created_id], {'fields': ['name', 'street2','title'], 'limit': 5})
print search_read_res

print 'Product edits'

#search for all products, but limit the result to 5
search_res = odoo.search('product.product',['name','like','#DY14-814'], {'limit': 5})
print search_res
#count the number of products
print odoo.search_count('product.product')
#look at the products we got in the search above
read_res = odoo.read('product.product',search_res) #, {'fields': ['name','product_uom']})
print read_res

# product template
search_res = odoo.search('product.template',['name','like','#DY14-814'], {'limit': 5})
print search_res
read_res = odoo.read('product.template',search_res) #, {'fields': ['name','product_uom']})
print read_res
print conn.execute_const()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

from log import logger
import connection
class OdooObject():
    def __init__(self):
        self._conn = connection.Connection()
    def _encap_domain(self, domain):
        logger.debug('encap_domain length:' + str(len(domain)))
        logger.debug(domain)
        if(domain is not None):
            if(len(domain) >= 1):
                #enclose in a list of list
                domain = [[domain]]
            else:
                domain = [domain]
        return domain
    def search(self, model, domain=[], parameters = {}):
        domain = self._encap_domain(domain)
        return self._conn.execute(model, 'search', domain, parameters)
    def search_count(self, model, domain=[], parameters = {}):
        domain = self._encap_domain(domain)
        return self._conn.execute(model, 'search_count', domain, parameters)
    def read(self, model, domain=[], parameters = {}):
        return self._conn.execute(model, 'read', [domain], parameters)
    def search_read(self, model, domain=[], parameters = {}):
        # in my testing, without encapsin domain one more time, we get a ValueError: Invalid leaf in 'id'
        # where the domain initially passed is something like ['id','=',[2440]] 
        if(len(domain)>0):
            domain = self._encap_domain(domain)
        return self._conn.execute(model, 'search_read', domain, parameters)
    def field_attribs(self, model, fieldnames = [], attribute_names=['type', 'string']):
        ''' Gets the specified field's attributes
        '''
        try:
            _ = (check for check in fieldnames)
            fieldnames = [fieldnames]
        except TypeError:
            fieldnames = [[fieldnames]]
            
        return self._conn.execute(model, 'fields_get', fieldnames, {'attributes': attribute_names})

    def create(self, model, dict_to_create):
        '''while most value types are what would be expected 
        (integer for Integer, string for Char or Text),
            Date, Datetime and Binary fields use string values
            One2many and Many2many use a special command 
            protocol detailed in the documentation to the write method.
        see:
        https://www.odoo.com/documentation/8.0/reference/orm.html#openerp.models.Model.write
        '''
        return self._conn.execute(model, 'create', [dict_to_create])
    def update(self, model, ids_to_update, dict_of_updates):
        '''while most value types are what would be expected 
        (integer for Integer, string for Char or Text),
            Date, Datetime and Binary fields use string values
            One2many and Many2many use a special command 
            protocol detailed in the documentation to the write method.
        see:
        https://www.odoo.com/documentation/8.0/reference/orm.html#openerp.models.Model.write
        '''
        #ids_to_update = self._encap_domain(ids_to_update)
        return self._conn.execute(model, 'write', [ids_to_update, dict_of_updates])
    
    def delete(self, model, list_of_ids):
        return self._conn.execute(model, 'unlink', [list_of_ids])


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

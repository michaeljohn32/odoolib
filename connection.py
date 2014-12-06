import xmlrpclib
import config
class Connection():
    def __init__(self, root='http://localhost:8069', db = 'beta', user = 'admin', pwd= config.PASS):
        self._common =  str(root) + '/xmlrpc/2/common'
        self._object = str(root) + '/xmlrpc/2/object'
        self._db = db
        self._user = user
        self._pwd = pwd
        # get the userid
        self._uid = xmlrpclib.ServerProxy(self._common).login(db, user, pwd)
        # get the model
        self._model = xmlrpclib.ServerProxy(self._object) 
        self.uid = self._getuid()
        print 'Logged in as %s (uid: %d)' % (user, self._uid)
    #Get methods
    def _getuid(self):
        return self._uid
    
    def execute(self, model_name, method_name, parameters_list = [[]], parameters_dict = {}):
        res = self._model.execute_kw(self._db, self.uid, self._pwd, model_name, method_name, parameters_list, parameters_dict)
#        res = self._model.execute_kw(self._db, self._uid, self._pwd, 'res.partner', 'fields_get',[], {'attributes': ['string', 'help', 'type']})
        return res
        
    def getuids(self):
        # get all the userids
        server = xmlrpclib.ServerProxy(self._object)
        user_ids = server.execute(
            self._db, 
            self._uid, 
            self._pwd, 
            'res.users', 
            'search',
            []
        )
        print user_ids

        users = server.execute(
            self._db, 
            self._uid, 
            self._pwd, 
            'res.users',
            'read',
            user_ids,
            []
        )
        print users




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

import xmlrpclib
import config
from log import logger
class Connection():
    def __init__(self, root='http://localhost:8070', db = 'beta', user = 'admin', pwd= config.PASS):
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
        logger.debug('Logged in as %s (uid: %d)' % (user, self._uid))
    #Get methods
    def _getuid(self):
        return self._uid
    
    def execute(self, model_name, method_name, parameters_list = [[]], parameters_dict = {}):
        # I use the # print statement for testing
        logger.debug( 'res = self._model.execute_kw(self._db,self.uid, self._pwd,"' + model_name +'","' + method_name + '",' + str(parameters_list) + ',' + str(parameters_dict) + ')')
        res = self._model.execute_kw(self._db, self.uid, self._pwd, model_name, method_name, parameters_list, parameters_dict)
        return res
    def execute_const(self):
        '''Use this to test against execute statement'''
        res = self._model.execute_kw(self._db,self.uid, self._pwd,"product.product","search",[[['name', 'like', 'DY14-814']]],{'limit': 5})
        return res           



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

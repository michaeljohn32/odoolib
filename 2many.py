#
#   Commands for manipulating one2many and many2many fields
#
from log import logger
def add_new(values_dict)
    '''This method returns the correct command format
    to add a new row to the set
    with information provided from the values_dict
    @params: 
        values_dict - a dictionary of values to write
    @returns: 
        command triplet '''
    return (0,0,values_dict)
def update(update_id, values_dict)
    '''This method returns the correct command format
    to update an already existing row in a set
     with information provided from the values_dict
    NOTE: doesn't work in a create() method
    @params:   
        update_id - the id of the record to update
        values_dict - dictionary of values to update
    @returns:
        command triplet

    '''
    return (1, update_id,values_dict)
def remove_and_delete(delete_id)
    '''This method returns the correct command format
    to delete a row from both the field in question
    and permanently remove it from the database 
    NOTE: doesn't work in a create() method
    @params:   
        delete_id - the id of the record to remove
    @returns:
        command triplet

    '''
    return (2,delete_id,0)
def unlink(unlink_id)
    '''This method returns the correct command format
    to unlink a row from the field in question,
    but does NOT permanently remove it from the database 
    NOTE: doesn't work on one2many or in a create() method
    @params:   
        unlink_id - the id of the record to remove
    @returns:
        command triplet

    '''
    return (3, unlink_id,0)
def link(link_id)
    '''This method returns the correct command format
    to link an already existing id
    NOTE: doesn't work on one2many fields
    @params:   
        link_id - the id of the record to link
    @returns:
        command triplet

    '''
    return (4, link_id, 0)
def remove_all()
    '''This method returns the correct command format
    to remove all records from a set
    NOTE: doesn't work on one2many fields and doesn't
    work with create() method
    @params:   
    @returns:
        command triplet

    '''
    return (5, 0, 0)
def replace_all(ids_list)
    '''This method returns the correct command format
    to replace all records in a set with the ids
    in ids_list
    NOTE: doesn't work on one2many fields
    @params:   
        ids_list - the list of ids to replace it with
    @returns:
        command triplet
    '''
    return (6, 0, ids_list)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

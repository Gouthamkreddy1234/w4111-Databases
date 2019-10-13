import pymysql
import src.data_service.dbutils as dbutils
import src.data_service.RDBDataTable as RDBDataTable

# The REST application server app.py will be handling multiple requests over a long period of time.
# It is inefficient to create an instance of RDBDataTable for each request.  This is a cache of created
# instances.
_db_tables = {}

def get_rdb_table(table_name, db_name, key_columns=None, connect_info=None):
    """

    :param table_name: Name of the database table.
    :param db_name: Schema/database name.
    :param key_columns: This is a trap. Just use None.
    :param connect_info: You can specify if you have some special connection, but it is
        OK to just use the default connection.
    :return:
    """
    global _db_tables

    # We use the fully qualified table name as the key into the cache, e.g. lahman2019clean.people.
    key = db_name + "." + table_name

    # Have we already created and cache the data table?
    result = _db_tables.get(key, None)

    # We have not yet accessed this table.
    if result is None:

        # Make an RDBDataTable for this database table.
        result = RDBDataTable.RDBDataTable(table_name, db_name, key_columns, connect_info)

        # Add to the cache.
        _db_tables[key] = result

    return result


#########################################
#
#
# YOU HAVE TO IMPLEMENT THE FUNCTIONS BELOW.
#
#
# -- TO IMPLEMENT --
#########################################

def get_databases(): #already given
    """

    :return: A list of databases/schema at this endpoint.
    """

    # -- TO IMPLEMENT --
    conn = connect()
    res = dbutils.run_q("SHOW DATABASES", conn=conn)
    return res

    pass

def get_db_tables(): #first function added by me
    """

    :return: A list of databases/schema at this endpoint.
    """

    # -- TO IMPLEMENT --
    conn = connect()
    res = dbutils.run_q("show tables", conn=conn)
    return res

    pass

def select(dbname, resource, keys, fields=None):
    print(resource,dbname)
    rdb_obj = get_rdb_table(resource, dbname)

    res = rdb_obj.find_by_primary_key(keys, fields)
    print("goutham="+str(res))
    return  res


def insert(dbname, resource, keys, otherfields=None):
    print(resource,dbname)
    rdb_obj = get_rdb_table(resource, dbname)

    dict = {}
    print(len(keys),len(rdb_obj._key_columns))
    for i in range(0, len(rdb_obj._key_columns)) :
        dict.update({rdb_obj._key_columns[i]:keys[i]})

    if otherfields is not None:
        for k,v in otherfields.items():
            dict.update({k:v})

    res = rdb_obj.insert(dict)
    #print("goutham="+res)
    return  res


def delete(dbname, resource, keys):
    print(resource,dbname)
    rdb_obj = get_rdb_table(resource, dbname)

    res = rdb_obj.delete_by_key(keys)
    #print("goutham="+res)
    return  res


def select_by_temp(dbname, resource, template, field_list=None):
    print(resource,dbname)
    rdb_obj = get_rdb_table(resource, dbname)

    res = rdb_obj.find_by_template(template, field_list=field_list)
    print("goutham="+str(res))
    return  res



def insert_post(dbname, resource, post_args):
    print(resource,dbname)
    rdb_obj = get_rdb_table(resource, dbname)

    res = rdb_obj.insert(post_args)
    #print("goutham="+res)
    return  res



def connect():
    _default_connect_info = {
        'host': 'localhost',
        'user': 'root',
        'password': 'dbuserdbuser',
        'db': 'lahman2019clean',
        'port': 3306
    }
    conn = pymysql.connect(
            host=_default_connect_info['host'],
            user=_default_connect_info['user'],
            password=_default_connect_info['password'],
            db=_default_connect_info['db'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    return conn





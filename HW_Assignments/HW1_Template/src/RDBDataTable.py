#from BaseDataTable import BaseDataTable
from HW_Assignments.HW1_Template.src.BaseDataTable import BaseDataTable
import pymysql

import logging
logger = logging.getLogger()

class RDBDataTable(BaseDataTable):

    """
    The implementation classes (XXXDataTable) for CSV database, relational, etc. with extend the
    base class and implement the abstract methods.
    """

    def __init__(self, table_name, connect_info, key_columns):
        """

        :param table_name: Logical name of the table.
        :param connect_info: Dictionary of parameters necessary to connect to the data.
        :param key_columns: List, in order, of the columns (fields) that comprise the primary key.
        """
        self._data = {
        "table_name" : table_name,
        "connect_info" : connect_info,
        "key_columns" : key_columns,
        }
        #key columns - list of fields in the order in which they they form the primary key (composite/compound)

        self.conn = pymysql.connect(host=connect_info['host'], user=connect_info['user'], password=connect_info['password'], db=connect_info['db'], cursorclass=pymysql.cursors.DictCursor)
        print(self.conn)#defining inside init
        self.conn.autocommit(False)


        pass

    def find_by_primary_key(self, key_fields, field_list=None):#we have a return here, cant return the query here
        """

        :param key_fields: The list with the values for the key_columns, in order, to use to find a record.
        :param field_list: A subset of the fields of the record to return.
        :return: None, or a dictionary containing the requested fields for the record identified
            by the key.
        """

        #get list of fields from the key_columns
        length = len(key_fields)
        list = []
        #make a where_list - [ a,b,c ]

        if len(key_fields) != len(self._data.get("key_columns")):
            raise ValueError("FIND_BY_PRIMARY_KEY FAILED: Number of fields in key_fields does not match the number of fields in key_columns")

        for i in range (0, length):
            list.append(str(self._data.get("key_columns")[i]+"="+"'"+key_fields[i]+"'"))#key_fields has the actual value

        w_clause = " and ".join(list)

        if field_list is None:
            l_f = " * "
        else:
            l_f = " " + ",".join(field_list) + " "

        query = "select"+l_f+"from "+self._data.get("table_name")+" where "+ w_clause
        print(query)
        #make the query here and return the result
        try:
            res, data = self.run_q(query)
            return (res, data)
        except Exception as e:
            return (0,"Error"+str(e))
        pass

    def find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None):
        """

        :param template: A dictionary of the form { "field1" : value1, "field2": value2, ...}
        :param field_list: A list of request fields of the form, ['fielda', 'fieldb', ...]
        :param limit: Do not worry about this for now.
        :param offset: Do not worry about this for now.
        :param order_by: Do not worry about this for now.
        :return: A list containing dictionaries. A dictionary is in the list representing each record
            that matches the template. The dictionary only contains the requested fields.
        """
        #simpler, delete all rows that match the template
        # made a find_list
        if field_list is None:
            l_f = " * "
        else:
            l_f = " " + ",".join(field_list) + " "

        list = []
        for k,v in template.items():
            list.append(str(k+"="+"'"+v+"'"))

        w_clause = " and ".join(list)

        query = "select"+l_f+"from "+self._data.get("table_name")+" where "+w_clause
        print(query)
        try:
            res, data = self.run_q(query)
            return (res, data)
        except Exception as e:
            return (0,"Error"+str(e))
        pass

    def delete_by_key(self, key_fields):#key_fields has only the values corresponding to the primary_key
        """

        Deletes the record that matches the key.

        :param key_fields: A template.
        :return: A count of the rows deleted.
        """
        if key_fields is None:
            raise ValueError('DELETE_BY_KEY FAILED: key_fields param cannot be None')

        key_col = self._data.get("key_columns", None)
        if(len(key_col) != len(key_fields)):
            raise ValueError('DELETE_BY_KEY FAILED: length(key_fields) != length(key_columns')

        # get list of fields from the key_columns
        length = len(key_fields)
        list = []
        # make a where_list - [ a,b,c ]
        for i in range(0, length):
            list.append(str(self._data.get("key_columns")[i] + "=" + "'" + key_fields[i] + "'"))  # key_fields has the actual value

        w_clause = " and ".join(list)

        query = "delete from " + self._data.get("table_name") + " where " + w_clause
        print(query)
        try:
            res, data = self.run_q(query)
            return (res, data)
        except Exception as e:
            return (0,"Error"+str(e))
        pass

    def delete_by_template(self, template):
        """

        :param template: Template to determine rows to delete.
        :return: Number of rows deleted.
        """
        if(template is None):
            raise ValueError('UPDATE_BY_TEMPLATE FAILED: template param cannot be None')

        list = []
        for k, v in template.items():
            list.append(str(k + "=" + "'" + v + "'"))

        w_clause = " and ".join(list)

        query = "delete from " + self._data.get("table_name")+ " where " + w_clause
        #run the query using the run_q and either print the result(data, rows) or the exception that is returned by the run_q
        print(query)

        try:
            res, data = self.run_q(query)
            return (res, data)
        except Exception as e:
            return (0,"Error"+str(e))
        pass

    def update_by_key(self, key_fields, new_values):
        """

        :param key_fields: List of value for the key fields.
        :param new_values: A dict of field:value to set for updated row.
        :return: Number of rows updated.
        """
        # Need not implement update_by_key

    def update_by_template(self, template, new_values):
        """

        :param template: Template for rows to match.
        :param new_values: New values to set for matching fields.
        :return: Number of rows updated.
        """
        if template is None:
            raise ValueError('UPDATE_BY_TEMPLATE FAILED: template param cannot be empty')

        if new_values is None:
            raise ValueError('UPDATE_BY_TEMPLATE FAILED: new_values param cannot be empty')

        list = []
        for k, v in template.items():
            list.append(str(k + "=" + "'" + v + "'"))

        w_clause = " and ".join(list)

        list_new_val = []
        for k, v in new_values.items():
            list_new_val.append(str(k + "=" + "'" + v + "'"))

        new_val_set = " , ".join(list_new_val)

        query = "update " + self._data.get("table_name")+ " set " + new_val_set + " where " + w_clause
        print(query)#run_q returns the number of rows updated
        try:
            res, data = self.run_q(query)
            return (res, data)
        except Exception as e:
            return (0,"Error"+str(e))
        pass

    def insert(self, new_record):
        """

        :param new_record: A dictionary representing a row to add to the set of records.
        :return: None
        """
        if new_record is None:
            raise ValueError("INSERT FAILED: Cannot pass an empty record")

        col = []
        val = []
        for k, v in new_record.items():
            col.append(k)
            val.append("'"+v+"'")

        cols = ','.join(col)
        vals = ','.join(val)

        query = "insert into " + self._data.get("table_name") + " (" + cols + ") " + "values" + " (" + vals + ")"
        #run the query - Capture either the result(data,rows) or an exception returned by the run_q
        print(query)
        try:
            res, data = self.run_q(query)
            return (res, data)
        except Exception as e:
            return (0,"Error"+str(e))
        pass

    def get_rows(self):
        return self._rows

    def run_q(self, sql, args=None, fetch=True, cur=None, conn=None, commit=True):
        '''
        Helper function to run an SQL statement.

        :param sql: SQL template with placeholders for parameters.
        :param args: Values to pass with statement.
        :param fetch: Execute a fetch and return data.
        :param conn: The database connection to use. The function will use the default if None.
        :param cur: The cursor to use. This is wizard stuff. Do not worry about it for now.
        :param commit: This is wizard stuff. Do not worry about it.

        :return: A tuple of the form (execute response, fetched data)
        '''

        cursor_created = False
        connection_created = False

        try:

            if conn is None:
                connection_created = True
                conn = self._get_default_connection()

            if cur is None:
                cursor_created = True
                cur = conn.cursor()

            if args is not None:
                log_message = cur.mogrify(sql, args)
            else:
                log_message = sql

            logger.debug("Executing SQL = " + log_message)

            res = cur.execute(sql, args)

            if fetch:
                data = cur.fetchall()
            else:
                data = None

            # Do not ask.
            if commit == True:
                conn.commit()

        except Exception as e:
            raise (e)

        return (res, data)

    def _get_default_connection(self):
        conn = pymysql.connect(host='localhost',
                                 user='dbuser',
                                 password='dbuserdbuser',
                                 db='lahman2019raw',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        return conn
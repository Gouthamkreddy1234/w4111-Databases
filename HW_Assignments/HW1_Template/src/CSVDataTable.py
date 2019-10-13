
from HW_Assignments.HW1_Template.src.BaseDataTable import BaseDataTable
import copy
import csv
import logging
import json
import os
import pandas as pd

pd.set_option("display.width", 256)
pd.set_option('display.max_columns', 20)

class CSVDataTable(BaseDataTable):
    """
    The implementation classes (XXXDataTable) for CSV database, relational, etc. with extend the
    base class and implement the abstract methods.
    """

    _rows_to_print = 10
    _no_of_separators = 2

    def __init__(self, table_name, connect_info, key_columns, debug=True, load=True, rows=None):
        """

        :param table_name: Logical name of the table.
        :param connect_info: Dictionary of parameters necessary to connect to the data.
        :param key_columns: List, in order, of the columns (fields) that comprise the primary key.
        """

        self._data = {
            "table_name": table_name,
            "connect_info": connect_info,
            "key_columns": key_columns,
            "debug": debug
        }

        self._logger = logging.getLogger()

        self._logger.debug("CSVDataTable.__init__: data = " + json.dumps(self._data, indent=2))

        if rows is not None:
            self._rows = copy.copy(rows)
        else:
            self._rows = []
            self._load()#loading the csv file here

    def __str__(self):

        result = "CSVDataTable: config data = \n" + json.dumps(self._data, indent=2)

        no_rows = len(self._rows)
        if no_rows <= CSVDataTable._rows_to_print:
            rows_to_print = self._rows[0:no_rows]
        else:
            temp_r = int(CSVDataTable._rows_to_print / 2)
            rows_to_print = self._rows[0:temp_r]
            keys = self._rows[0].keys()

            for i in range(0,CSVDataTable._no_of_separators):
                tmp_row = {}
                for k in keys:
                    tmp_row[k] = "***"
                rows_to_print.append(tmp_row)

            rows_to_print.extend(self._rows[int(-1*temp_r)-1:-1])

        df = pd.DataFrame(rows_to_print)
        result += "\nSome Rows: = \n" + str(df)

        return result

    def _add_row(self, r):
        if self._rows is None:
            self._rows = []
        self._rows.append(r)

    def _load(self):

        dir_info = self._data["connect_info"].get("directory")
        file_n = self._data["connect_info"].get("file_name")
        full_name = os.path.join(dir_info, file_n)

        with open(full_name, "r") as txt_file:
            csv_d_rdr = csv.DictReader(txt_file)
            headers = csv_d_rdr.fieldnames
            print("HEADERS= "+ str(headers))
            self._data.update({"columns":headers})
            for r in csv_d_rdr:
                self._add_row(r)
        self._logger.debug("CSVDataTable._load: Loaded " + str(len(self._rows)) + " rows")

    def save(self):
        """
        Write the information back to a file.
        :return: None
        """
        dir_info = self._data["connect_info"].get("directory")
        file_n = self._data["connect_info"].get("file_name")
        full_name = os.path.join(dir_info, file_n)

        with open(full_name, "wb") as txt_file:
            writer = csv.DictWriter(txt_file, self._data.get("columns"))
            for row in self._rows:
                #if not stringNeed.isdigit():
                #   rows['zip'] = "not number"
                # even more stuff to check and edit here
                # write the edited row
                writer.writerow(row)

    @staticmethod
    def matches_template(row, template):

        result = True
        if template is not None:
            for k, v in template.items():
                if v != row.get(k, None):
                    result = False
                    break

        return result

    def find_by_primary_key(self, key_fields, field_list=None):
        """

        :param key_fields: The list with the values for the key_columns, in order, to use to find a record.
        :param field_list: A subset of the fields of the record to return.
        :return: None, or a dictionary containing the requested fields for the record identified
            by the key.
        """
        #implement this next - once done, finish update, delete and insert

        if field_list is not None:
            if not set(field_list).issubset(self._data.get("columns", None)):
                raise ValueError('FIND_BY_PRIMARY_KEY FAILED: Incorrect column names mentioned in field_list')

        if len(key_fields) != len(self._data.get("key_columns")):
            raise ValueError("FIND_BY_PRIMARY_KEY FAILED: number of fields in key_fields does not match the number of fields in key_columns")

        d={}
        for r in self._rows:
            i=0
            flag = True
            for field in self._data.get("key_columns"):
                if(r[field] != key_fields[i]):
                    flag = False
                    break
                else:
                    i = i+1
            if(flag):
                if field_list is not None:
                    for f in field_list:
                        if not r[f] is None:
                            d.update({f:r[f]})
                        else:
                            d.update({f:""})
                else:
                    d = r

        return d
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
        #should the template contain all the fields? - implement this now

        if template is None:
            raise ValueError("FIND_BY_TEMPLATE FAILED: Template cannot be None")

        template_keys = set(template.keys())
        if not template_keys.issubset(self._data.get("columns", None)):
            raise ValueError('FIND_BY_TEMPLATE FAILED: Incorrect column names mentioned in template')

        if field_list is not None:
            if not set(field_list).issubset(self._data.get("columns", None)):
                raise ValueError('FIND_BY_TEMPLATE FAILED: Incorrect column names mentioned in field_list')

        l=[]
        for r in self._rows:
            flag = True
            for field, value in template.items():
                if(template[field] != r[field]):
                    flag = False
            if(flag):
                d = {}
                if field_list is not None:
                    for f in field_list:
                        d.update({f:r[f]})#perfect
                    l.append(d)
                else:
                    l.append(r)
        print(l)
        print(len(l))
        return l #list containing dicts
        pass

    def delete_by_key(self, key_fields):
        """

        Deletes the record that matches the key.

        :param template: A template.
        :return: A count of the rows deleted.
        """
        if key_fields is None:
            raise ValueError('DELETE_BY_KEY FAILED: key_fields param cannot be None')

        key_col = self._data.get("key_columns", None)
        if len(key_col) != len(key_fields):
            raise ValueError('DELETE_BY_KEY FAILED: length(key_fields) != length(key_columns')

        delete_list = []
        for r in self._rows:
            i=0
            flag = True
            for field in self._data.get("key_columns"):
                if(r[field] != key_fields[i]):
                    flag = False
                    break
                else:
                    i = i+1
            if(flag):
                print(r)
                delete_list.append(r)
                self._rows.remove(r)  #delete the row from the loaded csv. overwrite the old csv now?
                print("This row has been deleted by key")

        return len(delete_list)
        pass

    def delete_by_template(self, template):
        """

        :param template: Template to determine rows to delete.
        :return: Number of rows deleted.
        """
        if(template is None):
            raise ValueError('DELETE_BY_TEMPLATE FAILED: template param cannot be empty')

        template_keys = set(template.keys())
        if not template_keys.issubset(self._data.get("columns", None)):
            raise ValueError('DELETE_BY_TEMPLATE FAILED: Incorrect column names mentioned in template')

        delete_list = []
        for r in self._rows:
            flag = True
            for field, value in template.items():
                if(template[field] != r[field]):
                    flag = False
            if(flag):
                print(r)
                delete_list.append(r)
                # self._rows.remove(r)  #delete the row from the loaded csv. overwrite the old csv now?
                print("This row has been deleted by template")

        return len(delete_list)
        pass

    def update_by_key(self, key_fields, new_values):
        """

        :param key_fields: List of value for the key fields.
        :param new_values: A dict of field:value to set for updated row.
        :return: Number of rows updated.
        """
        #Need not implement update_by key

    def update_by_template(self, template, new_values):
        """
         Yes, it is a batch update across multiple rows
        :param template: Template for rows to match.
        :param new_values: New values to set for matching fields. -> dict -> {a:b}
        :return: Number of rows updated.
        """
        if template is None:
            raise ValueError("UPDATE_BY_TEMPLATE FAILED: You have passed a NULL template | Template must have atleast one key-value pair")

        if new_values is None:
            raise ValueError("UPDATE_BY_TEMPLATE FAILED: You have passed a NULL new_values dict")

        template_keys = set(template.keys())
        if not template_keys.issubset(self._data.get("columns", None)):
            raise ValueError('UPDATE_BY_TEMPLATE FAILED: Incorrect column names mentioned in template')

        new_val_k = set(new_values.keys())
        if not new_val_k.issubset(self._data.get("columns", None)):
            raise ValueError('UPDATE_BY_TEMPLATE FAILED: Incorrect column names mentioned in new_values')

        #get all the values that you are updating - this is the new values dict
        new_values_keys = set(new_values.keys())
        if set(self._data.get("key_columns", None)).issubset(new_values_keys):
            key_dict = {} #a subset of the new_values containing only the key pairs - template
            for key in self._data.get("key_columns", None):
                key_dict.update({key:"'"+new_values[key]+"'"})
            if len(self.find_by_template(key_dict)) > 0:
                raise ValueError("UPDATE_BY_TEMPLATE FAILED: Voilating the primary key property since a row with these key values already exists in the CSV")


        update_list = []
        for r in self._rows:
            flag = True
            for field, value in template.items():
                if (template[field] != r[field]):
                    flag = False
            if (flag):
                print(r)
                for k,v in new_values.items():
                    r[k] = v
                update_list.append(r)
                print("after="+str(r))
                print("This row was updated by template")

        return len(update_list)
        pass

    def insert(self, new_record):
        """

        :param new_record: A dictionary representing a row to add to the set of records.
        :return: None
        """

        new_cols = set(new_record.keys())
        tbl_cols = set(self._data['columns'])

        if new_record is None:
            raise ValueError("INSERT FAILED: The new_record you passes is an empty dictionary")

        if not new_cols.issubset(tbl_cols):
            raise ValueError("INSERT FAILED: new_record contains invalid fields")

        key_cols = self._data.get("key_columns", None)

        if key_cols is not None:
            key_cols_set = set(key_cols) #convert from list to set
            if not key_cols_set.issubset(new_cols):
                raise ValueError("INSERT FAILED: Key_Column fields not passed for insert ")

        for k in key_cols:
            if new_record.get(k, None) is None:
                raise ValueError("INSERT FAILED: you need to have a value in the Key_Columns")

        new_key_dict ={} #create a dict containg only key_columns:value pairs in it - template
        for col in new_record.keys():
            if col in key_cols:
                new_key_dict.update({col:new_record[col]})

        #check for conflicting row
        if(len(self.find_by_template(new_key_dict)) > 0):
            raise ValueError("INSERT FAILED: row with these key_values exists | Violating the primary_key constraint")

        self._add_row(new_record)
        #self.save()
        return "Insert was successfull"
        pass

    def get_rows(self):
        return self._rows


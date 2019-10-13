# W4111_F19_HW1
Implementation template for homework 1.


The following functions have been defined in both CSVDataTable and RDBDataTable -

    def find_by_primary_key(self, key_fields, field_list=None):
    def find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None):
    def delete_by_key(self, key_fields):
    def delete_by_template(self, template):
    def update_by_template(self, template, new_values):
    def insert(self, new_record):

    These functions work for all the three tables (whether a simple key or a composite/compund key is used)

For the CSVDataTable, the relational constraints work for the below reasons -

    1)insert - Searches if the contains a row with the same primary_key values exists and throws an error if yes
    2)update_by_template - Searches if the table contains a row with the same values as the primary key and throws an error if yes
    3)find_by_primary_key - Gets the value for the key_field and searches for the corresponding row (key can be composite as well, we loop over all the values in the key_fields)
    4)find_by_template - Get the template and searches for the corresponding rows matching it
    5)delete_by_key - Deletes the rows matching the key_fields (since the CSV also has unique values based on primary key by default)
    6)delete_by_template - Deletes the rows by matching the template

The csv_table_tests has 16 test functions -
The purpose of each test function is defined in the first few lines of the function and whether it is for a working/error scenario -

    CSV_find_by_key_case_1()
    CSV_find_by_key_case_2()
    CSV_find_by_key_case_3()
    CSV_find_by_template_case_1()
    CSV_find_by_template_case_2()
    CSV_find_by_template_case_3()
    CSV_delete_by_key_case_1()
    CSV_delete_by_key_case_2()
    CSV_delete_by_key_case_3()
    CSV_delete_by_template_case_1()
    CSV_delete_by_template_case_2()
    CSV_insert_case_1()
    CSV_insert_case_2()
    CSV_insert_case_3()
    CSV_update_by_template_case_1()
    CSV_update_by_template_case_2()


The rdb_table_tests also has 16 test functions -
The purpose of each test function is defined in the first few lines of the function and whether it is for a working/error scenario -

    RDB_find_by_key_case_1()
    RDB_find_by_key_case_2()
    RDB_find_by_key_case_3()
    RDB_find_by_template_case_1()
    RDB_find_by_template_case_2()
    RDB_find_by_template_case_3()
    RDB_delete_by_key_case_1()
    RDB_delete_by_key_case_2()
    RDB_delete_by_key_case_3()
    RDB_delete_by_template_case_1()
    RDB_delete_by_template_case_2()
    RDB_insert_case_1()
    RDB_insert_case_2()
    RDB_insert_case_3()
    RDB_update_by_template_case_1()
    RDB_update_by_template_case_2()

The output of the tester files is logged in the csv_table_test and rdb_table_test for csv_table_tests and rdb_table_tests respectively.


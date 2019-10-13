#all test cases to test every edge case for the rdb file
from HW_Assignments.HW1_Template.src.RDBDataTable import *

def RDB_find_by_key_case_1(): #IMP
    print("RDB::FIND_BY_PRIMARY_KEY CASE 1 -----> WORKING CASE")
    # find by key
    # define conn params
    # create an RDB object
    # run a find on a particular row, by key

    connect_info = {
                    'host': 'localhost',
                    'user': 'dbuser',
                    'password': 'dbuserdbuser',
                    'db': 'lahman2019raw',
                    'charset': 'utf8mb4'
                    }
    rdb_people_1 = RDBDataTable('Batting', connect_info, ['playerID','teamID','yearID','stint'])#playerID alone is the key for player table
    r, d = rdb_people_1.find_by_primary_key(['aardsda01','SFN', '2004','1'], ["G", "AB", "R"])  # key_fields and field_list
    print(r, d)
    print("\n")


def RDB_find_by_key_case_2(): #IMP
    print("RDB::FIND_BY_PRIMARY_KEY CASE 2 -----> Wrong field name in fields_list")
    # find by key
    # define conn params
    # create an RDB object
    # run a find on a particular row, by key

    connect_info = {
                    'host': 'localhost',
                    'user': 'dbuser',
                    'password': 'dbuserdbuser',
                    'db': 'lahman2019raw',
                    'charset': 'utf8mb4'
                    }
    rdb_people_1 = RDBDataTable('people', connect_info, ['playerID'])#playerID alone is the key for player table
    r, d = rdb_people_1.find_by_primary_key(['aardsda01'], ["bats1", "height", "weight"])  # key_fields and field_list
    print(r, d)
    print("\n")

def RDB_find_by_key_case_3(): #IMP
    print("RDB::FIND_BY_PRIMARY_KEY CASE 3 -----> Wrong number of fields in key_fields")
    # find by key
    # define conn params
    # create an RDB object
    # run a find on a particular row, by key

    connect_info = {
                    'host': 'localhost',
                    'user': 'dbuser',
                    'password': 'dbuserdbuser',
                    'db': 'lahman2019raw',
                    'charset': 'utf8mb4'
                    }
    rdb_people_1 = RDBDataTable('people', connect_info, ['playerID'])#playerID alone is the key for player table
    try:
        r, d = rdb_people_1.find_by_primary_key(['aardsda01','sdsd'], ["bats1", "height", "weight"])  # key_fields and field_list
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")


def RDB_find_by_template_case_1(): #IMP
    print("RDB::FIND_BY_TEMPLATE CASE 1 -----> WORKING CASE")
    # find by template
    # define conn params
    # create an RDB object
    # run a find on a particular row, by template - log

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    r, d = rdb_people_2.find_by_template({'bats': 'R', 'height': '75', 'weight': '215'}, ['playerID', 'birthYear'])
    print(r, d)
    print("\n")

def RDB_find_by_template_case_2(): #IMP
    print("RDB::FIND_BY_TEMPLATE CASE 2 -----> Wrong field name in template")
    # find by template
    # define conn params
    # create an RDB object
    # run a find on a particular row, by template

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    r, d = rdb_people_2.find_by_template({'bats1': 'R', 'height': '75', 'weight': '215'}, ['playerID', 'birthYear'])
    print(r, d)
    print("\n")

def RDB_find_by_template_case_3(): #IMP
    print("RDB::FIND_BY_TEMPLATE CASE 3 ----->Wrong field name in fields_list")
    # find by template
    # define conn params
    # create an RDB object
    # run a find on a particular row, by template

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    r, d = rdb_people_2.find_by_template({'bats': 'R', 'height': '75', 'weight': '215'}, ['player2', 'birthYear'])
    print(r, d)
    print("\n")

def RDB_delete_by_key_case_1(): #IMP
    print("RDB::DELETE_BY_KEY CASE 1 -----> WORKING CASE")
    # del by key
    # define conn params
    # create an RDB object
    # run a find on a particular row, by template - log
    # perform an update - log
    # run a find, by template - log
    # the result would have different data when compared to the first find

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r, d = rdb_people_2.find_by_primary_key(['abbeybe01'])  #find
        print(r, d)
        r,d = rdb_people_2.delete_by_key(['abbeybe01']) #delete
        print(r,d)
        r, d = rdb_people_2.find_by_primary_key(['abbeybe01'])  #find_again
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_delete_by_key_case_2(): #IMP
    print("RDB::DELETE_BY_KEY CASE 2 -----> Wrong number of fields in key_fields")
    # delete by key
    # find by template
    # define conn params
    # create an RDB object
    # run a delete by key

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r,d = rdb_people_2.delete_by_key(['aardsda01',"asds"]) #key_fields
        print(r,d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_delete_by_key_case_3(): #IMP
    print("RDB::DELETE_BY_KEY CASE 3 -----> Key_fields is empty and wrong number of fields in key_fields")
    # del by Key
    # define conn params
    # create an RDB object
    # run a delete by key

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r,d = rdb_people_2.delete_by_key([]) #key_fields
        print(r,d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_delete_by_template_case_1(): #NON-error case
    print("RDB::DELETE_BY_TEMPLATE CASE 1 -----> WORKING CASE")
    # del by tem
    # define conn params
    # create an RDB object
    # run a find on a particular row, by template - log
    # perform an delete - log
    # run a find, by template - log
    # the result would have different data when compared to the first find

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r, d = rdb_people_2.find_by_template({"birthYear": "1869", "birthMonth": "11"}, {'birthYear', 'birthMonth'})  # template
        print(r, d)
        r, d = rdb_people_2.delete_by_template({"birthYear": "1869", "birthMonth": "11"})  # template
        print(r, d)
        r, d = rdb_people_2.find_by_template({"birthYear": "1869", "birthMonth": "11"}, {'birthYear', 'birthMonth'})  # template
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_delete_by_template_case_2(): #IMP
    print("RDB::DELETE_BY_TEMPLATE CASE 2 -----> Wrong field name in template")
    # del by tem
    # define conn params
    # create an RDB object
    # run a delete by template

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r, d = rdb_people_2.delete_by_template({"birthYear": "1981", "birthMo": "12"})  # template
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_insert_case_1(): #IMP
    print("RDB::INSERT CASE 1 -----> Voilates the primary key constraint")
    # del by tem
    # define conn params
    # create an RDB object
    # run an insert

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r, d = rdb_people_2.insert({'playerID': 'abadfe01', "birthYear": "1995", "birthMonth": "05"})
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_insert_case_2(): #IMP
    print("RDB::INSERT CASE 2 -----> Wrong field name in new_values")
    # define conn params
    # create an RDB object
    # run an insert

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r, d = rdb_people_2.insert({'playerID1': 'abadfe01', "birthYear": "1995", "birthMonth": "05"})
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_insert_case_3(): #Working case - insert unique values
    print("RDB::INSERT CASE 3 -----> WORKING CASE")
    # del by tem
    # find by template
    # define conn params
    # create an RDB object
    # run an insert

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r, d = rdb_people_2.insert({'playerID': 'gk2547', "birthYear": "1995", "birthMonth": "05"})
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_update_by_template_case_1(): #IMP
    print("RDB::UPDATE_BY_TEMPLATE CASE 1 -----> Wrong field name in new_values")
    # update by template
    # define conn params
    # create an RDB object
    # run a find on a particular row, by template - log
    # perform an update - log

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r, d = rdb_people_2.update_by_template({"birthYear": "1954", "birthMonth": "9"}, {"height1": "165", "weight": "134"})
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")

def RDB_update_by_template_case_2():
    print("RDB::UPDATE_BY_TEMPLATE CASE 2 -----> WORKING CASE")
    # find by template
    # define conn params
    # create an RDB object
    # run a find on a particular row, by template - log
    # perform an update - log
    # run a find, by template - log
    # the result would have different data when compared to the first find

    connect_info = {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbuserdbuser',
        'db': 'lahman2019raw',
        'charset': 'utf8mb4'
    }
    rdb_people_2 = RDBDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r, d = rdb_people_2.find_by_template({"birthYear": "1954", "birthMonth": "9"}, {"height", "weight"})#find
        print(r, d)
        r, d = rdb_people_2.update_by_template({"birthYear": "1954", "birthMonth": "9"}, {"height": "195", "weight": "134"})#update
        print(r, d)
        r, d = rdb_people_2.find_by_template({"birthYear": "1954", "birthMonth": "9"}, {"height", "weight"})#find again
        print(r, d)
    except Exception as e:
        print(e)
    print("\n")


if __name__ == '__main__':
    # find_delete_findAgain()
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

    # find_update_findAgain()



#correct the insert in csv in the end
#write all the test cases now
#insert and update are important
#all test cases to test every edge case for the CSV file
from HW_Assignments.HW1_Template.src.CSVDataTable import *

def CSV_find_by_key_case_1(): #IMP
    print("CSV::FIND_BY_PRIMARY_KEY CASE 1 -----> WORKING CASE")
    # find by template
    # define conn params
    # create an CSV object
    # run a find on a particular row, by key

    connect_info = {'directory': "../Data/Baseball/",
                    'file_name': "Batting.csv"}

    CSV_people_1 = CSVDataTable('batting', connect_info, ['playerID','teamID','yearID','stint'])#playerID alone is the key for player table
    try:
        r = CSV_people_1.find_by_primary_key(['aardsda01','SFN', '2004','1'], ["G", "AB", "R"])  # key_fields and field_list
        print(r)
    except Exception as e:
        print(e)
    print("\n")


def CSV_find_by_key_case_2(): #IMP
    print("CSV::FIND_BY_PRIMARY_KEY CASE 2 -----> Wrong field_name in field_list")
    # find by template
    # define conn params
    # create an CSV object
    # run a find on a particular row, by key

    connect_info = {'directory': "../Data/Baseball/",
                    'file_name': "People.csv"}

    CSV_people_1 = CSVDataTable('people', connect_info, ['playerID'])#playerID alone is the key for player table
    try:
        r = CSV_people_1.find_by_primary_key(['aardsda01'], ["bats1", "height", "weight"])  # key_fields and field_list
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_find_by_key_case_3(): #IMP
    print("CSV::FIND_BY_PRIMARY_KEY CASE 3 -----> key_fields is empty")
    # find by template
    # define conn params
    # create an CSV object
    # run a find on a particular row, by key - log

    connect_info = {'directory': "../Data/Baseball/",
                    'file_name': "People.csv"}

    CSV_people_1 = CSVDataTable('people', connect_info, ['playerID'])#playerID alone is the key for player table
    try:
        r = CSV_people_1.find_by_primary_key([], ["bats", "height", "weight"])  # key_fields and field_list
        print(r)
    except Exception as e:
        print(e)
    print("\n")


def CSV_find_by_template_case_1(): #IMP
    print("CSV::FIND_BY_TEMPLATE CASE 1 -----> WORKING CASE")
    # find by template
    # define conn params
    # create an CSV object
    # run a find on a particular row, by template - log
    # run a find, by template - log

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}
    
    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.find_by_template({'bats': 'R', 'height': '75', 'weight': '215'}, ['playerID', 'birthYear'])
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_find_by_template_case_2(): #IMP
    print("CSV::FIND_BY_TEMPLATE CASE 2 -----> Wrong field name in template")
    # up by tem
    # find by template
    # define conn params
    # create an CSV object
    # run a find on a particular row, by template - log
    # run a find, by template - log

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}
    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.find_by_template({'bats1': 'R', 'height': '75', 'weight': '215'}, ['playerID', 'birthYear'])
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_find_by_template_case_3(): #IMP
    print("CSV::FIND_BY_TEMPLATE CASE 3 -----> Wrong field name in field_list")
    # find by template
    # define conn params
    # create an CSV object
    # run a find on a particular row, by template - log

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}
    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.find_by_template({'bats': 'R', 'height': '75', 'weight': '215'}, ['player2', 'birthYear'])
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_delete_by_key_case_1(): #IMP
    print("CSV::DELETE_BY_KEY CASE 1 -----> WORKING CASE")
    # define conn params
    # create an CSV object
    # run a find on a particular row, by template - log
    # perform an delete - log
    # run a find, by template - log
    # the result would have different data when compared to the first find
    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.find_by_primary_key(['abbated01'])  #find
        print(r)
        r = CSV_people_2.delete_by_key(['abbated01']) #delete
        print(r)
        r = CSV_people_2.find_by_primary_key(['abbated01'])  #find_again
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_delete_by_key_case_2(): #IMP
    print("CSV::DELETE_BY_KEY CASE 2 -----> Wrong number of values in key_fields")
    # del by key
    # find by template
    # define conn params
    # create an CSV object
    # perform an delete, by template - log

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r,d = CSV_people_2.delete_by_key(['aardsda01',"asds"]) #key_fields
        print(r,d)
    except Exception as e:
        print(e)
    print("\n")

def CSV_delete_by_key_case_3(): #IMP
    print("CSV::DELETE_BY_KEY CASE 3 -----> Key fields is empty and wrong number of values in key_fields")
    # del by tem
    # find by template
    # define conn params
    # create an CSV object
    # perform a delete by key

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r,d = CSV_people_2.delete_by_key([]) #key_fields
        print(r,d)
    except Exception as e:
        print(e)
    print("\n")

def CSV_delete_by_template_case_1(): #NON-error case
    print("CSV::DELETE_BY_TEMPLATE CASE 1 -----> WORKING CASE")
    # del by tem
    # find by template
    # define conn params
    # create an CSV object
    # run a find on a particular row, by template - log
    # perform a delete - log
    # run a find, by template - log
    # the result would have different data when compared to the first find

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.find_by_template({"birthYear": "1869", "birthMonth": "11"}, {'birthYear', 'birthMonth'})  # template
        print(r)
        r = CSV_people_2.delete_by_template({"birthYear": "1869", "birthMonth": "11"})  # template
        print(r)
        r = CSV_people_2.find_by_template({"birthYear": "1869", "birthMonth": "11"}, {'birthYear', 'birthMonth'})  # template
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_delete_by_template_case_2(): #IMP
    print("CSV::DELETE_BY_TEMPLATE CASE 2 -----> Wrong field name in template")
    # del by tem
    # find by template
    # define conn params
    # create an CSV object
    # perform an delete - log

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.delete_by_template({"birthYear": "1981", "birthMo": "12"})  # template
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_insert_case_1(): #Working case
    print("CSV::INSERT CASE 1 -----> WORKING CASE")
    # del by tem
    # find by template
    # define conn params
    # create an CSV object
    #perform an insert

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.insert({'playerID': 'gk2547', "birthYear": "1995", "birthMonth": "05"})
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_insert_case_2(): #IMP
    print("CSV::INSERT CASE 2 -----> Voilating the primary key constraint")
    # del by tem
    # find by template
    # define conn params
    # create an CSV object
    # Perform an insert

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.insert({'playerID': 'abadfe01', "birthYear": "1995", "birthMonth": "05"})
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_insert_case_3(): #IMP
    print("CSV::INSERT CASE 3 -----> Wrong field name in new_values")
    # del by tem
    # find by template
    # define conn params
    # create an CSV object
    # Perform an insert

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.insert({'playerID1': 'abadfe01', "birthYear": "1995", "birthMonth": "05"})
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_update_by_template_case_1(): #IMP
    print("CSV::UPDATE_BY_TEMPLATE CASE 1 -----> Wrong field name in new_values")
    # del by tem
    # find by template
    # define conn params
    # create an CSV object
    # perform an update - log

    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.update_by_template({"birthYear": "1954", "birthMonth": "9"}, {"height1": "165", "weight": "134"})
        print(r)
    except Exception as e:
        print(e)
    print("\n")

def CSV_update_by_template_case_2():
    print("CSV::UPDATE_BY_TEMPLATE CASE 2 -----> WORKING CASE")
    # del by tem
    # find by template
    # define conn params
    # create an CSV object
    # run a find on a particular row, by template - log
    # perform an update - log
    # run a find, by template - log
    # the result would have different data when compared to the first find
    connect_info = {
        'directory': "../Data/Baseball/",
        'file_name': "People.csv"}

    CSV_people_2 = CSVDataTable('people', connect_info, ['playerID'])  # playerID alone is the key for player table
    try:
        r = CSV_people_2.find_by_template({"birthYear": "1954", "birthMonth": "9"}, {"height", "weight"})#find
        print(r)
        r = CSV_people_2.update_by_template({"birthYear": "1954", "birthMonth": "9"}, {"height": "195", "weight": "134"})#update
        print(r)
        r = CSV_people_2.find_by_template({"birthYear": "1954", "birthMonth": "9"}, {"height", "weight"})#find again
        print(r)
    except Exception as e:
        print(e)
    print("\n")


if __name__ == '__main__':
    # find_delete_findAgain()
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

    # find_update_findAgain()



#correct the insert in csv in the end
#write all the test cases now
#insert and update are important
import json
import requests

class AppTest:

    _default_connect_info = {
        'host': 'localhost',
        'user': 'root',
        'password': 'dbuserdbuser',
        'db': 'lahman2019clean',
        'port': 3306
    }

    def __init__(self):
        self.connect_info = AppTest._default_connect_info #static variable
        self.session = requests.session()


    def route_1_case_1(self):
        print("CASE 1 for route 1: ")
        #make HTTP calls to the application using requests
        #Do the same in postman as well and add the screenshots
        res = self.session.get("http://127.0.0.1:5002/api/lahman2019clean/people/gkot009953")
        item_dict = json.dumps(res.text)
        print(res.text)
        print("\n")
        pass


    def route_1_case_2(self):
        print("CASE 2 for route 1: ")
        # make HTTP calls to the application using requests
        # Do the same in postman as well and add the screenshots
        res = self.session.put("http://127.0.0.1:5002/api/lahman2019clean/people/gkot009953?nameLast=kotapalle")
        item_dict = json.dumps(res.text)
        print(res.text)
        print("\n")

        pass


    def route_1_case_3(self):
        print("CASE 3 for route 1: ")
        # make HTTP calls to the application using requests
        # Do the same in postman as well and add the screenshots
        res = self.session.put("http://127.0.0.1:5002/api/lahman2019clean/people/gkotpal0096?nameLast=kotapalle")
        item_dict = json.dumps(res.text)
        print(res.text)
        print("\n")

        pass


    def route_1_case_4(self):
        print("CASE 4 for route 1: ")
        # make HTTP calls to the application using requests
        # Do the same in postman as well and add the screenshots
        res = self.session.delete("http://127.0.0.1:5002/api/lahman2019clean/people/gkotpal0096")
        item_dict = json.dumps(res.text)
        print(res.text)
        print("\n")

        pass


    def route_2_case_2(self):
        print("CASE 5 for route 1: ")
        # make HTTP calls to the application using requests
        # Do the same in postman as well and add the screenshots
        res = self.session.delete("http://127.0.0.1:5002/api/lahman2019clean/people/gkotpal00961")
        item_dict = json.dumps(res.text)
        print(res.text)
        print("\n")
        pass


    def route_3_case_1(self):
        pass


    def route_3_case_2(self):
        pass


    def route_3_case_3(self):
        pass


    def route_4_case_1(self):
        pass


    def route_4_case_2(self):
        pass


    def route_4_case_3(self):
        pass


    def route_5_case_1(self):
        pass


    def route_5_case_2(self):
        pass


    def route_5_case_3(self):
        pass

    def route_2_case_1(self):
        pass


if __name__ == "__main__":

    test_obj = AppTest()

    test_obj.route_1_case_1()
    test_obj.route_1_case_2()
    test_obj.route_1_case_3()
    test_obj.route_1_case_4()


    test_obj.route_2_case_1()
    test_obj.route_2_case_2()
    test_obj.route_3_case_3()

    test_obj.route_3_case_1()
    test_obj.route_3_case_2()
    test_obj.route_3_case_3()

    test_obj.route_4_case_1()
    test_obj.route_4_case_2()
    test_obj.route_4_case_3()

    test_obj.route_5_case_1()
    test_obj.route_5_case_2()
    test_obj.route_5_case_3()


API_KEY = "756zx4M5ThXZLOi0JszVjzMOapultFEv"

import requests

def getCourses(limit = -1, skip = -1, sort = -1):
    request_url = "https://cobalt.qas.im/api/1.0/courses?key="+API_KEY
    if limit is not -1:
        request_url = request_url + "&limit=" + str(limit)
    if skip is not -1:
        request_url = request_url + "&skip=" + str(skip)
    if sort is not -1:
        request_url = request_url + "&sort=" + str(sort)
    r = requests.get(request_url)
    return r.status_code

def getCourseById(id):
    request_url = "https://cobalt.qas.im/api/1.0/courses/" + id + "?key="+API_KEY
    r = requests.get(request_url)
    return r.status_code

if __name__ == "__main__":
    print("Hello World");
    print(getCourses(limit=100))
    print(getCourseById("CSC148H1F20179"))

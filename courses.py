import requests


API_KEY = "756zx4M5ThXZLOi0JszVjzMOapultFEv"


# Helper function that uses the url, and given parameters to make HTTP request and get back data
def _get_from_url(request_url, query=-1, limit=-1, skip=-1, sort=-1):
    request_url = request_url+"?key="+API_KEY
    if query is not -1:
        request_url = request_url + "&q=" + str(query)
    if limit is not -1:
        request_url = request_url + "&limit=" + str(limit)
    if skip is not -1:
        request_url = request_url + "&skip=" + str(skip)
    if sort is not -1:
        request_url = request_url + "&sort=" + str(sort)
    r = requests.get(request_url)
    return r.status_code


# Get a list of all courses, (default limit 10, max limit 100)
def get_courses(limit = -1, skip = -1, sort = -1):
    request_url = "https://cobalt.qas.im/api/1.0/courses"
    return _get_from_url(request_url, -1, limit, skip, sort)


# Get a course by its id
def get_course_by_id(id):
    request_url = "https://cobalt.qas.im/api/1.0/courses/" + id
    return _get_from_url(request_url)


# Get a list of courses that satisfy the search query
def get_courses_by_search(query, limit=-1, skip=-1, sort=-1):
    request_url = "https://cobalt.qas.im/api/1.0/courses/search"
    return _get_from_url(request_url, query, limit, skip, sort)


# Get a list of courses that satisfy the filtery query
def get_courses_by_filter(query, limit=-1, skip=-1, sort=-1):
    request_url = "https://cobalt.qas.im/api/1.0/courses/filter"
    return _get_from_url(request_url, query, limit, skip, sort)


# Basic Tests
if __name__ == "__main__":
    print("Hello World")
    print(get_courses(limit=100))
    print(get_course_by_id("CSC148H1F20179"))
    print(get_courses_by_search("Calculus"))
    print(get_courses_by_filter('instructor:"D Liu" AND code:"CSC" AND level:<=200'))

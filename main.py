import requests 
from mcp.server.fastmcp import FastMCP

# --- Configuration ---

MOODLE_URL = "http://localhost:9090" 
MOODLE_TOKEN = "559499561795c58013d7b346df2058b7"

mcp = FastMCP("Moodle Course Connector")


def call_moodle_api(ws_function, params={}):
    rest_url = f"{MOODLE_URL}/webservice/rest/server.php"


    
    all_params = {
        'wstoken': MOODLE_TOKEN,
        'wsfunction': ws_function,
        'moodlewsrestformat': 'json',
    }
    all_params.update(params)

    try:
        response = requests.post(rest_url, data=all_params, timeout=10)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling Moodle API: {e}")
        return None 

@mcp.tool("getCoursesIDsNamesAndSummaries")
def get_courses():

    """
    this function returns a list of all courses from moodle! It can be used to get the ID of a course.

    parameters:
    None

    returns:
    A list of dictionaries containing the following keys:
    id: The ID of the course
    fullName: The full name of the course
    shortName: The short name of the course
    summary: A summary of the course
    
    """

    try:
        moodle_data = call_moodle_api('core_course_get_courses')

        if moodle_data is None:
            return "An error occurred while calling Moodle API."

        # Verarbeite alle Kurse in einer Liste
        processed_courses = []
        for course in moodle_data:
            processed_courses.append({
                "id": course.get('id'),
                "fullName": course.get('fullname'),
                "shortName": course.get('shortname'),
                "summary": course.get('summary', '').strip(),
            })
        
        return processed_courses

    except Exception as e:
        print(f"An exception occurred: {e}")
        return "An error occurred while processing the courses."
    


@mcp.tool("getCourseContents")
def get_courses(id: int):

    """
    this function returns the contents of a course from moodle

    parameters:
    id: The ID of the course as an integer

    returns:
    The conents of the course as string.
    
    """

    try:
        moodle_data = call_moodle_api('core_course_get_contents', {'courseid': id})

        if moodle_data is None:
            return "An error occurred while calling Moodle API."

        
        return moodle_data

    except Exception as e:
        print(f"An exception occurred: {e}")
        return "An error occurred while processing the courses."
    




if __name__ == '__main__':
    mcp.run(transport="stdio")
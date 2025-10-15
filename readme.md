# Moodle Course Connector for MCP


This Python script provides a simple interface to a Moodle instance's Web Service API. It is designed to be used as a tool provider for MCP-compatible applications like LMStudio, allowing a language model to interact with Moodle data.

# Features
List Courses: Fetches a list of all available courses, including their IDs, names, and summaries.

Get Course Contents: Retrieves the detailed contents of a specific course using its ID.

(Its easy to add more tools to the script, just follow the same structure.)

MCP Integration: Exposes Moodle functions as tools using the FastMCP library.

# Prerequisites
Before you begin, ensure you have the following installed:

Python

The requests and mcp Python libraries.


You will also need administrative access to a Moodle instance to enable API access and generate a token.

Setup & Configuration
Follow these steps to get the script running.

1. Installation
Clone this repository or download the script. Then, install the required Python packages:

```
pip install requests mcp[cli]
```

2. Moodle API Setup
    Search for "Enable Web Service in moodle" on google. If you follow the instructions, you should get the token you need to use in the script.

3. Script Configuration
Open the Python script and update the following configuration variables with your Moodle instance details:

```
Replace with your Moodle site's URL

MOODLE_URL = "http://your-moodle-site.com" 

Replace with the token you generated in Moodle

MOODLE_TOKEN = "YOUR_MOODLE_API_TOKEN"
```

Last edit: 15.10.2025
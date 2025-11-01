### --- Code designed by Luis Eduardo Larios Flores for the "Bug and Automation Challenge" for Paylocity

## -- Instructions to setup the environments -- ##

1. Clone the repository in a local folder
2. Open the terminal or the project from Visual Code
3. Make sure you have installed a version for python or python3
4. Create a virtual environment 
    * `python -m venv name-of-the-venv`
5. Activate the venv
    * `venv/Script/Activate` in Windows
    * `source/venv/bin/Activate` in macOS
6. Install the dependencies from the req.txt 
    * `pip install -r req.txt` //note that you can find the req.txt file in the folder root of the repository


## -- Running the tests for the UI
1. Open the project in VS Code
2. Open a terminal in VS Code
3. Activate your virtual environment
4. Make sure that the harcoded values exists:
    1. In `test_update_employee.py` line 24 and line 59 is a value for the Employee ID where the update will happen
    2. In `test_delete_employee.py`line 22, there are a couple of commented lines if you desire to delete byID, otherwise always will delete the first record in the table
5. Run the next command:
   * `pytest -s tests/`
6. Find the results in the terminal

## -- Running the tests for the APIs 
1. Download the collection from the repository folder named "Reports > elarios_paylocity_colletion.json> 
2. Import the collection in Postman
3. Here you got to options:
    1. You can go through every request and send them individually or
    2. You can select the main folder for the collection and in the top right you will find a "Run" button which will 
        guide you through a set up screen for the run of the complete collection
4. You can review the summary of the test in the "Test Result" section of Postman

## -- Additional Notes

Please find in this repository in the folder "Reports > elarios_bugs_report_paylocity.xlsx" an excel with the documentation for all the bugs found during the challenge. 


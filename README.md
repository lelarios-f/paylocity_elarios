### --- Code designed by Luis Eduardo Larios Flores for the "Bug and Automaation Challenge" for Paylocity

## -- Instructions to setup the environments -- ##

1. Clone the repository in a local folder
2. Open the terminal or the project from Visual Code
3. Make sure you have installed a version for python or python3
4. Create a virtual environment 
    <python -m venv name-of-the-venv >
5. Activate the venv
    <venv/Script/Activate > in Windows
    <source/venv/bin/Activate> in macOS
6. Install the dependencies from the req.txt 
    <pip install -r req.txt> //note that you can find the req.txt file in the folder root of the repository


## -- Running the tests for the UI
1. Open the project in VS Code
2. Open a terminal in VS Code
3. Activate your virtual environment
4. Run the next command:
    <pytest -s tests/>
5. Find the results in the terminal

## -- Running the tests for the APIs 
1. Download the collection from the repository folde "Reports > elarios_paylocity_colletion.json> 
2. Import the collection in Postman
3. Here you got to options:
    i. You can go through every request and send them individually or
    ii. You can select the main folder for the collection and in the top right you will find a "Run" button which will 
        guide you through a set up screen for the run of the complete collection
4. You can review the summary of the test in the "Test Result" section of Postman
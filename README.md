## Automation testing of the TodoMVC site

### Purpose 
To implement the UI testing of the TodoMVC site  
The way of implementation relates to the BDD methodology. You can read more [here](https://en.wikipedia.org/wiki/Behavior-driven_development)

### The project structure
    ├── infra                               Infrastructure of tests  
    |    ├── page_elements                  Commonly used models of page elements for building page objects  
    |    └── page_objects                   Functional models of the pages being tested
    ├── tests
    |    ├── features                       Files with the Gherkin scenarios of features
    |    └── step_defs                      Code implementation of the steps used for building Gherkin scenarios
    ├── run-parallel.sh                     Local running of the test in parallel mode
    └── run.sh                              Local running of the tests (includes project install)


### To build and run the project
 - From source(one of the scripts):   
           `./run.sh` - run tests sequentially  
           `./run-parallel.sh` - run tests in parallel
 - In Docker container:   
`docker build -t todos .`  
`docker run todos:latest`

### About tests work
The files in the `tests/features` directory have the Gherkin scenarios of TODO tasks management  
The files are the Tests and the **Documentation** at the same time  

### Issues
Deleting a task by Selenium ActionChains makes test run stack for 10 seconds, without affecting results

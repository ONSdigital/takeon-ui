# Takeon-Ui Layer
#
### Pre-Requisites
 - Browser: 
    - Chrome
    - Version: <latest> eg:83.0.4103.61
   
 - Chromedriver:
    - Chromedriver version - <compatible to browser version> eg:83.0.4103.39
   
      As long as the browser version and chromedriver are compatible to each other even if you don't have the same browser version mentioned here and you can check that in 
      https://chromedriver.chromium.org/downloads when downloading the chromedriver if not the tests will fail.
      and install it in your $HOMEDIR location.
      
 - Environment Variable Setup:
       - Python
       - Version 3.7
       
         Set-up the python path in your bash profile:

             PYTHONPATH="/Users/{Username}/takeon-ui/tests/acceptance-tests/:$PYTHONPATH"
             export PYTHONPATH
          
         or if your project path is in a different location than the path mentioned above then add that the path only.
         
-  Project Dependencies

    Install packages $ pip install -r requirements.txt
    

    
### Running Tests

-  Setting up the environment:
        export AWS_ACCESS_KEY_ID="<AWS_ACCESS_KEY_ID>"
        export AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>"
        export AWS_SESSION_TOKEN="<AWS_SESSION_TOKEN>" 
        export TAKEON_URL="http://<URL>"
        export COGNITO_USER_POOL="<COGNITO_USER_POOL>"
        Replace URL with the enviroment url you wish to test.
        Note: make sure while setting up the url it has 'http://' protocol otherwise tests will fail
     
       
-  To run the BDD tests you need to switch to the features folder first.
        
   - To run one feature file eg: rsi_validation_qvv.feature

                         
        You need to switch to feature file -
        cd takeon-ui/tests/acceptance-tests/features/{survey_folder} and  
        and use - behave {feature_file_name}
          
                
   - To run all feature files part of a sub-folder. eg:bmi/rsi/test-survey
      
      
        You need to switch to features folder -
        cd takeon-ui/tests/acceptance-tests/features/
        and use - behave {survey_folder_name} e.g, behave rsi/
         
   - To run all the scenarios irrespective of survey types 
        
        
        You can be anywhere with in the acceptance tests or in any features folders path
        cd takeon-ui/tests/acceptance-tests/
        and use - 'behave' with no feature file name.
   
   - To run tests in headless mode
        
        
        You can run any one or all tests in headless mode with an additional flag called browser.
        Use - behave {featurefile} -D browser=headless will run in headless mode.
        To run in real chrome browser mode just use - behave {featurefile} without the browser option.
        
    
   - To run tests in order to capture screenshots     
      
      The screenshots gets captured whenever a test fails. In order to test screenshots capability we need to force fail the tests.
     
      First we need to change directory location to acceptance-tests folder 
      
      Example test to run: search feature with smoke tag 
      change the reference number in this feature file manually for Scenario Outline: Using an existing Survey id 
      in the example table to an invalid reference number like '1234'
         
      Once the tests run completes there will be a new screen_shots folder gets created under the acceptance-tests folder with in that folder 
      the screen_shots of the failed feature files are saved with the current date and time stamp.      
           
      
      Change the reference 12000000796 manually to 1234 
      | 066 | 12000000796 | 201903 | to 
      | 066 | 1234        | 201903 |
      
      Then run the below command in the terminal.
      behave -k --tags=@smoke -D browser=headless will run smoke tests in headless mode.
       
   
      
   - To run tests using a docker image
      
      switch to the tests folder cd takeon-ui/tests/ 
      Run the export below commands in the terminal to set the AWS Credentials, Env Url and cognito user pool
          
          export AWS_ACCESS_KEY_ID="<AWS_ACCESS_KEY_ID>"
          export AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>"
          export AWS_SESSION_TOKEN="<AWS_SESSION_TOKEN>"          
          export TAKEON_URL="http://<URL>"
          export TAKEON_URL="<COGNITO_USER_POOL>"
        
      Run the below make command 
                 
          make docker-run  
            
      Finally  you will see the test result like this
        
            
          2 features passed, 0 failed, 52 skipped
          3 scenarios passed, 0 failed, 435 skipped
          23 steps passed, 0 failed, 3577 skipped, 0 undefined


# Takeon-Ui Layer
### Pre-Requisites
 - Browser: 
    - Chrome
    - Version: 83.0.4103.61  
   
 - Chromedriver:
    - Chromedriver version - 83.0.4103.39
   
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

-  Setting up the environment URL:

        export TAKEON_URL="URL"
        Replace URL with the enviroment url you wish to test.
     
       
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
 
      
   - To run tests using a docker image
      
      switch to the tests folder cd takeon-ui/tests/ 
      Run the export command in the terminal to set the url
                    
          export TAKEON_URL="URL"
          
      Replace URL with the environment url you wish to test.
      Run the below make command 
          
          make docker-run  
          
      Finally to see if the tests been run successfully there will be a folder called docker_results gets created automatically after the tests run 
      and will have the screenshots which are been taken after each scenario. 
         

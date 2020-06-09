# Takeon-Ui Layer
### Pre-Requisites
 1. Browser: 
    - Chrome
     - Version: 83.0.4103.61  
   
 2. Chromedriver:
    - Chromedriver version - 83.0.4103.39
   
      As long as the browser version and chromedriver are compatible to each other even if you don't have the same browser version mentioned here and you can check that in 
      https://chromedriver.chromium.org/downloads when downloading the chromedriver if not the tests will fail.
      and install it in your $HOMEDIR location.
      
 3. Environment Variable Setup:
       - Python
       - Version 3.7
       
         Set-up the python path in your bash profile:

             PYTHONPATH="/Users/{Username}/takeon-ui/tests/acceptance-tests/:$PYTHONPATH"
             export PYTHONPATH
          
         or if your project path is in a different location than the path mentioned above then add that the path only.
         
4.  Project Dependencies

    Install packages $ pip install -r requirements.txt
    
### Running Tests

1.  Setting up the environment URL:

        export TAKEON_URL="URL"
        Replace URL with the enviroment url you wish to test.
            
 
2.  To run the tests you need to switch to the features folder first.
        
         cd takeon-ui/tests/acceptance-tests/features/{survey_folder} and  
         survey_folder eg: bmi or rsi
         to run one feature file scenarios use -  behave {feature file name}
         and to run all the scenarios just use - 'behave' with no feature file name.
         

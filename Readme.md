# Takeon-Ui Layer
### Pre-Requisites
 1. Browser: 
    - Chrome
     - Version: 83.0.4103.61  
   
 2. Chromedriver:
    - Chromedriver version - 83.0.4103.39
   
      Make sure the browser version and chromedriver are compatible to each other and you can check that in 
      https://chromedriver.chromium.org/downloads when downloading the chromedriver if not the tests will fail.
      and install it in your $HOMEDIR location.
      
 3. Environment Variable Setup:
       - Python
       - Version 3.7
       
         Set-up the python path in your bash profile:

             PYTHONPATH=/Users/{Username}/takeon-ui/tests/acceptance-tests/:$PYTHONPATH"
             export PYTHONPATH

4.  Project Dependencies

    Install packages $ pip install -r requirements.txt
    
### Running Tests

1.  Set-up the environment url 

     -  Create a class called url_configs in config_files folder.Add the url.
               
               URL_CONFIG = { 'env_url': '' }
     - Make sure add url_configs.py to git exclude in order to ignore the class by git to stop accidentally committing it to repo.
    
            
 
2.  To run the tests you need to be in the features folder.
        
         cd takeon-ui/tests/acceptance-tests/features/ and to run the tests use -  behave {feature file name}

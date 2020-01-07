
### TASK
Design and write UI tests for a chosen site, using PageObject pattern.

* Identify 2 core features (other than sign-up and sign-in) and write tests for them.
* Prepare a readme file describing the tests setup, what features are tested and how to run tests locally from the terminal/command prompt.
* Make sure that the config is not OS dependent - the tests should be runnable on any OS: Windows, OSX or Linux.


## Overview
Repository hosting a small project of test automation using Selenium and Python to test features of twitter.com

#### Tech stack
* Python 3.7
* Pipenv - virtual Python environment for platform independence
* Selenium - web browser automation
* Pytest - Python unit testing library (for assertions)
* Behave - BDD test framework (Python version)
* Allure - test report tool
* WebDriverManager - library for automated handling of webdriver binaries


#### Scope
System under test is twitter.com and specifically two of its core features:
* Tweeting
* Interaction with tweets of other users

Those two features have been covered with working tests in a minimal scope as a Proof of Concept of the test framework however Gherkin BDD scenarios have been created that if implemented would increase the coverage much more. 

### Setup
##### Project configuration:
By default project configuration is handled through settings.ini file in the root directory of the project.
It does not come with email and password credentials for a twitter account so prior to any test execution those must be provided there.
```yaml
[meta]
Browser = Chrome
ImplicitWait = 10

[default_user]
Email =
Password =
```
By default the browser is set to Chrome but Firefox is also supported. 
Webdrivers are automatically downloaded and installed for you.

Also, some credentials must be provided in the data table of login feature scenario. They can be the same ones as those in settings.ini.
```gherkin
Scenario Outline: Log in with credentials
    Given non-logged user is on Twitter login page
    When user fills credentials "<email>" "<password>" in the form and submits
    Then user is logged in and can see the Home page
    Examples:
    | email | password |
    |<here> |<and here>|
```

##### Project requirements:
* Python 3.7+ ([installation instructions](https://www.python.org/downloads/))
* pip ([installation instructions](https://pip.pypa.io/en/stable/installing/))
* pipenv ([installation instructions](https://github.com/pypa/pipenv))
* Allure (optional) ([installation instructions](https://docs.qameta.io/allure/#_installing_a_commandline))

##### Running
Once you have the requirements installed, open your terminal/command line in the root directory of the project and run:

```shell script
pipenv sync
```
and then to run all features:
```shell script
pipenv run behave
```
or to run specific features:
```shell script
pipenv run behave -i features/<feature_name>.feature
```
report from the test run in JSON format is stored by default in reports/ directory and those can be parsed and visualized by Allure:
```shell script
allure serve reports/
```

### Further considerations
Should this framework be taken beyond the proof of concept phase there are certain noteworthy improvements that could be done:
* screenshot handling in framework
* more browsers supported (ie, edge, opera, safari)
* web application elements in Page Objects organized in a more structured manner
* actual implementation of included BDD scenarios
* more extensive exception handling
* some synchronization optimisations
* parallel test runs with different browsers support
* specific browser support policy should be established as running latest versions of everything rarely lasts working for a long time
* this framework could also be extended to test the API (which would be preferable to UI testing in many cases) as BDD is also well suited for this purpose.


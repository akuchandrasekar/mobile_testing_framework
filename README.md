# MOBILE AUTOMATION SETUP


Use python version 3.9.0

### Environment Setup:

* `cd mobiletestingframework`
* `pyenv virtualenv mobiletestingframework`
* `pyenv activate mobiletestingframework`
* `pip install -r requirements.txt`
* Link the venv to PyCharm

### Set Platform, Device Name, Device OS Version & App Path:

Open YAML folder > rename `config_template.yml` to `config.yml`<br />

#### platform - config.yml file
line 2 > set the platform to `ios` or `android`<br />

#### iOS - config.yml file
line 7 > set the iOS platformVersion value [Eg: 13.5]<br />
line 8 > set the deviceName value [Eg: iPhone 11 Pro]<br />
line 13 > folder: `/Users/username/Library/Developer/Xcode/DerivedData/WordPress-bgxbidnfcsphaffyuskxfnuixlek/Build/Products/Debug-iphonesimulator/WordPress.app`<br />

#### Android - config.yml file
line 16 > set the Android platformVersion [Eg: 9]<br />
line 22 > folder: `/Users/username/Desktop/and/wordpress.apk`<br />


### Running Test Suites-

To Start appium server:
Open Terminal and enter the below command
* `appium`

To run a single test case from terminal:<br />
* `cd tests`<br />
* `pytest test_login.py`<br />

To run full suite > From /tests folder, run below command:<br />
* `pytest`<br />

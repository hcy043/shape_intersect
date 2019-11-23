# THE2-Tester
Simple automated test script for METU Ceng Homework (THE 2)

# Installation
Save test.py file to the folder which the2.py is saved

# Usage
cd to folder which the2.py and test.py is saved

Then run command: 
```
python test.py 
```
Or (in some cases)
```
python2 test.py 
```

# Options
Options can be changed by two way:
- By changing directly from the source file (Which is described in the Additional Information section)
- By passing cli arguments. (Which will be described in this section)

## There are 3 CLI option right now
- -fo or --fails-only : By default, whole test log will be shown (Both fails and passes). If this argument is passed only fails will be shown
- -nms or --no-minority-shapes : By default, minority shapes used in test will be shown. If this argument is passed minority shapes that are used in the test will not be shown 
- -nci or --no-calculated-input : By default, calculations from your function will be shown. If this argument is passed calculations from your function will not be shown 

Example usage with cli options
```
python2 test.py -fo --no-minority-shapes
```
The command above will print only fails and will not print minority shapes used in the test

# Additional Information
Some tests can be disabled, and some additional information can be displayed or ignored. Those options can be changed by editing test.py. Information needed to change settings can be found inside test.py, and in comments

# Contribution
Anyone can fork this repo, edit content of test.py, add more tests, add more functionality. After doing so commit your changes and open a pull request. I will merge them after reviewing :)

# Good Luck Everyone :)

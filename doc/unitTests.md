## Introduction 
Unit tests are typically automated tests run on separate sections of the application to make sure each of them behaves as intended. Cocoa boat app is no exception,
we wrote a set of unit tests to make sure the main parts of the application work as intended. 

## Process:
Most of our tests were focused on the 'model.py' class as it contains some very important functionality. 

![Screenshot 2021-05-16 at 22 36 05](https://user-images.githubusercontent.com/61206601/118411874-1b57fc00-b697-11eb-956e-aa127c1b8cc2.png)

Since cocoa is a bot, the best way to test it is by creating another test bot that will test the functionality of the current one. We tried that, but it turned to 
be more complex than anticipated and so we decided to stick to regular unit tests.

## Results:
We achieved 33% of files covered by our tests and 80% of the lines:

![Screenshot 2021-05-16 at 22 38 52](https://user-images.githubusercontent.com/61206601/118411942-7ee22980-b697-11eb-81dd-7d1c3b04888c.png)

This result could be improved, but we were limited by time.

## Challenges:
In some cases we ran into issues with our unit tests and they were quite diffciult to debug. One such case is 'test_add_meeting(self)':

![Screenshot 2021-05-16 at 22 36 05](https://user-images.githubusercontent.com/61206601/118411874-1b57fc00-b697-11eb-956e-aa127c1b8cc2.png)

We tried to debug, but failed to fix the test. Nonetheles it is written and just needs fixing.

## Conclussion:

Unit tests are good way to check the quality of our code and functionality of our products. Moreover, they can help to better understand other people's work like in
our case when we were writing them for a project developed by someone else. 

# Manual testing of Cocoa-bot


- [X] Manual tests

We analysed all the commands that the bot has and different edge cases that could happen doing the communication with the bot. We documented all the test cases in the `manual-tests.md`. There was a first Run for the cases and some of the bugs where discovered such as :

- Important not implemented commands such as `help`
- not handling exceptions doing reading the user input and converting it to a specific time (such as time)
- the bot sometimes does not communicat important information such as doing the `list meetings` and `cancel meetings`, if there there were no meetings the bot would not say anything to the user
- the bot is down if there was an error

This [PR](https://github.com/BME-MIT-IET/iet-hf2021-spicy-bloodhounds/pull/13) was made to this the following issues (at least partially). 
Another round of manual tests was made for the failed tests.


# Manual tests

##  Analyse all the commands for the bot
- [ ] prefix setup
- [ ] prefux delete me
- [ ] prefix schedule new
- [ ] prefix schedule cancel
- [ ] prefix list meetings

#### Prefix: Cocoapls


# Perform the Test Run with the Test Cases

## Test Case 1: _Use the prefix command_

![image](https://user-images.githubusercontent.com/27647952/118283180-5f98a000-b4cf-11eb-8332-f82098be6243.png)

### Result:
passed, prefix command is working right


## Test Case 2: _get help:_
- [ ] cocoapls help

![image](https://user-images.githubusercontent.com/27647952/118284134-6378f200-b4d0-11eb-9b92-5622dbb9eb15.png)

### Result:
failed, help command is not implimented


## Test Case 3: _setup user_

- [ ] cocoapls setup

￼![image](https://user-images.githubusercontent.com/27647952/118284527-d2564b00-b4d0-11eb-8af5-aa3079c54109.png)

### Result:
passed, the user succesfully is setup


## Test Case 4: _ Schedule new meeting-happy path_

- [ ] cocoapls schedule new

￼![image](https://user-images.githubusercontent.com/27647952/118286868-324df100-b4d3-11eb-9fb3-276fcad75d5c.png)


### Result:
passed, the meeting have beed setup and when a person will want to also create a new meeting, this two user will be paired



## Test Case 5: _create new meeting with same time_

- [ ] cocoapls schedule new

￼![image](https://user-images.githubusercontent.com/27647952/118287134-73460580-b4d3-11eb-8e58-3141eae10621.png)


### Result:
passed, the meeting is not set, if it's same as the one that already exists



## Test Case 6: _schedule meeting with someone_

- [ ] cocoapls schedule new


### Result:
passed, the user succesfully is setup



## Test Case 7: _create meeting with the wrong format for the time_

- [ ] cocoapls schedule new

![image](https://user-images.githubusercontent.com/27647952/118287348-aa1c1b80-b4d3-11eb-8248-e1dfe35a0bb9.png)



### Result:
Passed, the meeting is not set but the use is not notified about the error




## Test Case 8: _use wrong command_

- [ ] cocoapls schedule

![image](https://user-images.githubusercontent.com/27647952/118287522-d041bb80-b4d3-11eb-83c4-394d2fb0ed84.png)



### Result:
passed, the bot say that the command is not correct, but the bot should display the right commands




## Test Case 9: _cancel meetings_

- [ ] cocoapls schedule cancel

![image](https://user-images.githubusercontent.com/27647952/118287636-ed768a00-b4d3-11eb-9591-f9eef6ffc56b.png)



### Result:
failed, the bot did not notify that there are no meetings



## Test Case 10: _list meetings when there are no meetings_

- [ ] cocoapls list meetings

![image](https://user-images.githubusercontent.com/27647952/118287786-1434c080-b4d4-11eb-944d-5f9950a1a213.png)



### Result:
failed, the bot does not show that there are no meetings



## Test Case 11: _delete user_

- [ ] cocoapls delete me

![image](https://user-images.githubusercontent.com/27647952/118287893-2dd60800-b4d4-11eb-8acf-dc03d9bcd59b.png)


### Result:
passed, the use is deleted



## Test Case 12: _how bot behaves after the error in the input_

- [ ] cocoapls schedule, cocoapls delete me ...

￼![image](https://user-images.githubusercontent.com/27647952/118287986-45ad8c00-b4d4-11eb-8565-e1b288057810.png)



### Result:
failed. The bot is down










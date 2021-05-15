# Cocoa bot :robot:

Cocoa is a Discord bot to schedule "coffee-breaks" for server members. You can use it just to chat with anyone that is interested to spend some time in a virtual "coffe-break" or to ask for help for a specific question and other types of meetings. The meetings are created with random people that are interested in the same goal for the meetings.


### CI and static techniques
- [ ] Running a static analysis tool and reviewing the reported problems (SonarQube, FindBugs, VS Code Analyzer, Codacy, Coverity Scan...). As static analysis tools could find numerous problems, it is enough to review only a subset of them. If the team agrees with the reported problem, it can fix some of them. Try to review different types of problem and concentrate on more complex ones (e.g. not just formatting errors).

- [ ] Supporting deployment (Docker, Vagrant...)
- [ ] Performing manual code review on some part of the application (GitHub, Gerrit...)


### Testing

- [ ] Creating or extending unit tests (xUnit...)
- [ ] Designing, executing and documenting manual tests
- [ ] Measuring code coverage for tests and extending test suite based on the results (JaCoCo, OpenCover, Coveralls, Codecov.io...)


# CI and static techniques



# Testing :beetle:

- [X] Manual tests

We analysed all the commands that the bot has and different edge cases that could happen doing the communication with the bot. We documented all the test cases in the `manual-tests.md`. There was a first Run for the cases and some of the bugs where discovered such as :

- Important not implemented commands such as `help`
- not handling exceptions doing reading the user input and converting it to a specific time (such as time)
- the bot sometimes does not communicat important information such as doing the `list meetings` and `cancel meetings`, if there there were no meetings the bot would not say anything to the user
- the bot is down if there was an error

This [PR](https://github.com/BME-MIT-IET/iet-hf2021-spicy-bloodhounds/pull/13) was made to this the following issues (at least partially). 
Another round of manual tests was made for the failed tests.










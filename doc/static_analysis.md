## Static analysis tools

## Introduction
Static analysis, is a debugging type that is done by examining the code without executing the program. The process makes the code more clean, understandable and makes sure it meets all the industry standarts.Automated tools can assist programmers and developers in carrying out static analysis. The software chosen for scanning and validation the projects is SonarLint, Pylint, Codacy

## Sonar Lint results
After the evaluation with SonarLint and Pylint the following issue were found

* Unnecessary comments
Which is the great code smell, since is case variables, attributes and methods are named in the proper way, then there is no need in the comments at all. Or they suppose to be short and neat. All comments have been removed and variable names changed

* Repeated strings
In some cases Cocoa bot project contained duplication strings (bot answers the same way in different cases. It was decided to move the strings to the variables and constants, so we can reuse them later.

## Codacy

The second level of static analysis was connection of the repository to the Codacy tool. Which appeared to be more sofisticated than the others. Codacy found 91 issues. The majority of which were just simple coding style issues, however, there are also some security and error prone vulnerabilities

![Screen Shot 2021-05-16 at 19 48 46](https://user-images.githubusercontent.com/57729718/118407233-1a67a000-b680-11eb-9b58-5496a63a6c36.png)

Unused imports and variable assignments were immediately corrected as well as the tests (which caused a lot of issues at the time of evaluation).

It was decided by the team, that README file errors and warnings are not considered as critical ones, to be corrected

![Screen Shot 2021-05-16 at 19 59 57](https://user-images.githubusercontent.com/57729718/118407494-4b94a000-b681-11eb-9159-ed15b554294f.png)








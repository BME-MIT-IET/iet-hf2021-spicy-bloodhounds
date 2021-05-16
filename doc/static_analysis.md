## Static analysis tools

## Introduction
Static analysis, is a debugging type that is done by examining the code without executing the program. The process makes the code more clean, understandable and makes sure it meets all the industry standarts.Automated tools can assist programmers and developers in carrying out static analysis. The software chosen for scanning and validation the projects is SonarLint, Pylint, Codacy

## Sonar Lint results
After the evaluation with SonarLint and Pylint the following issue were found

* Unnecessary comments
Which is the great code smell, since is case variables, attributes and methods are named in the proper way, then there is no need in the comments at all. Or they suppose to be short and neat. All comments have been removed and variable names changed

* Repeated strings
In some cases Cocoa bot project contained duplication strings (bot answers the same way in different cases. It was decided to move the strings to the variables and constants, so we can reuse them later.



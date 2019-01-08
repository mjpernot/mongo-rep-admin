# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.0.1] - 2018-11-30
### Changed
- Documentation updates.


## [3.0.0] - 2018-05-01
Breaking Change

### Changed
- Changed "mongo_class" calls to new naming schema.
- Changed "mongo_libs" calls to new naming schema.
- Changed "cmds_gen" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [2.2.0] - 2018-04-26
### Changed
- Changed "svr_mongo" to "mongo_class" module reference.
- Changed "cmds_mongo" to "mongo_libs" module reference.

### Added
- Added single-source version control.


## [2.1.0] - 2017-08-17
### Changed
- Help_Message: Replace docstring with printing the programs __doc__.
- Change single quotes to double quotes.
- Convert program to use local libraries from ./lib directory.


## [2.0.0] - 2017-01-26
### Changed
- Made a large number of changes to the program.  Collapsed and streamlined the code.  Replaced blocks of code with calls to existing library functions.  Modified the options to bring inline with the programming standard.  Changed the output option to be always standard out unless requesting the output to be in JSON format (see new option below).

### Added
- Added -m option to allow data insertions to be put into a different mongo database than the present one.
- Added -j option to represent JSON format.


## [1.4.0] - 2016-03-22
### Changed
- Chk_Mem_Rep_Lag: Changed 'Secondary' to 'Slaves' and 'Primary' to 'Master' in the JSON document.  This is to standardize the dictionary key values.


## [1.3.0] - 2016-03-21
### Changed
- main:  Added "I" option to process steps.
- Chk_Rep_Lag:  Processing the "-I" option.
- Chk_Mem_Rep_Lag:  If a database and table is present, then call function to insert document.
- Help_Message:  Added documentation for new option.

### Added
- Added new option ("-I") for the Check Replication Lag function to write the JSON document to a database collection.


## [1.2.0] - 2016-03-16
### Added
- Added new functionality to program to allow the Check Replication Lag function (Chk_Rep_Lag) to print its output in JSON format.  This will be used to update a status web page.

### Changed
- main:  Added several new variables, added Arg_File_Chk function to the 'if' statement check.  Added two new options:  "-F" and "-O" for output format and output file respectively.
- Chk_Rep_Lag:  Processed the "-F" and "-O" options and passed them to the functions as named arguments (kwargs).
- Chk_Mem_Rep_Lag:  Setup new format as dictionary, printed out as normal or to the dictionary, converted the dictionary to JSON and then called Print_Data function to print the data to the correct output location (i.e. screen, file).
- Fetch_Rep_Lag:  Returns seconds ago if a JSON format or prints out if standard output.
- Help_Message:  Added documentation for new options.


## [1.1.0] - 2016-03-04
### Changed
- Run_Program:  Corrected an error in argument line in the call to the svr_mongo.Coll class call.
- Fetch_Priority:  Corrected an error in argument line in the call to the svr_mongo.Coll class call.
- main:  Removed some obsolete commented out code.


## [1.0.0] - 2016-02-19
- Initial creation.

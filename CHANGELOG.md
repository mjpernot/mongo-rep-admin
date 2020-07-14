# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.3.0] - 2020-07-13
### Added
- Added email, mongo insertion, write to file and suppression capability for the -L option in standard out format.
- \_process_std:  Process standard out formatted data.

### Changed
- chk_mem_rep_lag:  Refactored to handle only the JSON format and convert to standard out format if requested.
- Documentation updates.


## [3.2.1] - 2020-05-05
### Fixed
- fetch_members:  Refactored function to use adm_cmd("replSetGetStatus") call to get the replica set data.
- \_process_json:  Sent correct formatted data to gen_libs.display_data call.
- Documentation correction for -T and -S options.

### Changed
- \_process_json:  Changed variable name to standard naming convention.
- run_program:  Changed variable name to standard naming convention.
- fetch_priority:  Changed variable name to standard naming convention.
- chk_rep_stat:  Changed variable name to standard naming convention.

### Removed
- Removed non-used module libraries.


## [3.2.0] - 2020-04-22
### Added
- Added "-f" option to allow the flattening of the JSON data structure to file and standard out.
- Added "-a" option to allow for appending of data to existing output file.

### Changed
- chk_mem_rep_lag: Set the time format string to a variable to reduce literals.
- \_process_json:  Added -f option to set the indentation setting for the JSON structure.
- \_process_json:  Added -a option to set the file mode for writing to out file.
- Documentation changes.

### Fixed
- main:  Fixed handling command line arguments from SonarQube scan finding.


## [3.1.1] - 2019-10-18
### Fixed
- \_process_json:  Fixed printing JSON document to standard out.

### Changed
- \_process_json:  Added standard out suppression.
- chk_rep_lag:  Added args_array to chk_mem_rep_lag() call.
- Updated documentation.
- Added -z option to program - to suppres standard out for -L option.
- run_program:  Use repset name from config file first before querying for it.
- run_program:  Replaced setup_mail() call with gen_class.setup_mail() call.
- run_program:  Changed a number of arguments from positional to keyword arguments.
- fetch_priority:  Changed a number of arguments from positional to keyword arguments.
- fetch_priority:  Changed variable name to standard naming convention.

### Removed
- setup_mail:  Replaced by gen_class.setup_mail function.


## [3.1.0] - 2019-08-12
### Fixed
- rep_health_chk:  Fixed mutable list/dictionary argument issue.
- rep_state_chk:  Fixed mutable list/dictionary argument issue.
- rep_msg_chk:  Fixed mutable list/dictionary argument issue.
- get_master:  Fixed mutable list/dictionary argument issue.
- get_optimedate:  Fixed mutable list/dictionary argument issue.
- chk_mem_rep_lag:  Fixed mutable list/dictionary argument issue.
- chk_rep_stat:  Fixed mutable list/dictionary argument issue.
- prt_rep_stat:  Fixed mutable list/dictionary argument issue.
- fetch_priority:  Fixed mutable list/dictionary argument issue.
- fetch_members:  Fixed mutable list/dictionary argument issue.
- chk_rep_lag:  Fixed mutable list/dictionary argument issue.
- run_program:  Fixed mutable list/dictionary argument issue.

### Added
- \_process_json:  Private function for chk_mem_rep_lag().  Process JSON data.
- setup_mail:  Initialize a mail instance.

### Changed
- chk_mem_rep_lag:  Replaced section of code with call to \_process_json.
- chk_mem_rep_lag:  Replaced mongo_libs.json_prt_ins_2_db call with own internal code.
- chk_mem_rep_lag:  Changed class_inst to class_cfg to be more descriptive.
- chk_rep_lag:  Changed rep_cfg to mongo_cfg and class_inst to class_cfg to be more descriptive.
- chk_mem_rep_lag:  Added capability to mail out JSON formatted data.
- chk_mem_rep_lag:  Converted outdata to JSON format for email.
- chk_rep_lag:  Passing mail instance to chk_mem_rep_lag function.
- run_program:  Added setup of mail instance and passing mail instance to functions.
- main:  Added '-e' and '-s' options to allow for email capability for some options.
- rep_state_chk:  Refactored the "if" statements logic.
- main:  Refactored the "if" statements logic.
- run_program:  Changed variables to standard naming convention.
- chk_rep_lag:  Changed variables to standard naming convention.
- fetch_members:  Changed variable to standard naming convention.
- fetch_priority:  Changed variable to standard naming convention.
- prt_rep_stat:  Changed variable to standard naming convention.
- chk_rep_stat:  Changed variable to standard naming convention.
- chk_mem_rep_lag:  Converted JSON output to camelCase.
- get_optimedate:  Added \*\*kwargs to argument list.
- get_master:  Added \*\*kwargs to argument list.
- rep_msg_chk:  Added \*\*kwargs to argument list.
- rep_state_chk:  Added \*\*kwargs to argument list.
- rep_health_chk:  Added \*\*kwargs to argument list.


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
- Help_Message: Replace docstring with printing the programs \_\_doc\_\_.
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


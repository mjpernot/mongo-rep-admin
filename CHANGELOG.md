# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [5.0.0] - 2025-04-01
Breaking changes

- Updated pytho-lib v4.0.1
- Removed displaying out in standard output, all output will be JSON format.

### Added
- Added the -k, -a and -n options, respectively expand the JSON format, write to file mode and indentation spacing.
- create_data_config: Create data out config parameters.

### Changed
- chk_mem_rep_lag: Refactored function to remove any processing of arguments, replaced datetime with TimeFormat class instance, removed process_std and process_json calls and replaced with mongo_libs.data_out call.
- chk_rep_lag: Refactored function to remove any processing of arguments contained in data out configuration.
- call_func: Refactored function to set up the data out config parameters and TimeFormat instance and removed mail setup call.

### Removed
- process_std: No longer displaying out in standard output.
- process_json: Replaced with call to mongo_libs.data_out.
- Removed the -j and -f options.

## [4.0.2] - 2025-03-11
- Added support for Mongo 7.0
- Updated mongo-libs to v4.5.1

### Fixed
- Fixed pre-header where to determine which python version to use.

### Removed
- Mongo 3.4 support.


## [4.0.1] - 2025-02-11

### Fixed
- Add pre-header check on allowable Python versions to run.


## [4.0.0] - 2025-01-28
Breaking Changes

- Removed support for Python 2.7.
- Added pymongo==4.10.1 for Python 3.9 and Python 3.12.
- Added dnspython==2.7.0 for Python 3.9 and Python 3.12.
- Updated python-lib v4.0.0
- Updated mongo-lib v4.4.0

### Added
- call_func: Call each function selected.
- process_std: Process standard out formatted data.
- process_json: Process JSON data.

### Changed
- run_program: Replaced \_call_func call with call_func call.
- chk_mem_rep_lag: Replaced \_process_json call with process_json call.
- chk_mem_rep_lag: Replaced \_process_std call with process_std call.
- get_optimedate: Replaced "if" statement inside loop with max() call.
- Converted strings to f-strings.
- Documentation changes.

### Deprecated
- Support for Mongo 3.4

### Removed
- \_call_func function.
- \_process_json function.
- \_process_std function.


## [3.7.6] - 2024-11-21
- Updated distro==1.9.0 for Python 3
- Updated psutil==5.9.4 for Python 3
- Updated python-lib to v3.0.8
- Updated mongo-lib to v4.3.4

### Deprecated
- Support for Python 2.7


## [3.7.5] - 2024-09-27
- Updated pymongo==4.1.1 for Python 3.6
- Updated simplejson==3.13.2 for Python 3
- Updated mongo-lib to v4.3.2
- Updated python-lib to v3.0.5


## [3.7.4] - 2024-09-23

### Fixed
- config/mongo.py.TEMPLATE: Added missing TLS entries.


## [3.7.3] - 2024-09-10

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [3.7.2] - 2024-04-22
- Updated mongo-lib to v4.3.0
- Added TLS capability
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- run_program, fetch_priority: Added TLS parameters to database instance calls.
- Set pymongo to 3.12.3 for Python 2 and Python 3.
- Documentation updates.


## [3.7.1] - 2024-02-26
- Updated to work in Red Hat 8
- Updated mongo-lib to v4.2.9
- Updated python-lib to v3.0.3

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [3.7.0] - 2023-08-31
- Upgraded python-lib to v2.10.1
- Replaced the arg_parser code with gen_class.ArgParser code.

### Changed
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main: Removed gen_libs.get_inst call.


## [3.6.2] - 2022-11-30
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4 
- Upgraded mongo-lib to v4.2.2

### Fixed:
- run_program, fetch_priority: Added SSL entries to the mongo_class instance calls.

### Changed     
- run_program: Made auth_mech a required parameter, cannot be passed as an empty argument anymore.
- run_program, fetch_priority:  Removed the use_arg and use_uri arguments.
- Converted imports to use Python 2.7 or Python 3.
- \_process_std: Added int() to convert floating division to integer division.
- Documentation update.


## [3.6.1] - 2022-06-27
- Upgrade python-lib to v2.9.2
- Upgrade mongo-libs to v4.2.1

### Changed
- config/mongo.py.TEMPLATE: Removed old entries.


## [3.6.0] - 2021-09-07
- Updated to work in Mongo 4.2.14 environment.
- Updated to work in a SSL environment.
- Added ability to override the default mail command and use mailx.

### Changed
- \_process_std, \_process_json, node_chk:  Added use_mailx option to send_mail function call.
- main:  Add -u option to the conditional required list.
- config/mongo.py.TEMPLATE:  Added SSL connection entries.
- Removed unnesscary \*\*kwargs from argument lists.
- Documentation updates.


## [3.5.0] - 2021-01-08
- Verified to work with pymongo v3.8.0.
- Updated to be used in FIPS 140-2 environment.

### Changed
- run_program:  Capture and process status return from function calls and replaced section of code with call to \_call_func function.
- fetch_priority:  Returned status of Collection connection to calling function.
- node_chk, prt_rep_stat, chk_rep_stat, fetch_members:  Added return status code.
- node_chk:  Replace section of code with call to single_node_chk function.
- node_chk:  Refactored indent check and removed redundant data in node status return.
- chk_rep_lag, chk_mem_rep_lag, \_process_std, \_process_json:  Capture and return connection status on Mongo call.
- run_program, fetch_priority:  Added "auth_mech" to mongo_class instance call.
- run_program, fetch_priority:  Capture and process connection status on Mongo connect call.
- run_program, fetch_priority:  Replaced "cmds_gen.disconnect" with "mongo_libs.disconnect".
- config/mongo.py.TEMPLATE:  Added authentication mechanism entries to config file.
- Documentation updates.

### Added
- \_call_func:  Private function for run_program and call each function selected.
- single_node_chk:  Check the status of a single node.

### Removed
- cmds_gen module library.


## [3.4.0] - 2020-10-19
### Added
- node_chk:  Check the status of all Mongo nodes.
- Added -N option to run a node health check on all Mongo nodes.

### Changed
- run_program, fetch_priority:  Updated parameter settings to mongo_class to use in mongo_libs v4.0.0.
- fetch_priority:  Updated configuration settings for mongo_libs v4.0.0.
- main: Added -N option to function dictionary.
- run_program:  Changed configuration entry match configuration file.
- config/mongo.py.TEMPLATE:  Changed configuration entry and added three new entries.
- Documentation updates.


## [3.3.0] - 2020-07-13
### Added
- Added email, mongo insertion, write to file and suppression capability for the -L option in standard out format.
- \_process_std:  Process standard out formatted data.

### Changed
- run_program:  Added repset_hosts to mongo_class.RepSet instance call.
- chk_mem_rep_lag:  Changed dictionary to PascalCase.
- chk_mem_rep_lag:  Refactored to handle only the JSON format and convert to standard out format if requested.
- Documentation updates.

### Removed
- fetch_rep_lag


## [3.2.1] - 2020-05-05
### Fixed
- fetch_members:  Refactored function to use adm_cmd("replSetGetStatus") call to get the replica set data.
- \_process_json:  Sent correct formatted data to gen_libs.display_data call.
- Documentation updates.

### Changed
- run_program, fetch_priority, chk_rep_stat, \_process_json:  Changed variable name to standard naming convention.

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
- Documentation updates.

### Fixed
- main:  Fixed handling command line arguments from SonarQube scan finding.


## [3.1.1] - 2019-10-18
### Fixed
- \_process_json:  Fixed printing JSON document to standard out.

### Changed
- \_process_json:  Added standard out suppression.
- chk_rep_lag:  Added args_array to chk_mem_rep_lag() call.
- Added -z option to program - to suppres standard out for -L option.
- run_program:  Use repset name from config file first before querying for it.
- run_program:  Replaced setup_mail() call with gen_class.setup_mail() call.
- fetch_priority, run_program:  Changed a number of arguments from positional to keyword arguments.
- fetch_priority:  Changed variable name to standard naming convention.
- Documentation updates.

### Removed
- setup_mail:  Replaced by gen_class.setup_mail function.


## [3.1.0] - 2019-08-12
### Fixed
- Changed in a large number of functions:  Fixed mutable list/dictionary argument issue.

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
- main, rep_state_chk:  Refactored the "if" statements logic.
- chk_rep_lag, fetch_members, fetch_priority, prt_rep_stat, chk_rep_stat, run_program:  Changed variables to standard naming convention.
- chk_mem_rep_lag:  Converted JSON output to camelCase.
- get_master, rep_msg_chk, rep_state_chk, rep_health_chk, get_optimedate:  Added \*\*kwargs to argument list.


## [3.0.1] - 2018-11-30
### Changed
- Documentation updates.


## [3.0.0] - 2018-05-01
Breaking Change

### Changed
- Changed "mongo_class", "mongo_libs", "cmds_gen", "gen_libs", "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.


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
- Documentation update.

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
- Documentation update.


## [1.1.0] - 2016-03-04
### Changed
- Fetch_Priority, Run_Program:  Corrected an error in argument line in the call to the svr_mongo.Coll class call.
- main:  Removed some obsolete commented out code.


## [1.0.0] - 2016-02-19
- Initial creation.


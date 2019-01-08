# Python project for replication administration of a Mongo replica set.
# Classification (U)

# Description:
  This program is used to adminstrate a Mongo replica set, to include checking master status, membership status, replication time lag between primary and secondaries, and replication configuration status.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features
  * Check Replication lag.
  * Show current members in replication set.
  * Show priority for members in replication set.
  * Check status of rep for members in rep set, print errors.
  * Check status of rep for members in rep set and print all.
  * Insert results into a Mongo database.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - mongo_lib/mongo_class
    - mongo_lib/mongo_libs


# Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-rep-admin.git
```

Install/upgrade system modules.

```
cd mongo-rep-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create Mongodb configuration file.

```
cd config
cp mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```


# Program Descriptions:
### Program: mongo-rep-admin.py
##### Description: Replication administration program for a Mongo replica set.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}mongo-rep-admin/mongo-rep-admin.py -h
```


# Help Message:
  Below is the help message for the program.  Recommend running the -h option on the command line to see the latest help message.

    Program:  mongo-rep-admin.py

    Description:  Administration program for Mongo Replication system.  Has a
        number of functions to monitor the status of the replication between
        primary and secondary databases.  The program can monitor and check on
        a number of different aspects in replication to include checking master
        status, membership status, replication time lag between primary and
        secondaries, and replication configuration status.

    Usage:
        mongo_rep_admin.py -c file -d path {-L | -M | -P  | -S | -T |
            -j | -o dir_path/file | -i db:coll | -m file} [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -L => Check Replication lag.
        -M => Show current members in replication set.
        -P => Show priority for members in replication set.
        -S => Check status of rep for members in rep set, print errors.
        -T => Check status of rep for members in rep set and print all.
        -j => Set output to JSON format.
        -i database:collection => Name of database and collection.
            Delimited by colon (:).  Default: sysmon:mongo_rep_lag
        -m file => Mongo config file used for the insertion into a Mongo
            database.  Do not include the .py extension.  Used only with the
            -i option.
        -o path/file => Directory path and file name for output.
        -v => Display version of this program.
         -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -o and -j options is only available for -L option.

    Notes:
        Mongo configuration file format (mongo.py).  The configuration
            file format for the Mongo connection used for inserting data into
            a database.  There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 27017)
            conf_file = None
            auth = True

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:
            
            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_rep_admin.py -c mongo -d config -L

    Workaround:   To disable printing to standard out, use the -o option to
        print to a file.  This is most often useful if wanting to insert into
        a database, but not receive anything on standard out.


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mongo-rep-admin.py program.

### Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-rep-admin.git
```

Install/upgrade system modules.

```
cd mongo-rep-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for mongo-rep-admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-rep-admin
```


### Unit:  help_message
```
test/unit/mongo_rep_admin/help_message.py
```

### Unit:  
```
test/unit/mongo_rep_admin/
```

### Unit:  
```
test/unit/mongo_rep_admin/
```

### Unit:  run_program
```
test/unit/mongo_rep_admin/run_program.py
```

### Unit:  main
```
test/unit/mongo_rep_admin/main.py
```

### All unit testing
```
test/unit/mongo_rep_admin/unit_test_run.sh
```

### Code coverage program
```
test/unit/mongo_rep_admin/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the mongo-rep-admin.py program.

### Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-rep-admin.git
```

Install/upgrade system modules.

```
cd mongo-rep-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.

```
cd test/integration/mongo_rep_admin/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Integration test runs for mongo-rep-admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-rep-admin
```


### Integration:  
```
test/integration/mongo_rep_admin/
```

### All integration testing
```
test/integration/mongo_rep_admin/integration_test_run.sh
```

### Code coverage program
```
test/integration/mongo_rep_admin/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the mongo-rep-admin.py program.

### Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-rep-admin.git
```

Install/upgrade system modules.

```
cd mongo-rep-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.

```
cd test/blackbox/mongo_rep_admin/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Blackbox test run for mongo-rep-admin.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-rep-admin
```


### Blackbox:  
```
test/blackbox/mongo_rep_admin/blackbox_test.sh
```


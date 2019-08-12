# Python project for replication administration of a Mongo replica set.
# Classification (U)

# Description:
  This program is used to adminstrate a Mongo replica set, to include checking master status, membership status, replication time lag between primary and secondaries, and replication configuration status.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


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


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}mongo-rep-admin/mongo-rep-admin.py -h
```


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
test/unit/mongo_rep_admin/chk_mem_rep_lag.py
test/unit/mongo_rep_admin/chk_rep_lag.py
test/unit/mongo_rep_admin/chk_rep_stat.py
test/unit/mongo_rep_admin/fetch_members.py
test/unit/mongo_rep_admin/fetch_priority.py
test/unit/mongo_rep_admin/fetch_rep_lag.py
test/unit/mongo_rep_admin/get_master.py
test/unit/mongo_rep_admin/get_optimedate.py
test/unit/mongo_rep_admin/help_message.py
test/unit/mongo_rep_admin/main.py
test/unit/mongo_rep_admin/prt_rep_stat.py
test/unit/mongo_rep_admin/rep_health_chk.py
test/unit/mongo_rep_admin/rep_msg_chk.py
test/unit/mongo_rep_admin/rep_state_chk.py
test/unit/mongo_rep_admin/run_program.py
test/unit/mongo_rep_admin/setup_mail.py
```

### All unit testing
```
test/unit/mongo_rep_admin/unit_test_run.sh
```

### Code coverage program
```
test/unit/mongo_rep_admin/code_coverage.sh
```

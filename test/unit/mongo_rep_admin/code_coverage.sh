#!/bin/bash
# Unit test code coverage for mongo_rep_admin program.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/chk_rep_lag.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/chk_rep_stat.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/fetch_members.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/fetch_priority.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/fetch_rep_lag.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/get_master.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/get_optimedate.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/help_message.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/main.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/prt_rep_stat.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/rep_health_chk.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/rep_msg_chk.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/rep_state_chk.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/run_program.py
coverage run -a --source=mongo_rep_admin test/unit/mongo_rep_admin/setup_mail.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 

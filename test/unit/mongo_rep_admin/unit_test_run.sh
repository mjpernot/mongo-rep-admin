#!/bin/bash
# Unit testing program for the mongo_rep_admin.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
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

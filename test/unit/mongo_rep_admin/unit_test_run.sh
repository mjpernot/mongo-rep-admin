#!/bin/bash
# Unit testing program for the mongo_rep_admin.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
/usr/bin/python test/unit/mongo_rep_admin/call_func.py
/usr/bin/python test/unit/mongo_rep_admin/create_data_config.py
/usr/bin/python test/unit/mongo_rep_admin/create_header.py
/usr/bin/python test/unit/mongo_rep_admin/chk_mem_rep_lag.py
/usr/bin/python test/unit/mongo_rep_admin/chk_rep_lag.py
/usr/bin/python test/unit/mongo_rep_admin/chk_rep_stat.py
/usr/bin/python test/unit/mongo_rep_admin/fetch_members.py
/usr/bin/python test/unit/mongo_rep_admin/fetch_priority.py
/usr/bin/python test/unit/mongo_rep_admin/get_master.py
/usr/bin/python test/unit/mongo_rep_admin/get_optimedate.py
/usr/bin/python test/unit/mongo_rep_admin/help_message.py
/usr/bin/python test/unit/mongo_rep_admin/main.py
/usr/bin/python test/unit/mongo_rep_admin/node_chk.py
/usr/bin/python test/unit/mongo_rep_admin/rep_health_chk.py
/usr/bin/python test/unit/mongo_rep_admin/rep_msg_chk.py
/usr/bin/python test/unit/mongo_rep_admin/rep_state_chk.py
/usr/bin/python test/unit/mongo_rep_admin/run_program.py
/usr/bin/python test/unit/mongo_rep_admin/single_node_chk.py

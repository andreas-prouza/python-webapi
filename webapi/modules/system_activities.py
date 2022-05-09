import pyodbc
import logging

cnxn = pyodbc.connect('DSN=*LOCAL')
cursor = cnxn.cursor()


#########################################################
# Get WRKACTJOB data
#########################################################
def get_active_jobs(subsystem):
    cursor.execute("Select job_name, subsystem, job_type, thread_count, cpu_time, function_type, FUNCTION, job_status \
        from table(QSYS2.ACTIVE_JOB_INFO(SUBSYSTEM_LIST_FILTER=>upper(?))) t", subsystem) 

    return get_with_column_names(cursor)



#########################################################
# Get WRKACTJOB data
#########################################################
def get_system_status():
    cursor.execute("SELECT ELAPSED_CPU_USED, SYSTEM_ASP_USED \
                    From QSYS2.SYSTEM_STATUS_INFO si") 

    return get_with_column_names(cursor)





#########################################################
# Just to appand column name to each column in each row
#########################################################
def get_with_column_names(cursor):
    column_names = [column[0] for column in cursor.description]

    rows = cursor.fetchall()
    newData = []
    for row in rows:
        tmprow = {}
        for k, v in zip(column_names, row):
            tmprow[k] = v
        newData.append(tmprow)

    logging.debug(f"Result: {newData}")

    return newData

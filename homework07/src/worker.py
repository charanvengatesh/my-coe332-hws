from jobs import q, update_job_status, get_job_by_id
import time


@q.worker
def execute_job(jid):
    job = get_job_by_id(jid)
    update_job_status(jid, 'in progress')
    time.sleep(5)  # simulate working
    update_job_status(jid, 'complete')


execute_job()

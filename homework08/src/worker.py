from jobs import rd, q, update_job_status, get_job_by_id, save_result
import json
from collections import defaultdict


@q.worker
def execute_job(jid):
    job = get_job_by_id(jid)
    update_job_status(jid, 'in progress')

    # Get the HGNC data from Redis
    data = json.loads(rd.get('data'))
    genes = json.loads(data)['response']['docs']

    # Perform Gene Locus Type Analysis
    locus_type_count = defaultdict(int)
    for gene in genes:
        locus_type = gene.get('locus_type', 'Unknown')
        locus_type_count[locus_type] += 1

    # Prepare the result
    result = {
        'locus_types': list(locus_type_count.keys()),
        'counts': list(locus_type_count.values())
    }

    save_result(jid, result)
    update_job_status(jid, 'complete')


execute_job()

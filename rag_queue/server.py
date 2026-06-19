from fastapi import FastAPI, Query
from dotenv import load_dotenv

load_dotenv()

from .client.rq_client import queue
from .queue.worker import process_query 


app = FastAPI()

@app.get('/')
def root():
    return {"Status" : "server is running"}

@app.post('/chat')
def chat( query: str = Query(..., description="the chat query of user")):
    job = queue.enqueue(process_query, query)
    return {"status":"queued", "job_id": job.id}

@app.get('/jobstatus')
def get_result(
        job_id: str = Query(..., description="job id data")
):
    job = queue.fetch_job(job_id=job_id)
    res = job.return_value()
    return {"result": res}

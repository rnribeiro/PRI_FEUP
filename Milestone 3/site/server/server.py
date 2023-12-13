from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SOLR_URL = "http://localhost:8983/solr"  # Replace with your Solr server URL

@app.post("/solr/request")
async def solr_request(request: Request):
    """
    Endpoint to send a request to Solr.
    Expects a JSON payload containing the Solr request data.
    """
    try:
        jsondata = await request.body()
        jsondata = json.loads(jsondata)
        params = json.loads(jsondata['data'])
        # Send a POST request to Solr
        response = requests.get(f"{SOLR_URL}/books_m2/select", params=params['params'])
        print(response)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Solr request failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

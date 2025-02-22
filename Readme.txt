#python -m venv venv
#venv\Scripts\activate
#If you get a security error, run:
#Set-ExecutionPolicy Unrestricted -Scope Process
#venv\Scripts\activate

#deactivate

#pip install fastapi uvicorn jinja2

#uvicorn main:app --reload
#uvicorn app:app --reload     // since your file name is app.py

#Deployment in cloud run
#gcloud auth configure-docker REGION-docker.pkg.dev   / Region eg us-central1
#gcloud auth configure-docker us-central1-docker.pkg.dev

#gcloud run deploy fastapi-app --image=REGION-docker.pkg.dev/PROJECT_ID/fastapi-repo/fastapi-app --region=us-central1

#gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/cloudrunfastapi
#gcloud run deploy --image gcr.io/$GOOGLE_CLOUD_PROJECT/cloudrunfastapi --allow-unauthenticated --region=us-central1
or
#docker build -t REGION-docker.pkg.dev/PROJECT_ID/fastapi-repo/fastapi-app .
#docker push REGION-docker.pkg.dev/PROJECT_ID/fastapi-repo/fastapi-app


#gcloud run deploy fastapi-app \
    --image=REGION-docker.pkg.dev/PROJECT_ID/fastapi-repo/fastapi-app \
    --platform=managed \
    --region=us-central1 \
    --allow-unauthenticated

# The message from postman 
{
  "message": {
    "data": "WW91IGhhdmV0byB1c2UgdGhlIGJlbG93IGNvZGUgdG8gZW5jb2RlIGN1c3RvbSBtZXNzYWdlcyBpbiBCYXNlNjQgdXNpbmcgUHl0aG9uCgppbXBvcnQgYmFzZTY0CiAKbWVzc2FnZSA9ICJZb3VyIGN1c3RvbSBtZXNzYWdlIgoKZW5jb2RlZF9tZXNzYWdlID0gYmFzZTY0LmI2NGVuY29kZShtZXNzYWdlLmVuY29kZSgpKS5kZWNvZGUoKQoKcHJpbnQoZW5jb2RlZF9tZXNzYWdlKQo="  
  }
}
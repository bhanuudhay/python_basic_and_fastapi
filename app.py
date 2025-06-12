from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to home page"}

@app.get('/contact')
def contact():
    return {"message": "Contact page"}
@app.post('/upload')
def handleUpload(files : list[UploadFile]):
    print(files)
    return {"message": "Files uploaded successfully"}


import uvicorn
uvicorn.run(app)

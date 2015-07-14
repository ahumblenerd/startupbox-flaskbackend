# Startupbox-Flask-Backend
A flask backend for Image Similarity Checker.

# Description

The  server returns a json response for input . Input maybe posted to the server as json . 

# Requirements

- Flask
- ImageHash
- MarkupSafe
- Pillow
- Werkzeug
- itsdangerous
- more-itertools
- numpy
- scipy
- six
- wsgiref

```
pip install Flask==0.10.1
pip install ImageHash==1.0
pip install MarkupSafe==0.23
pip install Pillow==2.9.0
pip install Werkzeug==0.10.4
pip install itsdangerous==0.24
pip install more-itertools==2.2
pip install numpy==1.9.2
pip install scipy==0.15.1
pip install six==1.9.0
pip install wsgiref==0.1.2
```
Or

```
pip install -r requirements.txt
```

# Posting to server 

#### Using CURL
Sample 
```
curl -H "Content-Type: application/json" -X POST -d '{"link1": "http://ahumblenerd.github.io/deltateam/images/arun_latest.jpg","link2": "http://ahumblenerd.github.io/deltateam/images/aravind.jpg"}' http://127.0.0.1:5000/
```
General Syntax
```
curl -H Content-Type: application/json" -X POST -d '{"link1": url1 ,"link2": url2"}' http://127.0.0.1:5000/
```
Or using POSTMAN
- Set request body to  
```
{
    "link1": "http://ahumblenerd.github.io/deltateam/images/arun_latest.jpg","link2": "http://ahumblenerd.github.io/deltateam/images/aravind.jpg"
}
```

Sample backend hosted at http://arunpurushothaman.pythonanywhere.com


```
curl -H "Content-Type: application/json" -X POST -d '{"link1": "http://ahumblenerd.github.io/deltateam/images/arun_latest.jpg","link2": "http://ahumblenerd.github.io/deltateam/images/ravind.jpg"}' http://arunpurushothaman.pythonanywhere.com
```

##### Note

Please do not use `https` when posting to pythonanywhereserver as it blocks https requests for free tier users.

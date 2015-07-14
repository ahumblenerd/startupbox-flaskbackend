from flask import Flask
from PIL import Image
import imagehash
import urllib
from flask import request
from flask import jsonify


class sim:

   def __init__(self,res1,res2):
      print "Inside"
      print res1,res2
      urllib.urlretrieve(res1, "data1")
      print "Image 1 downloaded"
      urllib.urlretrieve(res2, "data2")
      print "Image 2 downloaded"
      self.hash = imagehash.dhash(Image.open("data1"))
      print "Hashing first image"
      self.otherhash = imagehash.dhash(Image.open("data2"))
      print "Hashing second image"

   def check_sim(self) :
      if (self.hash - self.otherhash < 10):                     # hamming distance threshold
         return 'Similar'
      else :
         return 'Different'

   def percentage(self):
      h1=str(self.hash)
      h2=str(self.otherhash)
      h_size = len(h1) * 4
      h = (bin(int(h1, 16))[2:]).zfill(h_size)
      h_size = len(h2) * 4
      h_1 = (bin(int(h2, 16))[2:]).zfill(h_size)
      x= len(h_1)
      for i in range(64):
         if h[i]!= h_1[i] :
            x=x-1
      per=(x/64.0*100.0)
      return per



app = Flask(__name__)
@app.route('/test',methods=['GET','POST'])
def helloworld():
    return "Hello world"
@app.route('/',methods=['GET','POST'])
def hello():
   if request.json:

       mydata = request.json
       link_1 = mydata.get('link1')
       link_2 = mydata.get('link2')
       try:
         obj=sim(link_1,link_2)
         return jsonify(link1=link_1,link2=link_2,similarity=obj.check_sim(),percentage=str(obj.percentage()))
       except:
          return jsonify(error="Download Error")
  





if __name__ == '__main__':
    app.run()


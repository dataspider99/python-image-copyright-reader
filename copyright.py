from PIL import Image
import re, urllib
from StringIO import StringIO

regex = re.compile("<dc:rights>(.*)<\/dc:rights>")

def copy_right(imagepath):
    if imagepath.startswith("http"):
        image = urllib.urlopen(imagepath).read()
        with open("sample","w") as f:
            f.write(image)
        image = StringIO(image)
    else:
        image = imagepath
        
    img = Image.open(image)
    if not img.app.get('APP1'):
        return None
    else:
        copyright_string =  img.app.get('APP1')
        try:
            copyright_string = re.sub("[\r\n\s\t]","",copyright_string)
            copy_right = regex.findall(copyright_string)[0]
            CopyRight = re.sub("<.+?>","", copy_right).strip()
        except:
            return None
        return CopyRight

if __name__=="__main__":
    print copy_right("https://s-media-cache-ak0.pinimg.com/736x/88/db/1b/88db1bffd88699428128f174ffefd9fc.jpg")
                
            
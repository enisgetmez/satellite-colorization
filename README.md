# satellite-colorization
coloring old satellite images

![colorize](https://github.com/enisgetmez/satellite-colorization/blob/main/colorize.gif?raw=true)

## Install and Run

### step 1 :

    pip install -r requirements.txt
### step 2 :
Run cmd and enter the command:

    hostsman -i cbsproxy.ibb.gov.tr:127.0.0.1
### step 3 :
Download the relevant model from the url below and put it in the models folder:
https://code.naturkundemuseum.berlin/mediaspherefornature/colorize_iiif/blob/master/experimental/model/colorization_release_v2.caffemodel

### step 4 :
Enter the command :

    python main.py 

Now, when you log in to https://sehirharitasi.ibb.gov.tr/, the basemaps will show the tile layers produced by satellite-colorization

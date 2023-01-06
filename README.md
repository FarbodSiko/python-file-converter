# python-file-converter
do you ever think that what if I send my python project to someone who doesn't have python installed on their pc.

in this project i'am showing you a project that help you convert you .py file to .dmg file .

WHAT TO DO :
1- first of all download "py2app" library so that you can use it.
      you can download the library with the below's commands:
      for windows : pip install py2app
      for mac os : pip3 install py2app 
      for linux : python3 -m pip install py2app
2- after installing the library you should download the "setup.py" file and put it in the same directory with you main project.
3- and then put your projects name in the 4th line of the source code and replace it with "Example.py".
4- and finally your good to go and the last thing you need to do is to open up your IDE terminal ( remember that its better to do this part with the IDE terminal instead of using your pc CMD/terminal ) 
5- run this command to generate your .dmg file :
        python3 setup.py py2app
6- then you should wait for it to make the file and after that you can find your .dmg file in you computer.
        for example in Mac os 13.0 you can find you generated file next to your main project directory in a folder named "dist" 
7- run it and enjoy :D 

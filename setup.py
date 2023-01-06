from setuptools import setup 
'''
APP = ['Example.py']
OPTIONS = {
    'argv_emulation' : True,
}

setup( app=APP,options={ 'pyapp': OPTIONS}, setup_requires=['py2app'])
'''
setup(
    app=['Example.py'],
    setup_requires=["py2app"],
)
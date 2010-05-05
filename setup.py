from setuptools import setup # this is new

LONG_DESCRIPTION = '''A minimalist Python interface for the Gowalla API'''

CLASSIFIERS = [
                'Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Natural Language :: English',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Python Modules' 
              ]

KEYWORDS = 'gowalla rest simplejson wrapper social location'

setup(name='gowalla',
    version='1.0',
    description='Gowalla API wrapper',
    long_description=LONG_DESCRIPTION,
    author='Drew Yeaton',
    author_email='drew@sentineldesign.net',
    url='http://github.com/sentineldesign/python-gowalla/',
    download_url='http://pypi.python.org/pypi/gowalla/',
    packages=['gowalla'],    
    platforms = ['Platform Independent'],
    license = 'GPLv3',
    classifiers = CLASSIFIERS,
    keywords = KEYWORDS,
    requires = ['simplejson'],
)
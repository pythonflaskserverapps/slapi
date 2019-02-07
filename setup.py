from setuptools import setup
from slapi import read_string_from_file

setup(name='slapi',
      version='0.0.6',
      author='pythonflaskserverapps',
      author_email='pythonflaskserverapps@gmail.com',
      description='shadow lichess api',
      long_description=read_string_from_file("README.md", "Shadow lichess API."),
      long_description_content_type='text/markdown',
      license='MIT',
      keywords="shadow lichess api",
      url='https://github.com/pythonflaskserverapps/slapi',            
      packages=['slapi'],
      test_suite="travis_test",
      python_requires=">=3.6",
      install_requires=[        
        "urllib3[secure]==1.24.1",        
        "websocket-client==0.54.0"
      ],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",        
        "Programming Language :: Python :: 3.6"
      ],
      entry_points={
        'console_scripts': []
      },
      package_dir={
        'slapi': 'slapi'
      },
      include_package_data=False,
      zip_safe=False)


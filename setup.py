from setuptools import setup


setup(name='slapi',
      version='0.0.2',
      author='pythonflaskserverapps',
      author_email='pythonflaskserverapps@gmail.com',
      description='lichess shadow api',
      long_description='Lichess shadow API.',
      license='MIT',
      keywords="lichess shadow api",
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


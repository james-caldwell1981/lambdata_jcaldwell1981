from setuptools import setup
setup(
  name = 'lambdata_james_caldwell1981',
  version = '2.1',
  license='MIT',
  description = 'Data Science helper functions.',
  author = 'James Caldwell',
  author_email = 'james.caldwell.1981@gmail.com',
  url = 'https://github.com/james-caldwell1981/lambdata_jcaldwell1981',
  download_url = 'https://github.com/james-caldwell1981/lambdata_jcaldwell1981.git',
  keywords = ['James', 'Caldwell', 'lambdata'],
  install_requires=[
          'pandas',
          'sklearn',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
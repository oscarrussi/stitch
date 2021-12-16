from setuptools import setup

setup(name='tap-poke-api',
      version='0.0.1',
      description="Singer tap for pulling all data from tap poke-api",
      author='Oscar Andrés Russi Porras',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_poke_api'],
      install_requires=[
          'requests>=2.21.0',
          'singer-python>=2.1.4',
      ],
      entry_points='''
          [console_scripts]
          tap-poke-api=tap_poke_api:main
      ''',
      )

from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress'
    ]

setup(name='abomid',
      packages=find_packages(),
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = abomid:main
      """,
      )

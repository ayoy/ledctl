from setuptools import setup

setup(name='ledctl',
      version='0.1',
      description='Raspberry Pi RGB LED strip controller',
      url='http://github.com/ayoy/ledctl',
      author='Dominik Kapusta',
      author_email='dominik@kapusta.cc',
      license='MIT',
      packages=['ledctl'],
      install_requires=[
          'flask',
          'pigpio',
      ],
      zip_safe=False)

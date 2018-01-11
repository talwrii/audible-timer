import setuptools.command.test
import sys

try:
    # Setuptools entry point is slow.
    # If we have `festentrypoint` then use a fast entry point
    import fastentrypoints
except ImportError:
    sys.stdout.write('Not using fastentrypoints\n')
    pass

class ToxTest(setuptools.command.test.test):
    user_options = []

    def initialize_options(self):
        setuptools.command.test.test.initialize_options(self)

    def run_tests(self):
        import tox
        tox.cmdline()


import setuptools
import os

HERE = os.path.dirname(__file__)

setuptools.setup(
    name='audible-timer',
    version="0.1.0",
    author='Tal Wrii',
    author_email='talwrii@gmail.com',
    description='',
    license='GPLv3',
    keywords='',
    url='',
    packages=['audible_timer'],
    long_description='See https://github.com/talwrii/audible-timer',
    entry_points={
        'console_scripts': ['audible-timer=audible_timer.audible_timer:main']
    },
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"
    ],
    cmdclass = {'test': ToxTest},
    install_requires=[]
)

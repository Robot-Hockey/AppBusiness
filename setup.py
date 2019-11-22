from setuptools import setup, find_packages

setup (
    name = 'AppBusiness',
    author='Robot Hockey Team',
    url='https://github.com/Robot-Hockey/AppBusiness',
    download_url='https://github.com/Robot-Hockey/AppBusiness/archive/master.zip',
    version = '0.1',
    description = 'App to control business on the table.',
    license='GPL-v2',
    platforms=['Linux'],
    packages=find_packages(include=['app', 'app.*']),
    entry_points={
        'console_scripts': ['app-business=app.game:main']
    }
)

from distutils.core import setup, Extension

module1 = Extension('spi', sources = ['spi.c'])

setup (
    name = 'AppBusiness',
    author='Robot Hockey Team',
    url='https://github.com/Robot-Hockey/AppBusiness',
    download_url='https://github.com/Robot-Hockey/AppBusiness/archive/master.zip',
    version = '0.1',
    description = 'App to control business on the table.',
    license='GPL-v2',
    platforms=['Linux'],
    ext_modules = [module1]
)
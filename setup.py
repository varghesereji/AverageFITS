import setuptools


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='AverageFITS',
    version='1.0',
    author='Varghese Reji',
    author_email='varghesereji0007@gmail.com',
    description='Averaging fits files based on header keys',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/varghesereji/AverageFITS.git',
    license='GNU GPLv3',
    packeges=['AverageFITS'],
    install_requires=['astropy']
    )

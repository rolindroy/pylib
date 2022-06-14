import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='pylib',
    version='0.0.1',
    author='Rolind Roy',
    author_email='rolind.roy@test.com',
    description='Testing installation of Package',
    long_description="---------------------",
    long_description_content_type="text/markdown",
    url='https://github.com/rolindroy/pylib',
    license='MIT',
    packages=['pylib'],
    install_requires=['requests'],
)
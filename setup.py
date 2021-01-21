from setuptools import setup

setup(
    name='finalsa-services-connector',
    version='1.0.0',
    url='https://github.com/finalsa/finalsa-flask-models/',
    license='BSD',
    author='Luis Diego Jiménez Delgado',
    author_email='luis@finalsa.com',
    description='Handler for finalsa services',
    packages=['finalsa'],
    namespace_packages=['finalsa'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests',
    ],
    classifiers=[
    ]
)
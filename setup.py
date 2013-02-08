# coding: utf-8
"""
Create a Django Project from template + create virtualenv
"""
from setuptools import setup

setup(
    name="create_django_project",
    author="Florian Finke",
    author_email="flo@randomknowledge.org",
    version='0.0.1',
    packages=['create_django_project'],
    url='https://github.com/randomknowledge/create_django_project',
    include_package_data=True,
    license='MIT',
    description='',
    long_description=__doc__,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'create-django-project = create_django_project.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

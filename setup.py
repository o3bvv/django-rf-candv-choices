# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


__here__ = os.path.abspath(os.path.dirname(__file__))

REQUIREMENTS = [
    i.strip() for i in
    open(os.path.join(__here__, "requirements.txt")).readlines()
]

setup(
    name='django-rf-candv-choices',
    version='1.0.0',
    description="Support of django-candv-choices for django-rest-framework.",
    keywords=[
        'choices', 'constants', 'candv', 'values', 'Django', 'rest-framework',
    ],
    license='LGPLv3',
    url="https://github.com/oblalex/django-rf-candv-choices",
    author="Alexander Oblovatniy",
    author_email="oblovatniy@gmail.com",
    namespace_packages=[
        'candv_x',
        'candv_x.rest_framework',
    ],
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries",
    ],
    platforms=[
        'any',
    ],
)

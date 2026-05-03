from setuptools import setup

setup(
    name='wtforms',
    version='3.2.2',
    description='Form validation and rendering for Python web development.',
    maintainer='WTForms',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'markupsafe>=1.1.1',
    ],
    extras_require={
        'email': [
            'email-validator>=2.0',
        ],
    },
    packages=[
        'wtforms',
        'wtforms.csrf',
        'wtforms.fields',
        'wtforms.widgets',
    ],
    package_dir={'': 'src'},
    include_package_data=True,
)

from setuptools import setup

setup(
    name='FootballMatchdaySummarizer',
    version='1.0.0',
    description='Summarizes Football Match Days',
    install_requires=['python = 3',
                      'enaml',
                      'atom',
                      ],
    entry_points={'console_scripts': [
        'run = main:main',
    ]}
)

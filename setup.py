from setuptools import setup, find_packages

setup(
    name='FootballMatchdaySummarizer',
    version='1.0.0',
    description='Summarizes Football Match Days',
    install_requires=['enaml',
                      'atom',
                      ],
    packages=find_packages(),
    entry_points={'console_scripts': [
        'app_run = football_match_day_summarizer.main:main',
    ]}
)

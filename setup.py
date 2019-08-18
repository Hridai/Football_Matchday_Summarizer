from setuptools import setup, find_packages

setup(
    name='somethingrandom',
    version='1.0.0',
    description='Summarizes Football Match Days',
    install_requires=['enaml',
                      'atom',
                      'qtpy',
                      'pyqt5',
                      ],
    packages=find_packages(),
    entry_points={'console_scripts': [
        'app_run = football_matchday_summarizer.app:main',
    ]}
)

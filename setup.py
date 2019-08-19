from setuptools import setup, find_packages

setup(
    name='football_matchday_summarizer',
    version='1.0.0',
    description='Summarizes Football Match Days',
    install_requires=['enaml',
                      'atom',
                      'qtpy',
                      'pyqt5',
                      ],
    packages=find_packages(),
    package_data={'football_matchday_summarizer': ['*.enaml', '*.png']},
    entry_points={'console_scripts': [
        'run-app = football_matchday_summarizer.app:main',
    ]}
)

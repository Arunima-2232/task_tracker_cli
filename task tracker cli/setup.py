from setuptools import setup, find_packages

setup(name="task_tracker_cli",
      version="0.1",
      packages=find_packages(),
      entry_points={
          "console_scripts": [
              "mycli=task_tracker_cli.main:main",
          ],
      },
      )
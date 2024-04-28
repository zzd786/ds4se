import os
import subprocess

# Add the path to Maven's bin directory to the PATH environment variable
os.environ['PATH'] += os.pathsep + 'C:/ProgramData/chocolatey/lib/maven/apache-maven-3.9.6/bin'

# Now try running your command
subprocess.run(['mvn', 'clean', 'install'], check=True)

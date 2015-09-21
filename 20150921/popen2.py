__author__ = 'Henry Pan'

import subprocess

if __name__ == '__main__':
    print '\npopen2:'

    proc = subprocess.Popen(['cat', '-'],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            )

    stdout_value = proc.communicate('write to stdin, then read from it')[0]

    print stdout_value
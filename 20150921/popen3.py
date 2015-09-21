__author__ = 'Henry Pan'

import subprocess



### to watch streams for stdout and stderr
if __name__ == '__main__':

    print '\npopen3'
    proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
    stdout_value, stderr_value = proc.communicate('through stdin to stdout')
    print '\tpass through:', repr(stdout_value)
    print '\tstderr      :', repr(stderr_value)
__author__ = 'Henry Pan'

import subprocess

if __name__ == '__main__':
    # subprocess.call(['ls', '-lh'])
    # subprocess.call(['cat', 'README.md'])
    # output = subprocess.check_output(['ls', '-l'])
    # print output
    #
    # output = subprocess.check_output(
    #     'echo to stdout; echo to stderr 1>&2; exit 1',
    #     shell=True
    # )
    # print output

    # print '\nread:'
    # proc = subprocess.Popen(['echo', '"to stdout'], stdout=subprocess.PIPE)
    #
    # stdout_value = proc.communicate()[0]
    # print 'stdout:', repr(stdout_value)

    print '\nwrite:'

    proc = subprocess.Popen(['cat', '-'],
                            stdin=subprocess.PIPE,
                            )

    proc.communicate('Wonderland')




def check_os_info():
    import os 
    print(os.getpid())
    print(os.getcwd())
    print(os.getuid())
    print(os.getgid())

def subproc_sample():
    import subprocess
    ret = subprocess.getoutput('date')
    print(ret)

    ret = subprocess.getoutput('date -u')
    print(ret)

    ret = subprocess.getoutput('date -u | wc')
    print(ret)

    ret = subprocess.check_output(['date', '-u'])
    print(ret)

    # return states
    ret = subprocess.call('date')
    print(ret)

    # use shell or don't use shell
    ret = subprocess.call('date -u', shell=True)
    ret = subprocess.call(['date', '-u'])
    
if __name__ == "__main__":
    print("\t===check_os_info==")
    check_os_info()
    
    print("\t===subproc_sample==")
    subproc_sample()

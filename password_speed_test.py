import time
import operator
import getpass

pwds = []
pwd = 'nothing'
while pwd != '':
    pwd = raw_input('Enter a password or quit by entering nothing (press enter):')
    print pwd
    if pwd:
        pwds.append(pwd)
print 'got pwds:',pwds

pwd_times = {}    
for p in pwds:
    raw_input('press enter to continue')
    start_time = time.time()
    print 'start_time', start_time
    for i in range(5):
        p_input = ''
        while p_input != p:        
            p_input = getpass.getpass('Type '+p+' ')
            if p_input != p:
                print 'Doesn\'t match retype'
        elapsed = time.time() - start_time
    print p,elapsed
    pwd_times[p] = elapsed
            
sorted_pwds = sorted(pwd_times.items(), key=operator.itemgetter(1))

for sp in sorted_pwds:
    print sp

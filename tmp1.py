import os
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')

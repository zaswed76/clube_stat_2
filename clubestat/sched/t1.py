
from datetime import date, datetime

from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

def my_job(text):
    print(text)

# The job will be executed on November 6th, 2009
sched.add_job(my_job, 'date', run_date=datetime(2017, 12, 8, 20, 45, 0), args=['text'])

sched.start()
import os
import time
from datetime import datetime

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from exchanges.bitcoin import Bitfinex


def fetch_bitcon_price():
    current_price = Bitfinex().get_current_data()
    print(current_price)


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

executors = {
    'default': {'type': 'threadpool', 'max_workers': 5},
    'processpool': ProcessPoolExecutor(max_workers=3)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 2
}

if __name__ == '__main__':
    # scheduler = BackgroundScheduler()
    # scheduler.configure(
    #                 jobstores=jobstores,
    #                 executors=executors,
    #                 job_defaults=job_defaults)

    print(fetch_bitcon_price())

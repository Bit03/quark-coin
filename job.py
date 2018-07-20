import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from exchanges.bitcoin import Bitfinex


def fetch_bitcon_price():
    current_data = Bitfinex().get_current_data()
    print (current_data)
    return current_data


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///db.sqlite')
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
    scheduler = BlockingScheduler()
    scheduler.configure(
                    jobstores=jobstores,
                    executors=executors,
                    job_defaults=job_defaults)
    #
    # print(fetch_bitcon_price())

    scheduler.add_job(fetch_bitcon_price, 'interval', seconds=5, id='fetch_bitcon_job_id')
    #
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

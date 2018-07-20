import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from exchanges.bitcoin import Bitfinex
from influxdb import InfluxDBClient

client = InfluxDBClient('10.0.1.71', 8086, 'root', 'root', 'bitcoin')
client.create_database('bitcoin')


def fetch_bitcon_price():
    current_data = Bitfinex().get_current_data()
    json_body = [{
        "measurement": "btc_price_usd",
        "tags": {
            "provider": "bitfinex",
            "symbol": "btcusd",
        },
        "time": current_data.get("datetime"),
        "fields": {
            "last": float(current_data.get("last")),
            "bid": float(current_data.get("bid")),
            "ask": float(current_data.get("ask")),
        }
    }]
    client.write_points(json_body)


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
    scheduler.remove_job(job_id="fetch_bitcon_job_id")
    #
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

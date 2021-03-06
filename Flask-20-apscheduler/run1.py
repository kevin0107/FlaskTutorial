from flask import Flask
from flask_apscheduler import APScheduler


class Config(object):
    SCHEDULER_API_ENABLED = True


scheduler = APScheduler()


@scheduler.task('interval', id='do_job_1', seconds=30)
def job1():
    print('Job 1 executed')


# cron examples
@scheduler.task('cron', id='do_job_2', minute='*')
def job2():
    print('Job 2 executed')


@scheduler.task('cron', id='do_job_3', week='*', day_of_week='sun')
def job3():
    print('Job 3 executed')


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    scheduler.init_app(app)
    scheduler.start()

    app.run()
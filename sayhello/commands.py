import click
from sayhello import app, db
from sayhello.models import Message


@app.cli.command()
@click.option('--count', default=20, help='Quantity of message, default is 20.')
def forge(count):
    """Generate fake message"""
    from faker import Faker
    db.drop_all()
    db.create_all()

    fake = Faker('zh_CN')  # 创建用来生成虚拟数据到Faker实例
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Create %d fake message.' % count)


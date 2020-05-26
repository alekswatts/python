import sqlalchemy as sa



metadata = sa.MetaData()
connection = {'user': 'postgres', 'database': 'essdom', 'host': '51.15.214.33', 'password': 'POstgres123'}
dsn = 'postgresql://{user}:{password}@{host}/{database}'.format(**connection)


domain = sa.Table(
    'domains', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('domain', sa.String(255)),
    sa.Column('ip', sa.String(16)),
    sa.Column('content', sa.Text),
    sa.Column('title', sa.String(255)),
    sa.Column('dtype', sa.String(255)),
    sa.Column('company', sa.String(255)),
    sa.Column('affiliate', sa.Boolean),
    sa.Column('other', sa.String(255)),
    sa.Column('orderlinks', sa.Text),
    sa.Column('ordercontent', sa.Text)
)

if __name__ == '__main__':
    engine = sa.create_engine(dsn)
    metadata.create_all(engine)

import pdb
from db import sa, dsn, domain


engine = sa.create_engine(dsn)
conn = engine.connect()

all_domains = conn.execute(sa.select([domain.c.id, domain.c.domain]))

######################################

# good_domains = dict()

# for dom in all_domains:
#     print(dom.domain)
#     gdom = dom.domain[4:] if dom.domain.startswith('www.') else dom.domain
#     if gdom not in good_domains:
#         good_domains[gdom] = dom.id
#     else:
#         if good_domains[gdom] > dom.id:
#             good_domains[gdom] = dom.id

# all_domains_ids = set([d.id for d in conn.execute(sa.select([domain.c.id]))])
# good_domains_ids = set(good_domains.values())

# ######################################

# bad_domains = all_domains_ids - good_domains_ids
# print(len(bad_domains))
# pdb.set_trace()

# conn.execute(domain.delete().where(domain.c.id.in_(bad_domains)))

for dom in all_domains:
    if dom.domain.startswith('www.'):
        gdom = dom.domain[4:]
        conn.execute(domain.update().values(domain=gdom).where(domain.c.id == dom.id))
        print(dom.domain, gdom, dom.id)

print('All Done!')

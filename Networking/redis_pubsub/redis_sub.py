import redis
conn = redis.Redis()

topics = ['maine coon', 'persian']
sub = conn.pubsub()
sub.unsubscribe('maine coon')
sub.unsubscribe('persian')
# sub.subscribe(topics)
# for msg in sub.listen():
#     print(msg)
#     if msg['type'] == 'message':
#         cat = msg['channel']
#         hat = msg['data']
        # print('Subscribe: {0} wears a {1}'.format(cat, hat))
# sub.unsubscribe(topics)
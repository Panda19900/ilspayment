from flask import current_app
from google.cloud import datastore

testList = list

def init_app(app):
    pass

def getClient():
    return datastore.Client(current_app.config['PROJECT_ID'])

def fromDatastore(entity):
    if not entity:
        return None
    if isinstance(entity, testList):
        entity = entity.pop()

    entity['id'] = entity.key.id
    return entity

def viewList():
    ds = getClient()
    query = ds.query(kind='Test', order=['owner'])
    entities = testList(map(fromDatastore))
    return entities

def viewListByUser(user_id):
    ds = getClient()
    query = ds.query(
        kind='Test',
        filters=[
            ('owner_id', '=', user_id)
        ]
    )
    entities = testList(map(fromDatastore))
    return entities

def read(id):
    ds = getClient()
    key = ds.key('Test', int(id))
    results = ds.get(key)
    return fromDatastore(results)

def update(data, id=None):
    ds = getClient()
    if id:
        key = ds.key('Test', int(id))
    else:
        key = ds.key('Test')

    test_entity = datastore.Entity(
        key=key)

    test_entity.update(data)
    ds.put(test_entity)
    return fromDatastore(test_entity)

def delete(id):
    ds = getClient()
    key = ds.key('Test', int(id))
    ds.delete(key)

import pandas as pd

from ml import outlier, supervised
from supports.database import Transactions

from server import db

def data_frame(query, columns):
    def make_row(x):
        return dict([(c, getattr(x, c)) for c in columns])
    return pd.DataFrame([make_row(x) for x in query])

def transaction_to_df(trans):
    df = data_frame(trans, [
        'date_of_transction',
        'amount',
        'details',
        'uuid',
        'user_uuid',
        'location',
        'store_name'
    ])
    df = pd.concat([df, pd.get_dummies(df['location'])], axis=1)
    df = pd.concat([df, pd.get_dummies(df['store_name'])], axis=1)
    df = df.drop(['location', 'store_name', 'uuid', 'user_uuid', 'details', 'date_of_transction'], axis=1)
    return df

'''
def predict(transaction_id):
    transaction = Transactions.query.filter(Transactions.uuid == transaction_id)
    # df = pd.read_sql(transaction.statement, db.engine)
    transaction.details = vectorize.vectorize(
        transaction.details,
        transaction.user_uuid)
    less = reduce_dimensions(transaction)
    return outlier.predict(less, transaction.user_id)
'''

def predict(transaction_id):
    transaction = Transactions.query.filter(Transactions.uuid == transaction_id).limit(1)
    print('TRANSACTION')
    print(transaction)
    df = data_frame(transaction, )
    df = pd.read_sql(transaction.statement, db)
    df = pd.concat([df, pd.get_dummies(df['location'])], axis=1)
    df = pd.concat([df, pd.get_dummies(df['store_name'])], axis=1)
    df = df.drop(['location', 'store_name'], axis=1)

    return outlier.predict(df, transaction.fetch(1)[0].user_uuid)

'''
def initial_train(user_uuid):
    transactions = Transactions.query.filter(Transactions.user_uuid == user_uuid)
    # df = pd.read_sql(transactions.statement, db.engine)
    vectorize.train_model(
        [x.details for x in transactions],
        user_uuid)
    # transactions = vectorize.multi_vectorize(transactions)
    for t in range(len(transactions)):
        transactions[t].details = vectorize.vectorize(transactions[t].details.replace(' ','_'), user_uuid)
    outlier.train_model(transactions, user_uuid)

    return [
        predict(reduction_dimensions(x), user_uuid) for x in transactions
    ]
'''

def initial_train(user_uuid):
    print("Running an initial train")
    transactions = Transactions.query.filter(Transactions.user_uuid == user_uuid).all()
    '''
    df = data_frame(transactions, [
        'date_of_transction',
        'amount',
        'details',
        'uuid',
        'user_uuid',
        'location',
        'store_name'
    ])
    df = pd.concat([df, pd.get_dummies(df['location'])], axis=1)
    df = pd.concat([df, pd.get_dummies(df['store_name'])], axis=1)
    df = df.drop(['location', 'store_name', 'uuid', 'user_uuid', 'details', 'date_of_transction'], axis=1)
    '''
    df = transaction_to_df(transactions)
    outlier.train_model(df, user_uuid)
    return [
        outlier.predict(transaction_to_df([x]), user_uuid) for x in transactions
    ]

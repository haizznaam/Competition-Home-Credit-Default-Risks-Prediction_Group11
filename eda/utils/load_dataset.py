import pandas as pd
from datetime import datetime


def load_all_tables(path='',  progress=True):
    '''
    Function to load all the tables required

    Input:
        path: str, default = ''
            Path of directory where tables are stored in
        progress: bool, default = True
            Whether to display full loading progress.

    '''

    if progress:
        print('Loading all the tables...\n')
        time_start = datetime.now()

    # making all the table names variables global to be used all along the project
    global application_train, application_test, previous_application, \
        bureau, bureau_balance, credit_card_balance, installments_payments, POS_CASH_balance

    application_train = pd.read_csv(path + 'dseb63_application_train.csv')
    if progress:
        print("Loaded 1 table")

    application_test = pd.read_csv(path + 'dseb63_application_test.csv')
    if progress:
        print("Loaded 2 tables")

    previous_application = pd.read_csv(
        path + 'dseb63_previous_application.csv')
    if progress:
        print("Loaded 3 tables")

    bureau = pd.read_csv(path + 'dseb63_bureau.csv')
    if progress:
        print("Loaded 4 tables")

    bureau_balance = pd.read_csv(path + 'dseb63_bureau_balance.csv')
    if progress:
        print("Loaded 5 tables")

    credit_card_balance = pd.read_csv(path + 'dseb63_credit_card_balance.csv')
    if progress:
        print("Loaded 6 tables")

    installments_payments = pd.read_csv(
        path + 'dseb63_installments_payments.csv')
    if progress:
        print("Loaded 7 tables")

    POS_CASH_balance = pd.read_csv(path + 'dseb63_POS_CASH_balance.csv')
    if progress:
        print("Loaded 8 tables")
        print('\nComplete loaded 8 tables.')
        print('-' * 45)
        print(f'Dataset loaded time = {datetime.now() - time_start}')



import pandas as pd
from sqlalchemy import create_engine

from django.core.management.base import BaseCommand, CommandError
from dataset.models import Dataset

class Command(BaseCommand):
    help = 'Insert Dataset from csv to Database.'

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file_path",
                            help="dataset file path", required=True)
        parser.add_argument("-d", "--database_url",
                            help="database url", required=True)

    def handle(self, *args, **options):
        dataset_df = pd.read_csv(options.get('file_path'))
        engine = create_engine(options.get('database_url'))
        dataset_df.to_sql(Dataset.objects.model._meta.db_table, engine,
                          index=False, if_exists='append')
        print("Seeded suceccfully")

import os
import pandas as pd
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Process a CSV file and print basic analytics (row/column count, column names)'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Path to the CSV file to process')

    def handle(self, *args, **options):
        csv_path = options['csv_path']
        if not os.path.exists(csv_path):
            raise CommandError(f'File not found: {csv_path}')
        try:
            df = pd.read_csv(csv_path)
            # Check if DataFrame is empty or malformed
            if df.empty or df.shape[1] == 0:
                raise CommandError('Error processing file: No valid columns found')
            self.stdout.write(self.style.SUCCESS(f'Rows: {df.shape[0]}, Columns: {df.shape[1]}'))
            self.stdout.write(self.style.SUCCESS(f'Column names: {list(df.columns)}'))
        except (pd.errors.ParserError, pd.errors.EmptyDataError, UnicodeDecodeError) as e:
            raise CommandError(f'Error processing file: {e}')
        except Exception as e:
            raise CommandError(f'Error processing file: {e}')

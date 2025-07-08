from celery import shared_task
import time
import pandas as pd

@shared_task
def sample_long_task(x, y):
    time.sleep(5)  # Simulate a long-running task
    return x + y

@shared_task
def process_uploaded_file(file_path):
    try:
        df = pd.read_csv(file_path)
        # Example: count rows and columns
        result = {
            'rows': df.shape[0],
            'columns': df.shape[1],
            'columns_names': list(df.columns),
        }
        # Optionally, save result to DB or file
        return result
    except Exception as e:
        return {'error': str(e)}

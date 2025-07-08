import os
import tempfile
import pandas as pd
import pytest
from django.core.management import call_command
from django.core.management.base import CommandError

@pytest.mark.django_db
def test_process_csv_command_success(capsys):
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False) as tmp:
        df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        df.to_csv(tmp.name, index=False)
        tmp_path = tmp.name
    try:
        call_command('process_csv', tmp_path)
        captured = capsys.readouterr()
        assert 'Rows: 2, Columns: 2' in captured.out
        assert 'Column names: [\'a\', \'b\']' in captured.out
    finally:
        os.remove(tmp_path)

@pytest.mark.django_db
def test_process_csv_command_file_not_found():
    with pytest.raises(CommandError) as exc:
        call_command('process_csv', '/nonexistent/file.csv')
    assert 'File not found' in str(exc.value)

@pytest.mark.django_db
def test_process_csv_command_invalid_csv(tmp_path):
    # Create a file that is not a valid CSV
    file_path = tmp_path / 'bad.csv'
    file_path.write_text('this is not a csv at all')
    with pytest.raises(CommandError) as exc:
        call_command('process_csv', str(file_path))
    assert 'Error processing file' in str(exc.value)

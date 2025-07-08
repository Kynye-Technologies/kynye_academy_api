import pytest
from apps.analytics.tasks import sample_long_task

@pytest.mark.django_db
def test_sample_long_task():
    result = sample_long_task.apply(args=(2, 3)).get()
    assert result == 5

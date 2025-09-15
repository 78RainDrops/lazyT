import lazy_task.lazy as lazy
import pytest

@pytest.fixture
def sample_tasks():
    return [
        {"id": "1", "description": "Buy milk", "status": "todo", "createdAt": "2025-01-01 | 10:00", "updateAt": "2025-01-01 | 10:00"},
        {"id": "2", "description": "Do laundry", "status": "in-progress", "createdAt": "2025-01-01 | 11:00", "updateAt": "2025-01-01 | 11:00"},
    ]

@pytest.fixture
def mock_save_load(monkeypatch):
    store = []
    
    def fake_save(tasks):
        store.clear()
        store.extend(tasks)

    def fake_load():
        return list(store)

    monkeypatch.setattr(lazy.save_task, 'save', fake_save)
    monkeypatch.setattr(lazy.save_task, 'load', fake_load)
    return lambda: store

def test_initializer_task_empty(monkeypatch):
    monkeypatch.setattr(lazy.save_task, 'load', lambda: [])
    task_list, task_id, status = lazy.initialize_task()
    assert task_list == []
    assert task_id == 0
    assert status == ("todo", "in-progress", "done")

def test_add_task_increment_id(mock_save_load):
    storage = mock_save_load()
    task_list, task_id, status = [], 0, ("todo", "in-progress", "done")
    
    task_list = lazy.add_task("Test task", task_list, task_id, status)
    
    assert len(task_list) == 1
    assert task_list[0]['id'] == "1"
    assert task_list[0]['status'] == "todo"
    assert storage[0]['description'] == "Test task"

def test_edit_task_updates_description_and_time(sample_tasks, mock_save_load):
    storage = mock_save_load()
    lazy.save_task.save(sample_tasks)  # seed fake storage
    lazy.edit_task("1", "Buy chocolate milk", sample_tasks)

    edited = storage[0]
    assert edited["description"] == "Buy chocolate milk"
    assert edited["updateAt"] != "2025-01-01 | 10:00"

def test_done_task_changes_status(sample_tasks, mock_save_load):
    storage = mock_save_load()
    lazy.save_task.save(sample_tasks)
    lazy.done_task('2', 'done', sample_tasks)
    
    updated = storage[1]
    assert updated['status'] == 'done'
    assert updated['updateAt'] != "2025-01-01 | 10:00"

def test_delete_task_remove_from_list(sample_tasks, mock_save_load):
    storage = mock_save_load()
    lazy.save_task.save(sample_tasks)
    
    new_list = lazy.delete_task("1", sample_tasks)
    assert len(new_list) == 1
    assert new_list[0]['id'] == '2'
    assert storage[0]['id'] == '2'

def test_show_task_filters_by_status(capsys, sample_tasks):
    lazy.show_task(sample_tasks, status='in-progress')
    captured = capsys.readouterr()
    assert "Do laundry" in captured.out
    assert "Buy milk" not in captured.out

def test_show_task_no_result(capsys):
    lazy.show_task([], status='done')
    captured = capsys.readouterr()
    assert "No Task found" in captured.out

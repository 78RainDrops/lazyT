import json, os
from pathlib import Path

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = Path.home()/'.lazyT_tasks.json'
# path = os.path.join(BASE_DIR, "task.json")

def save(task_list):
    task_dict = {'task_list' : task_list}
    # with open(path, 'w')as f:
    #     json.dump(task_dict, f, indent=4)
    path.write_text(json.dumps(task_dict, indent=4))
        
def load():
    if not path.exists():
        path.write_text(json.dumps({"task_list": []}, indent=4))
    
    data = json.loads(path.read_text())
    
    return data.get('task_list', [])
    # print(data)


# for i, tsk in enumerate(task_list):
#     if tsk['id'] == "3":
#         task_list.pop(i)
#         print("Delete Successfully.")

#     save(task_list)
import argparse
from datetime import datetime
from . import save_task

def initialize_task():
    task_list = save_task.load()
    task_id = int(max(tsk['id'] for tsk in task_list) if task_list else 0)
    status = ('todo', 'in-progress', 'done')
    return task_list, task_id, status

def add_task(task,task_list, task_id, status):
    task_id += 1
    now = get_time()

    task = {
        'id' : str(task_id),
        'description' : task,
        'status' : status[0],
        'createdAt' : now,
        'updateAt' : now,
    }

    task_list.append(task)
    save_task.save(task_list)
    print("Task successfully added.")
    return task_list

def edit_task(task_id, new_task, task_list):
    for tsk in task_list:
        if tsk['id'] == str(task_id):
            tsk['description'] = new_task
            save_task.save(task_list)
            print("Task edited successfully")

def done_task(task_id,status,task_list):
    for tsk in task_list:
        if tsk['id'] == str(task_id):
            tsk['status'] = status
            save_task.save(task_list)
            print(f'Task updated to: {status}')

def show_task(task_list, status=None):
    filtered = [tsk for tsk in task_list if(status is None or tsk['status'] == status)]

    print(f"{'ID':<5} {'TASK':<20} {'STATUS':<8} {'CREATED':<20} {'UPDATED':<20}")
    print("-"*69)

    for tsk in filtered:
        print(f"{tsk['id']:<5} {tsk['description']:<20} {tsk['status']:<8} {tsk['createdAt']:<20} {tsk['updateAt']:<20}")
    
    if not filtered:
        print("No Task found")

def delete_task(task_id,task_list):
    print(f"Deleting task id {task_id}")
    task_list = list(filter(lambda t: t['id'] != str(task_id), task_list))
    save_task.save(task_list)
    return task_list

def get_time():
    now = datetime.now().strftime('%Y-%m-%d | %H:%M')
    return now


def main():
    task_list, task_id, status = initialize_task()
    
    parser = argparse.ArgumentParser(
        description="A todo list cli app"
    )
    subparser = parser.add_subparsers(dest='command')
    
    add_parser = subparser.add_parser('add', help='Add a new task.')
    add_parser.add_argument('task', help='Task Description')
    
    list_parser = subparser.add_parser('list', help='List all task')
    list_parser.add_argument('-s', '--status', choices=['done', 'in-progress', 'todo'], help='Filter task by status')
    
    update_parser = subparser.add_parser('edit', help='edit task decription')
    update_parser.add_argument('id', help='task id to edit')
    update_parser.add_argument('task', help='edited task')
        
    task_parser = subparser.add_parser('task', help='Change from todo to in-progress or done')
    task_parser.add_argument('id', help='Task id')
    task_parser.add_argument('-s','--status', choices=['done', 'in-progress', 'todo'], help='Status of the task')
    
    del_parser = subparser.add_parser('del', help='Delete a task')
    del_parser.add_argument('id', help='id of the task to delete')
    
    args = parser.parse_args()
    if args.command == "add":
        add_task(args.task,task_list,task_id,status)
    elif args.command == "list":
        if args.status:
            print(f"Filtered task (status = {args.status}):\n")
            show_task(task_list, args.status)
        else:
            print('All tasks:\n')
            show_task(task_list)
    elif args.command == "edit":
        edit_task(args.id, args.task, task_list)
    elif args.command == "task":
        done_task(args.id, args.status, task_list)
    elif args.command == "del":
        delete_task(args.id, task_list)
    else:
        parser.print_help()

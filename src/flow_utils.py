import time

from src.openai_assistants_api.message import MessageClient
from src.openai_assistants_api.run import RunClient
from src.openai_assistants_api.thread import ThreadClient


def wait_run_completed(thread_id, run_id, interval_seconds=10, timeout_seconds=60):
    run_client = RunClient()
    while True:
        run = run_client.retrieve(thread_id, run_id)
        if run['completed_at'] != None:
            return run
        elif timeout_seconds <= 0:
            print('timeout exceeded, cancelling run..')
            _ = run_client.cancel(run_id=run_id)
        print('waiting for run to complete..')
        time.sleep(interval_seconds)
        
        
def get_assistant_completion(assistant_id, message, thread_id=None, ephemeral_thread=False):
    thread_client = ThreadClient()
    message_client = MessageClient()
    run_client = RunClient()  
    
    if thread_id is None:        
        print('creating thread..')
        thread = thread_client.create()
        thread_id = thread['id']   
    
    print('creating message..')
    _ = message_client.create(thread_id, 'user', message)
    
    print('creating run..')
    created_run = run_client.create(thread_id, assistant_id)
    
    _ = wait_run_completed(thread_id, created_run['id'])
    
    messages = message_client.get_list(thread_id)
    
    if ephemeral_thread:
        print('deleting thread..')
        _ = thread_client.delete(thread_id)
        
    return messages[0]['content'][0]['text']['value']

    
# Multi Thread File Find
A modular ready-to-use cross-platform Python file finder. Multi-threaded and recursive available.

## Usage
```python
from mtff import mtff

multi_thread_file_find = mtff()

results = multi_thread_file_find.search_file("targetfile.mp3")

results = multi_thread_file_find.search_file("targetfile.mp3", threads=4)

results = multi_thread_file_find.search_file("targetfile.mp3", recursive=True)
```
Output (results):
```
['file_full_path/targetfile.mp3']
```
## Definitions
```python
def search_file(self, file_name, extension="", threads=None, *, target_path="", recursive=False):
```
■ Path propriorities:
    1. target_path argument
    2. path in file_name
    3. current path
■ Extension propriorities:
    1. extension argument
    2. file_name argument (unchanged)
■ Threads
    1. if not given: threads count will be the number of CPU cores
    2. if 1: will use main (current) thread
    3. if files around are less than thread number: will use main (current) thread
■ Set recursive to True to recursively search all folders below
■ Tries to clean up RAM after the job
■ Default is multi-threaded non-recursive

will write more documentation later
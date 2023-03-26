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
■ Path propriorities:*same paragraph*
    1. target_path argument*same paragraph*
    2. path in file_name*same paragraph*
    3. current path*same paragraph*
■ Extension propriorities:*same paragraph*
    1. extension argument*same paragraph*
    2. file_name argument (unchanged)*same paragraph*
■ Threads*same paragraph*
    1. if not given: threads count will be the number of CPU cores*same paragraph*
    2. if 1: will use main (current) thread*same paragraph*
    3. if files around are less than thread number: will use main (current) thread*same paragraph*
■ Set recursive to True to recursively search all folders below*same paragraph*
■ Tries to clean up RAM after the job*same paragraph*
■ Default is multi-threaded non-recursive*same paragraph*

will write more documentation later

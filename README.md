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
<br/>
■ Path priorities:<br/>
1. target_path argument<br/>
2. path in file_name<br/>
3. current path<br>
■ Extension priorities:<br/>
1. extension argument<br/>
2. file_name argument (unchanged)<br/>
■ Threads<br/>
1. if not given: threads count will be the number of CPU cores<br/>
2. if 1: will use main (current) thread<br/>
3. if files around are less than thread number: will use main (current) thread<br/>
■ Set recursive to True to recursively search all folders below<br/>
■ Tries to clean up RAM after the job<br/>
■ Default is multi-threaded non-recursive<br/>
<br/>
will write more documentation later<br/>

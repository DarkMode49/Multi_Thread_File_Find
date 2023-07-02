# Multi Thread File Find
A modular ready-to-use cross-platform Python file finder. Multi-threaded and recursive available.

## Usage
```python
from mtff import mtff

multi_thread_file_find = mtff()

# Recursive search with multi-thread on current path
results = multi_thread_file_find.search_file("targetfile.mp3")

# Recursive search with 4 threads on current path
results = multi_thread_file_find.search_file("targetfile.mp3", threads=4)

# Search with multi-thread on current path only
results = multi_thread_file_find.search_file("targetfile.mp3", recursive=False)
```
Output (results):
```
['file_full_path/targetfile.mp3']
```

<ul>
  <li type="none">
    <img src="https://cdn-icons-png.flaticon.com/512/2809/2809229.png" raw=true style="width: 30px;height: 30px;" />
    <span>mtff</span>
    <details open>
      <summary></summary>
      <ul>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/3199/3199560.png" raw=true style="width: 30px;height: 30px;" />
          <span>__init__</span>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/1827/1827800.png" raw=true style="width: 30px;height: 30px;" />
          <span>found</span>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/1827/1827800.png" raw=true style="width: 30px;height: 30px;" />
          <span>all_files</span>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/1827/1827800.png" raw=true style="width: 30px;height: 30px;" />
          <span>target</span>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/3199/3199560.png" raw=true style="width: 30px;height: 30px;" />
          <span>_search_file</span>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/3199/3199560.png" raw=true style="width: 30px;height: 30px;" />
          <a href="https://github.com/DarkMode49/Multi_Thread_File_Find#search_file">search_file</span>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/3199/3199560.png" raw=true style="width: 30px;height: 30px;" />
          <span>free_mem</span>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/3199/3199560.png" raw=true style="width: 30px;height: 30px;" />
          <a href="https://github.com/DarkMode49/Multi_Thread_File_Find#find_all_files-static">find_all_files</a>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/3199/3199560.png" raw=true style="width: 30px;height: 30px;" />
          <a href="https://github.com/DarkMode49/Multi_Thread_File_Find#replace_extension-static">replace_extension</a>
        </li>
        <li type="none">
          <img src="https://cdn-icons-png.flaticon.com/512/3199/3199560.png" raw=true style="width: 30px;height: 30px;" />
          <a href="https://github.com/DarkMode49/Multi_Thread_File_Find#dist_offsets-static">dist_offsets</a>
        </li>
      </ul>
    </details>
  </li>
</ul>
## 📖 Definitions

### search_file
The main method that is used for the search

#### Syntax
```python
search_file(file_name, extension="", *, threads=None, target_path="", recursive=True)
```
#### Parameters
<ul>
  <li>file_name: File name with or without path. Required</li>
  <li>extension(""): Target extension</li>
  <li>threads(None): Number of threads as an integer number</li>
  <li>target_path(""): Target path for search. Parents ignored</li>
  <li>recursive(True): True to search all nested folders, False for only current path/folder. Parents ignored</li>
</ul>

#### Return Value
List containing the file with full path.<br/>
Empty if not found.

#### Notes
Requires all functionality in mtff class.<br/>
Notice that extension, threads, target_path and recursive parameters are optional.<br/>
Consider you gave a "full file name with extension" to search along with different a "extension" argument.<br/>
How final file name is decided? Look for priorities below:<br/>
<ul>
  <li>Path priorities:
    <ol type="1">
      <li>target_path argument</li>
      <li>path in file_name</li>
      <li>current path</li>
    </ol>
  </li>
  <li>Extension priorities:
    <ol type="1">
      <li>extension argument</li>
      <li>file_name argument (not changed)</li>
    </ol>
  </li>
  <li>Threads:
    <ol type="1">
      <li>threads argument</li>
      <li>the number of CPU cores</li>
    </ol>
  </li>
</ul>
If threads count is 1, will use main (current) thread.<br/>
If files around are less than thread number, will use main (current) thread.<br/>
Will clean up RAM off of object variables<br/>
Default is multi-threaded recursive<br/>
<br/>

### find_all_files (Static)
Finds list of all files recursive or non-recursive

#### Syntax
```python
find_all_files(path, recursive=False)
```

#### Parameters
<ul>
  <li>path: The path of folder</li>
  <li>recursive(False): True to get all files in nested folders, False for only current path/folder</li>
</ul>

#### Return Value
List of all files found in folder or folders.

#### Notes
Will cause MemoryError if there were too many files.

### replace_extension (Static)
Replaces the extension of a file name that already has an extension.

#### Syntax
```python
replace_extension(file_name, extension)
```

#### Parameters
<ul>
  <li>file_name: File name with or without extension</li>
  <li>extension: String extension to append at end of file_name with or without dot</li>
</ul>

#### Return Value
File name with given extension replaced with old extension.

#### Example
```python
replace_extension("file.txt", "mp3") # -> file.mp3
replace_extension("file.txt", ".docx") # -> file.docx
replace_extension("file", ".docx") # -> file.docx
replace_extension("file.", ".docx") # -> file.docx
```

### dist_offsets (Static)
Is used to divide a list/array into equal parts. This method calculates the boundaries for each part of divison. The boundaries can be used to safely extract a part out of the list/iterable.
<br/>⚠️Warning: this function has bugs

#### Syntax
```python
dist_offsets(length, parts)
```

#### Parameters
<ul>
  <li>length: Length of list/iterable in integer</li>
  <li>parts: Number of parts to divide into in integer</li>
</ul>

#### Return Value
List containing lists. Each list represents a part and has two index integers as start and end.

#### Example
```python
dist_offsets(8, 2) # -> [[0, 4], [5, 7]]
dist_offsets(10, 3) # -> [[0, 3], [4, 6], [7, 9]]
dist_offsets(500, 2) # -> [[0, 250], [251, 499]]
```

# Change Log
## 2023-06-24
### Added
<ul>
  <li>Added some comments</li>
  <li>New static methods: find_all_files, replace_extension</li>
  <li>New methods: free_mem</li>
  <li>More documentation</li>
</ul>

### Changed
<ul>
  <li>Syntax improved</li>
  <li>Modularity increased</li>
  <li>search_file optimized</li>
  <li>Search is now recursive by default</li>
  <li>search_file method "threads" parameter is now keyword-only</li>
</ul>

### Fixed
<ul>
  <li>File not found if all files scan only found one file</li>
</ul>

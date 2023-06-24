from threading import Thread
from os.path import dirname, splitext
from os.path import basename, join, isfile
from os import getcwd, walk, listdir
from multiprocessing import cpu_count
from math import floor


class mtff():
    def __init__(self) -> None:
        self.found = []
        self.all_files = tuple()
        self.target = ""
    
    
    def _search_file(self, start_index, end_index):
        _all_files = tuple()
        if end_index > 0:
            _all_files = self.all_files[start_index:end_index]
        else:
            _all_files = self.all_files

        for filename in _all_files:
            if basename(filename) == self.target:
                self.found.append(filename)
    

    def search_file(self, file_name, extension="", *, threads=None, target_path="", recursive=True) -> list:
        _path = ""
        if not target_path:
            # Check for path in file_name
            _path = dirname(file_name)
        
        if _path:
            # file_name has path
            # file name is extracted here
            file_name = basename(file_name)
        
        if target_path:
            _path = target_path
        
        if not _path:
            # Last priority
            # get current path
            _path = getcwd()
        
        if extension:
            file_name = mtff.replace_extension(file_name, extension)
        
        self.all_files = mtff.find_all_files(_path, recursive)
        
        if not threads:
            threads = cpu_count()
        
        if threads < 1:
            raise ValueError(
                "Thread count argument {0} not acceptable".format(threads))

        all_files_count = len(self.all_files)

        # Return empty if there are no
        # files to search
        if not all_files_count:
            return []
        
        if self.found:
            self.found = []
        self.target = file_name
        
        # Go single thread if files are less than threads
        if threads == 1 or all_files_count <= threads:
            self._search_file(0, all_files_count - 1)

            _f = self.found
            # Free the RAM
            self.free_mem()
            return _f
        
        bounds = mtff.dist_offsets(all_files_count, threads)

        all_threads = []
        threads -= 1
        while threads > -1:
            new_thread = Thread(target=self._search_file, args=(
                *bounds[threads],
            ))
            new_thread.start()

            all_threads.append(new_thread)
            threads -= 1
        
        # Wait for threads to end
        for th in all_threads:
            th.join()
        
        _f = self.found
        self.free_mem()
        return _f
    

    def free_mem(self):
        self.all_files = []
        self.found = []
    

    @staticmethod
    def find_all_files(path, recursive=False) -> tuple:
        all_files = []

        if recursive:
            for dir_path, _, file_names in walk(path):
                for filename in file_names:
                    all_files.append(join(dir_path, filename))
                    #? MemoryError if too many
        else:
            all_files = [join(path, filename) for filename in listdir(path) if isfile(filename)]
        
        return tuple(all_files)


    @staticmethod
    def replace_extension(file_name, extension) -> str:
        name, _ = splitext(file_name)
        
        return name + '' if extension[0] == '.' else '.' + extension


    @staticmethod
    def dist_offsets(length, parts) -> list:
        p = floor(length / parts)
        r = 0
        offsets = []

        for _ in range(parts):
            offsets.append([r, r + p])
            r += p
        
        offsets = [[x + 1, y] for x, y in offsets]
        offsets[0][0] = 0
        offsets[-1][1] = length - 1
        return offsets

from threading import Thread
from os.path import dirname, splitext
from os.path import basename, join, isfile
from os import getcwd, walk, listdir
from multiprocessing import cpu_count
from math import floor


class mtff():
    def __init__(self) -> None:
        self.found = []
        self.all_files = []
    
    
    def _search_file(self, start_index, end_index, target):

        for filename in self.all_files[start_index:end_index]:
            if basename(filename) == target:
                self.found.append(filename)


    def search_file(self, file_name, extension="", threads=None, *, target_path="", recursive=False):
        if not target_path:
            _path = dirname(file_name)
        
        if _path:
            file_name = basename(file_name)
        
        if not _path:
            _path = getcwd()
        
        if extension:
            file_name = "{0}{1}{2}".format(
                splitext(file_name)[0],
                '.' if '.' not in extension else '',
                extension
            )

        
        if recursive:
            for dir_path, _, file_names in walk(_path):
                for filename in file_names:
                    self.all_files.append(join(dir_path, filename))
                    #? MemoryError if too many
        else:
            self.all_files = [join(_path, filename) for filename in listdir(_path) if isfile(filename)]
        
        
        if not threads:
            threads = cpu_count()
        
        if threads < 1:
            raise ValueError(
                "Thread count argument {0} not acceptable".format(threads))

        if threads == 1:
            self._search_file(0, len(self.all_files) - 1, file_name)

            self.all_files = []
            _f = self.found
            self.found = []
            return _f
        

        all_files_count = len(self.all_files)
        if all_files_count and all_files_count <= threads:
            self._search_file(self.all_files, file_name)

            self.all_files = []
            _f = self.found
            self.found = []
            return _f
        
        if not all_files_count:
            return []

        bounds = mtff.dist_offsets(all_files_count, threads)

        if self.found:
            self.found = []

        all_threads = []
        threads -= 1
        while threads > -1:
            new_thread = Thread(target=self._search_file, args=(
                *bounds[threads],
                file_name
            ))
            new_thread.start()

            all_threads.append(new_thread)
            threads -= 1
        
        for th in all_threads:
            th.join()
        
        self.all_files = []
        _f = self.found
        self.found = []
        return _f
    

    @staticmethod
    def dist_offsets(length, parts):
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

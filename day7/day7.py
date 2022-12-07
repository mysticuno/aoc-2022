class File:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name

    def __repr__(self):
        return f'File {self.name} size={self.size}'
    
class Folder(File):
    
    def __init__(self, name):
        super().__init__(name)
        self.files = {}
    
    def add_file(self, file):
        self.files[file.get_name()] = file
        if isinstance(file, Folder):
            # add self as parent to child dir
            file.get_files()['..'] = self
        
    def get_files(self):
        return self.files
    
    def get_size(self, unders=None):
        if unders is None:
            unders = []
        size = 0
        for filename in self.files:
            if filename == '..':
                continue # ignore parent dir
            file = self.files[filename]
            if isinstance(file, Folder):
                size += file.get_size(unders)[0] # size only
            else:
                size += file.get_size()
        if size < 100000:
            unders.append((self, size))
        return size, unders
    
    def __repr__(self):
        return f'dir {self.name}'


with open('input.txt') as f:
    root = Folder('/')
    parent = None
    current = root
    f.readline() # skip first line
    
    for line in f.readlines():
        contents = line.strip().split(" ")
        if contents[0] == '$':
            # command
            cmd = contents[1]
            if cmd == 'cd':
                name = contents[2]
                parent = current
                current = current.files.get(name)                
        elif contents[0] == 'dir':
            name = contents[1]
            folder = Folder(name)
            current.add_file(folder)
        else: # file
            size, name = contents
            file = File(name, int(size))
            current.add_file(file)

    size, dirs_under_100 = root.get_size()
    print(f"Sum {sum(map(lambda x: x[1], dirs_under_100))}")

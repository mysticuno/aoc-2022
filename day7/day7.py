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
        self.under_100k = 0
    
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
        print(f"Getting size for files in {self.name}")
        for filename in self.files:
            if filename == '..':
                continue # ignore parent dir
            file = self.files[filename]
            print(f"Getting size for {file}")
            if isinstance(file, Folder):
                size += file.get_size(unders)
            else:
                size += file.get_size()
        if size < 100000:
            unders.append((self, size))
        print(f"Dir {self.name} total size {size}")
        print(f"unders {unders} sum {sum(map(lambda x: x[1], unders))}")
        return size
    
    def __repr__(self):
        return f'dir {self.name}'


with open('input.txt') as f:
    # $ commands: cd [dir] or ls
    # dir [name] dirname
    # num [name] filename
    # parse commands
    # build directories and maintain sums
    # current_dir and parent_dir
    # is_listing = False
    # directories = {"/": {"..": None}} # assume starting in '/'
    # pwd = directories["/"]
    root = Folder('/')
    parent = None
    current = root
    print(f.readline()) # skip first line
    
    for line in f.readlines():
        print(line, end="")
        contents = line.strip().split(" ")
        if contents[0] == '$':
            # command
            cmd = contents[1]
            if cmd == 'cd':
                print(f'current: {current} parent: {parent}')
                name = contents[2]
                # if name == '..':
                #     current = parent
                # else:
                parent = current
                current = current.files.get(name)
                print(f'AFter CD: current: {current} parent: {parent}')
                
            elif cmd == 'ls':
                # is_listing = True
                continue # will begin listing
        elif contents[0] == 'dir':
            name = contents[1]
            folder = Folder(name)
            current.add_file(folder)
        else: # file
            size, name = contents
            file = File(name, int(size))
            current.add_file(file)
    print(root.get_size())

import os


class ProjectManager:
    def __init__(self):
        self.name = ''
        self.path = ''
        self.path_logs = ''
        self.path_image = ''

    def creation(self, name):
        self.name = name
        self.path = os.path.join(r'RTV_redactor/projects', self.name)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        else:
            return False
        self.path_logs = os.path.join(self.path, 'logs.txt')
        self.path_image = os.path.join(self.path, 'image.png')
        open(self.path_logs, 'a').close()
        return True

    def loading(self, name):
        self.name = name
        self.path = os.path.join(r'RTV_redactor/projects', self.name)
        if not os.path.exists(self.path):
            print('No such projects!!!')
            return False
        self.path_logs = os.path.join(self.path, 'logs.txt')
        self.path_image = os.path.join(self.path, 'image.png')
        return True

    def update_logs(self, node):
        with open(self.path_logs, 'a') as logs:
            logs.write(node + '\n')

    def delete_last_node(self):
        with open(self.path_logs, 'r') as f:
            lines = f.readlines()
        with open(self.path_logs, 'w') as f:
            for i in range(len(lines) - 1):
                f.write(lines[i])

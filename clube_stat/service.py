import getpass
import yaml


def get_pass():
    # return getpass.getpass(prompt='введите пароль: ')
    return input("введите пароль _ ")

def get_log():
    return input("введите логин _ ")

def save(path, data):
    with open(path, 'w') as outfile:
        yaml.dump(data, outfile, indent=4, width=0)

def load(path):
    with open(path, "r") as f:
        return yaml.load(f)

if __name__ == '__main__':
    from clubestat import pth
    cfg_pth = pth.CONFIG_PATH
    d = {"user": "login", "pwd": "pass", "www": [[1, 2, 3],[1, 2, 3] ]}
    save(cfg_pth, d)
    print(load(cfg_pth))
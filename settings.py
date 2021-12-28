OS_RELEASE = '/etc/os-release'
pretty_name = 'PRETTY_NAME='


with open(OS_RELEASE) as file:
    for line in file:
        if line.startswith(pretty_name):
            PATH_ENVIRONMENTS = line.split(pretty_name)[1].strip().replace(' ', '_')
            break

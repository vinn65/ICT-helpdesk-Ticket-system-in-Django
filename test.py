# list_packages.py
import pkg_resources

# List all installed packages and their versions
installed_packages = pkg_resources.working_set
sorted_packages = sorted(["{}=={}".format(i.key, i.version) for i in installed_packages])

# Write to a requirements.txt file
with open('requirements.txt', 'w') as f:
    for package in sorted_packages:
        f.write(package + '\n')

print("Installed packages listed in requirements.txt")

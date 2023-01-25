# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)

__metaclass__ = type

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """

    def filters(self):
        return {
            'security_drivers': self.security_drivers,
            'cgroup_controllers': self.cgroup_controllers,
        }

    def security_drivers(self, data, default=["selinux", "apparmor"]):
        """
        """
        display.v(f"security_drivers({data}, {default}")

        result = False

        if isinstance(data, list):
            for d in data:
                if d in default:
                    result = True

        display.v(f"= {result}")

        return result

    def cgroup_controllers(self, data):
        """
        """
        display.v(f"security_drivers({data}")

        default = ["cpu", "devices", "memory", "blkio", "cpuset", "cpuacct"]
        result = []

        if isinstance(data, list):
            for d in data:
                if d in default:
                    result.append(d)

        display.v(f"= {result}")

        return result

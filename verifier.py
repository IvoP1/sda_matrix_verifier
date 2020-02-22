import sys
import re
import urllib3
from collections import defaultdict
import pandas as pd
from dnacentersdk import api


urllib3.disable_warnings()


def matrix_builder(dna_version):
    '''
    Builds a dictionary from the online matrix for a given version

        Args:
            dna_version (str): version of DNAC

        Returns:
            dict: {"Hardware" : ["Compatible versions"]}
    '''


    url = r'https://www.cisco.com/c/en/us/solutions/enterprise-networks/software-defined-access/compatibility-matrix.html'
    tables = pd.read_html(url)

    # Select table of release train 1.3.X  or 1.2.X
    if(dna_version > "1.3"):
        compatibility_table = tables[0]
    else:
        compatibility_table = tables[2]

    # Select column of desired release
    for columns in compatibility_table.columns:
        if dna_version in columns:
            column_name = columns
        else:
            pass

    compatibility_dict = defaultdict(list)

    # Creates dictionary in the format {"Hardware" : ["Compatible versions"]}
    for i in range(4, 11):
        platforms = compatibility_table["Hardware"].iloc[i]
        versions = compatibility_table[column_name].iloc[i]

        parsed_platforms = (re.split(r';|, |\*|\n|\( |\)|\(', platforms))
        parsed_versions = (re.split(r'IOS XE| |\xa0|,', versions))

        while '' in parsed_versions:
            parsed_versions.remove('')

            #Removing special characters from recomended releases
        for device in parsed_platforms:
            for version in parsed_versions:
                if version == "16.9.41":
                    compatibility_dict[device].append("16.9.4")
                elif version == "16.9.3s1":
                    compatibility_dict[device].append("16.9.3s")
                elif version == "16.11.1c3":
                    compatibility_dict[device].append("16.11.1c")
                else:
                    compatibility_dict[device].append(version)
    return compatibility_dict


def verify_versions(dnac, matrix):

    '''
    Verifies compability of current switch version to the supported ones on the matrix
    For specific hardware verification must be done by family due to compability matrix format
    Prints result

        Args:
            dnac (obj): dnac object with token
            matrix (dict): dictionary of compability matrix
    '''
    devices = dnac.devices.get_device_list(family='Switches and Hubs')

    for device in devices.response:
        if (device.series == 'Cisco Catalyst 9200 Series Switches' or
                device.series == 'Cisco Catalyst 9400 Series Switches'):
            if not device.softwareVersion in matrix.get(device.series):
                print ("Unsupported Version; Hostname: {} Current version: {}".format(
                    device.hostname, device.softwareVersion))
            else:
                print ("Correct version: {}".format(device.hostname))
        elif(device.series == 'Cisco Catalyst 3850 Series Ethernet Stackable Switch' or
             device.series == 'Cisco Catalyst 3650 Series Switches'):
            if not device.softwareVersion in matrix.get("Cisco Catalyst 3850 Series and 3650 Series Switches"):
                print ("Unsupported Version; Hostname: {} Current version: {}".format(
                    device.hostname, device.softwareVersion))
            else:
                print ("Correct version: {}".format(device.hostname))
        else:
            try:
                if matrix.get(device.platformId) is None:
                    raise Exception()
                if not device.softwareVersion in matrix.get(device.platformId):
                    print ("Unsupported Version; Hostname: {} Current version: {}".format(
                        device.hostname, device.softwareVersion))
                else:
                    print ("Correct version: {}".format(device.hostname))
            except Exception:
                print ("Verification for device type {} not supported".format(
                    device.platformId))
                continue


def main():
    matrix = matrix_builder(sys.argv[4])
    # Retrieves token for DNAC API
    dnac = api.DNACenterAPI(username=sys.argv[1],
                            password=sys.argv[2],
                            base_url=sys.argv[3],
                            verify=False)
    verify_versions(dnac, matrix)


if __name__ == "__main__":
    main()

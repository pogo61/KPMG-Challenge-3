#!/bin/python
import argparse
import json
import sys


def get_value(in_obj, in_keys, idx):
    value = in_obj
    # print(f"value is {value}")
    # print(f"index is {idx}")
    # print(f"in_keys is {in_keys}")
    # print(f"in_keys[i] is {in_keys[idx]}")
    tmp = in_keys[idx]
    # print(f"tmp is {tmp}")
    temp_object = in_obj[tmp]
    # temp_object = in_obj[2]
    # print(f"temp_object is {temp_object}")
    i2 = idx + 1
    if i2 < len(in_keys):
        value = get_value(temp_object, in_keys, i2)
    else:
        value = temp_object
    return value


def object_processor(object, key):
    in_object = str(object)
    metadata_key = str(key)

    if in_object is None or metadata_key is None:
        print("Please supply the object and the key")
    else:
        temp_key = metadata_key.split("/")
        print(f"temp_list is {temp_key}")
        print(f"in_object is {in_object}")
        i = 0
        check_object = json.loads(in_object)
        # print(f"check_object is {check_object}")
        result = get_value(check_object, temp_key, i)
        return result


def main(args_in):
    print(f"args_in = {args_in}")
    parser = argparse.ArgumentParser()
    parser.add_argument('--object', help='The instance Id of the EC2 instance')
    parser.add_argument('--key', help='the key of a specific metadata item')
    print(f"Value = {object_processor(**vars(parser.parse_args(args_in)))}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

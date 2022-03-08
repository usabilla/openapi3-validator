import glob


def files_lookup(lookup_path, file_names):
    print(f"Open API specs lookup path: {lookup_path}")
    print(f"Open API specs names to lookup: {file_names}")

    spec_paths = []
    for spec_name in file_names:
        full_lookup_path = "{}/**/{}".format(lookup_path, spec_name)
        spec_paths.extend(glob.glob(full_lookup_path, recursive=True))

    print(f"Open API specs lookup result: {spec_paths}")
    return spec_paths

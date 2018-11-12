import os

def maybe_unzip_dataset(args):

    datasets = [args.dataset_name]
    dataset_paths = [args.dataset_path]


    for dataset_idx, dataset_path in enumerate(dataset_paths):
        if dataset_path.endswith('/'):
            dataset_path = dataset_path[:-1]
        print(dataset_path)
        if not os.path.exists(dataset_path):
            print("Not found dataset folder structure.. searching for .tar.bz2 file")
            zip_directory = "{}.tar.bz2".format(os.path.join(os.environ['DATASET_DIR'], datasets[dataset_idx]))

            assert os.path.exists(zip_directory), "{} dataset zip file not found" \
                                                  "place dataset in datasets folder as explained in README".format(zip_directory)
            print("Found zip file, unpacking")

            unzip_file(filepath_pack=os.path.join(os.environ['DATASET_DIR'], "{}.tar.bz2".format(datasets[dataset_idx])),
                       filepath_to_store=os.environ['DATASET_DIR'])
            args.reset_stored_filepaths = True


def unzip_file(filepath_pack, filepath_to_store):
    command_to_run = "tar -I pbzip2 -xf {} -C {}".format(filepath_pack, filepath_to_store)
    os.system(command_to_run)

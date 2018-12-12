import argparse


parser = argparse.ArgumentParser(description="Extract bottom-up features from a Detectron model")
parser.add_argument(
    "--config",
    help="Model config file used by Detectron",
    default="data/config_faster_rcnn_x101.yaml",
)
parser.add_argument(
    "--weights",
    help="Model weights file checkpointed from Detectron",
    default="data/model_faster_rcnn_x101.yaml",
)
parser.add_argument(
    "--output-h5",
    dest="output_dir",
    help="Path to output HDF file for saving bottom-up features",
    default="data/data_img_faster_rcnn_x101.h5",
)
parser.add_argument(
    "--max-bboxes",
    help="Maximum number of bounding box proposals per image",
    type=int,
    default=36
)
parser.add_argument(
    "--batch-size",
    help="Batch size for feature extraction",
    type=int,
    default=4
)
parser.add_argument(
    "--dataset",
    help="dataset to re-evaluate",
    default="oid_val",
)
parser.add_argument(
    "--feat_name",
    help=" the name of the feature to extract, default: gpu_0/fc7",
    default="gpu_0/fc7"
)


def main(args):
    pass


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)

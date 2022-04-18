# How to

## Prerequisites

```bash
source ws_270322_trafficsign/computer-vision-tf2/env/bin/activate`
git clone https://github.com/pharath/tfrecord-viewer.git`
cd tfrecord-viewer/` (**important!!!** Else it will not work!)
```

## Run

```bash
python tfviewer.py --bbox-name-key image/object/class/label path/to/GTSD_train_00000-of-00000.records`
```

- **Warning**: `--bbox-name-key` and other keys can be different for other `.records` files, so inspect the keys first using `python inspect_tfrecords_first_image.py path/to/GTSD_train_00000-of-00000.records`

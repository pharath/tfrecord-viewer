import tensorflow as tf 
import argparse

parser = argparse.ArgumentParser(description='inspect TF Record.')

parser.add_argument('tfrecords', type=str, nargs='+',
                    help='path to TF record(s) to inspect')

args = parser.parse_args()

raw_dataset = tf.data.TFRecordDataset(args.tfrecords)

for raw_record in raw_dataset.take(1):
    example = tf.train.Example()
    example.ParseFromString(raw_record.numpy())
    print(example)

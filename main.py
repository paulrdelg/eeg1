
# Python packages
import csv
import os
import pathlib
import requests
import sys
import zipfile

# Third-party packages
import mne
import mne_bids
import numpy
import openneuro
import tensorflow as tf


def mnetest():
	sample_data_folder = mne.datasets.sample.data_path()
	print(sample_data_folder)
	sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample', 'sample_audvis_filt-0-40_raw.fif')
	print(sample_data_raw_file)
	raw = mne.io.read_raw_fif(sample_data_raw_file)
	raw.plot_psd(fmax=50)
	raw.plot(duration=5, n_channels=30)

def main():
	dataset = 'ds003505'
	
	subject = '15'
	session = 'off'
	task = 'faces'
	suffix = 'eeg'
	datatype = 'eeg'
	
	# Define BIDS root path and create directory
	bids_root = os.path.join(os.getcwd(), dataset)
	if not os.path.isdir(bids_root):
		os.makedirs(bids_root)
	
	# Download BIDS data
	#openneuro.download(dataset=dataset, target_dir=bids_root, include=[f'sub-{subject}'])
	
	# Define BIDS path
	bids_path = mne_bids.BIDSPath(root=bids_root, subject=subject, datatype=datatype, task=task)
	
	# Download raw data
	raw = mne_bids.read_raw_bids(bids_path=bids_path, verbose=False)
	print('done')


if __name__ == '__main__':
	main()

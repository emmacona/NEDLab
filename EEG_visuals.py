# Date created: 12/18/2024
# Author: Emmanuelle CN

import mne
import numpy as np
import matplotlib.pyplot as plt
from mne.preprocessing import find_bad_channels_maxwell


# Load  EEG data
file_path = 'file_path.set'
epochs = mne.io.read_epochs_eeglab(file_path)

# Check for any existing bad channel annotations in the data
# TODO need to identify bad channels to simplify future analysis
print("Bad channels:", epochs.info['bads'])

# Plot the epochs data
epochs.plot(n_epochs=10, 
            n_channels=len(epochs.ch_names),  # Change the number of epochs to view different parts of the EEG file
            scalings='auto')

# Plot spectral density
bands = {
    'Delta': (0.5, 4),
    'Theta': (4, 8),
    'Alpha': (8, 13),
    'Beta': (13, 30),
    'Gamma': (30, 100)
}
epochs.plot_psd(tmax=np.inf, fmax=100, 
                average=False)

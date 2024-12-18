import mne
import numpy as np
import matplotlib.pyplot as plt
from mne.preprocessing import find_bad_channels_maxwell


# Load your EEG data
file_path = 'Data/6Hz/Q1K_HSJ_1025-1042_F1_AEP_A_20240715_095058_processed_ae06.set'
epochs = mne.io.read_epochs_eeglab(file_path)

# Check for any existing bad channel annotations in the data
print("Bad channels:", epochs.info['bads'])

# Plot the epochs data
epochs.plot(n_epochs=10, n_channels=len(epochs.ch_names), 
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

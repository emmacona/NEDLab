#### Context
# SNR is defined as the ratio of signal power to noise power

#### Imports
import mne
import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters
input_folder = 'Data/6Hz'
output_folder = 'Output/6Hz'
frequency = 1000 # sample frequency

# Get .set EEG file paths from input_folder
file_paths = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.set')]

# Process each file
for file_path in file_paths:
    # Load EEG data
    epochs = mne.io.read_epochs_eeglab(file_path, preload=True)
    data = epochs.get_data()  # Shape is (n_epochs, n_channels, n_times)
    sfreq = epochs.info['sfreq']  # Sampling frequency

    # Assuming you're processing one channel data or a mean for simplicity
    eeg_data = np.mean(data, axis=(0, 1))  # Mean across epochs and channels

    # Compute Fourier Transform
    n = len(eeg_data)
    freqs = np.fft.fftfreq(n, d=1/sfreq)
    fft_values = np.fft.fft(eeg_data)
    power_spectrum = np.abs(fft_values) ** 2

    # Identify signal and noise indices
    signal_idx = np.where((freqs > frequency - 0.5) & (freqs < frequency + 0.5))[0]
    noise_idx = np.where((freqs > 4) & (freqs < 8))[0]

    # Compute power in the bands
    signal_power = np.sum(power_spectrum[signal_idx])
    noise_power = np.mean(power_spectrum[noise_idx])

    # Calculate SNR
    SNR = 10 * np.log10(signal_power / noise_power)

    # Filename
    base_name = os.path.basename(file_path)
    base_name = os.path.splitext(base_name)[0]  # Remove the extension
    parts = base_name.split('_')
    filename = '_'.join(parts[:3]) # Keep only Q1K_HSJ_XXXX-XXXX_M1/S1...

    # Save the plot to the output folder
    plt.figure(figsize=(10, 6))
    plt.plot(freqs, power_spectrum)
    plt.xlim([0, 50])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectrum')
    plt.title(f'Power Spectrum for {filename}')
    plt.savefig(os.path.join(output_folder, f'{filename}_power_spectrum.png'))
    plt.close()

    print(f'Processed {filename}: SNR = {SNR}')

# Audio and Video Processing with Color Components and Pickle

This repository includes various scripts for processing audio and video data. It demonstrates fundamental techniques such as color component extraction, video recording, quantization, upsampling, filtering, and data serialization with `pickle`.

## Overview

This project provides tools for:
- Extracting and reconstructing color components (Y, Cb, Cr) from images and video.
- Real-time video recording and playback.
- Image quantization, upsampling, and basic filtering.
- Serializing data using Python's `pickle` module for data preservation and transfer.

## Repository Structure

### Files

- **Img_Video.py**: Main script that provides an interactive menu for image and video processing options, including:
  - Y, Cb, Cr color component extraction.
  - Real-time video capture and playback.
- **Quantization.py**: Handles image quantization for compression purposes.
- **Upsampling.py**: Increases the resolution or sampling rate of image or audio data.
- **filter.py**: Contains basic filtering techniques for audio or image processing.
- **pk.py**: Demonstrates data serialization and deserialization using `pickle`.
- **record.py**: Captures audio input from a microphone or other sources.
- **task2.py**, **task3.py**: Additional tasks with specific processing techniques.
- **main.py**: Main script to run or integrate various processing modules.
- **i.jpg**: Sample image used for testing image-to-video or quantization tasks.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pshar10/Audio_Video_Processing.git
   cd Audio_Video_Processing
   ```

2. **Install Dependencies** (as specified in `requirements.txt` if available):
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Input Files**:
   - Place necessary input files, such as audio recordings or images, in the project directory.

## Usage

Run specific scripts to perform individual tasks. For example:

- Convert image to video and separate Y, Cb, Cr components:
  ```bash
  python Img_Video.py
  ```

  After running `Img_Video.py`, follow the interactive menu prompts:
  - **i**: Display Y component of the image `i.jpg`.
  - **v**: Capture video and display Y, Cb, Cr components.
  - **r**: Record a 5-second video as `output.avi`.
  - **p**: Play back `output.avi`.
  - **Space**: Quit the program.

- Record audio input:
  ```bash
  python record.py
  ```

- Apply quantization:
  ```bash
  python Quantization.py
  ```

## Key Functions and Modules

- **Image-to-Video Conversion and Component Extraction** (`Img_Video.py`): Separates Y, Cb, Cr color components and reconstructs the image.
- **Quantization** (`Quantization.py`): Compresses image data for different quality levels.
- **Upsampling** (`Upsampling.py`): Increases sampling rate for enhanced resolution.
- **Pickle Serialization** (`pk.py`): Serializes and deserializes multimedia data.
- **Audio Recording** (`record.py`): Records audio input from a microphone. 

---

This project serves as a foundation for basic multimedia processing, demonstrating core techniques for image, video, and audio manipulation with Python.


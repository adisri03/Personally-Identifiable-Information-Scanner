# PII Detector

## Overview

The PII Detector is a Python script designed to enhance data privacy by identifying personally identifiable information (PII) in PDF, Excel,JPEG, and JPG files. PII includes sensitive data such as names, addresses, social security numbers, and more. The script empowers users to proactively scan digital documents for potential PII, allowing for a more secure and privacy-conscious handling of sensitive information.

## Key Features

- Supports detection of PII in PDF, Excel, JPEG, or JPG files.
- Extracts links from Excel files or a local folder for further analysis.
- Generates an Excel report with details on PII matches.

### Multi-Format Support:

The script supports the detection of PII in PDF, Excel, JPEG, and JPG files, covering a wide range of common document formats.
### Link Extraction from Excel:

Users can input Excel files containing links or local folder containing files. The script automatically extracts these links for further analysis, providing a comprehensive approach to PII detection.
### Detailed Reporting:

The script generates a detailed Excel report summarizing the PII findings. The report includes information such as the column name, matched PII elements, and the corresponding link or file path.


## Prerequisites

- Python 3.x
- Required Python libraries: PyPDF2, pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/pii-detector.git
    ```

2. Change to the project directory:

    ```bash
    cd pii-detector
    ```

## Usage

1. Run the script:

    ```bash
    python pii_detector.py
    ```

2. Follow the prompts to enter PII elements, file paths, and user information.

3. The script will generate an Excel report in the Downloads folder.

## Configuration

- Customize the script for specific PII elements or detection patterns.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [PyPDF2](https://pythonhosted.org/PyPDF2/)
- [pandas](https://pandas.pydata.org/)


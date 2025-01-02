# APT Analysis and Samples Repository

## Overview
This repository contains malware samples and analysis tools as part of a research project for the Master of Cybersecurity and Threat Intelligence (MCTI) program at the University of Guelph. The project focuses on Advanced Persistent Threat (APT) analysis and includes machine learning classifiers for malware detection.

## ⚠️ Security Warning
The presence of these samples is strictly for educational and research purposes. 

**IMPORTANT:**
- Do not execute any files on your personal system or network
- All samples may contain live malware and can cause harm
- Ensure all interactions are conducted in isolated environments
- Use dedicated malware analysis virtual machines

## Project Components

### 1. Malware Samples
- Collection of APT samples for research
- Organized by threat actor groups
- Includes metadata and analysis reports

### 2. Machine Learning Classifiers
- Classic ML implementation for malware detection
- CNN-based classifier for enhanced detection capabilities
- Technical documentation and performance analysis

## Usage Requirements
1. Isolated analysis environment
2. Proper security controls
3. Understanding of malware analysis safety protocols
4. Appropriate permissions and research context

## Documentation
Detailed technical reports in the form of Jupyter notebooks are available in the results directory:
- `results/classic_ML_classifiers/`: Analysis using traditional ML approaches
  - Support Vector Machines (SVM)
  - K-Nearest Neighbors (KNN)
  - Decision Trees
  - Performance metrics and comparison

![Classic ML Classifier Results](./results/results_classic_classifier.JPG)

- `results/CNN_ML_classifier/`: Deep learning approach
  - Convolutional Neural Network implementation
  - Training process and hyperparameter tuning
  - Comparative analysis with traditional methods

Both notebooks demonstrate the results of training classifiers to predict APT group attribution based on malware characteristics.

## Legal Notice
By accessing this repository, you agree to:
1. Take full responsibility for your actions
2. Adhere to ethical guidelines in cybersecurity research
3. Use the contents for legitimate research purposes only
4. Follow appropriate safety protocols

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
For research collaborations or contributions, please follow security protocols and submit pull requests with appropriate documentation.

## Disclaimer
The authors and the University of Guelph are not responsible for any misuse or damage caused by the contents of this repository. Use at your own risk and responsibility.

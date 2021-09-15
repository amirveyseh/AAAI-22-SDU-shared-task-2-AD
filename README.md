# SDU@AAAI-22 - Shared Task 2: Acronym Disambiguation

This repository contains training & development sets, acronym dictionary, and the evaluation scripts for the [acronym disambiguation task at SDU@AAA-22](https://sites.google.com/view/sdu-aaai22/shared-task).

# Dataset

The dataset folder contains data for three languages English (Legal domain and Scientific domain), French, and Spanish. The corresponding forlder for each language contains three files:

- **diction.json**: A dictionary of the acronyms and their possible meanings. All predictions should use this dictionary to expand the ambiguous acronyms in the text.
- **train.json**: The training samples for acronym disambiguation task. Each sample has three attributes:
  - sentence: The string value of the sample text
  - acronym: The string value of the ambiguous acronym in the text.
  - label: The correct long-form of the acronym in the sample. These expansions are selected from `diction.json` dictionary. 
  - id: The unique ID of the sample
- **dev.json**: The development set for acronym disambiguation task. The samples in `dev.json` have the same attributes as the samples in `train.json`.
  
 Note that the acronyms in the `train.json`, `dev.json` and `test.json` (which will be provided later) are all disjoint. 
  
# Code
In order to familiarize the participants with this task, we provide a rule-based baseline in `code` directory. This baseline computes the similarityy of the candidate long-forms with the sample text (in terms of number of overlapping words) and it choose the long-form with the highest similarity score as the final prediction. To run this baseline, run the following command:

`python code/baseline.py -input <path/to/input.json> -diction <path/to/diction.json> -output <path/to/output.json>`

Please replace `<path/to/input.json>`, `<path/to/diction.json>`, `<path/to/output.json` with the real paths to the input file (e.g., `dataset/dev.json`), dictionary and output json files. The output file contains the predictions for the input file and could be consumed by the scorer described in the next section to obtain the performance of this baseline.

# Evaluation

To evaluate the predictions, run the following command:

`python scorer.py -g path/to/gold.json -p path/to/predictions.json`

The `path/to/gold.json` and `path/to/predictions.json` should be replaced with the real paths to the gold file (e.g., `dataset/dev.json` for evaluation on development set) and predictions file (i.e., the predictions generated by your system. It should be in the same format as `dataset/dev.json` or `dataset/train.json` files). The official evaluation metrics are the macro-averaged precision, recall and F1 for correct long-form predictions. For verbose evaluation (including the micro-averaged precision, recall and F1 and also the accuracy of the predictions), use the following command:

`python scorer.py -g path/to/gold.json -p path/to/predictions.json -v`

# Participation

In order to participate, please first fill out this form to register for the shared tasks: https://forms.gle/njVArce6cwgFmZjG7. The team name that is provided in this form will be used in the subsequent submissions and communications. This shared task is organized as a CodaLab competition accessible from [here](https://competitions.codalab.org/competitions/34899). There are two separate phases:
- *Development Phase*: In this phase, the participants will use the training/development sets provided in this repository to design and develop their models. 
- *Evaluation Phase*: 10 days before the system runs due, i.e., 1st November 2021, the test set is released here. The test set has the same distribution and format as the development set. Run your model on the provided test set and save the prediction results in a Json file with the same format as the "dev.json" file. Name the prediction file as "**output.json**" and submit it to the CodaLab comptetition page.

For more information, see [SDU@AAAI-22](https://sites.google.com/view/sdu-aaai22/shared-task).

# Licenses
The dataset provided for this shared task is licensed under [CC BY-NC-SA 4.0 international license](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode), and the evaluation script and the baseline are licensed under MIT license.

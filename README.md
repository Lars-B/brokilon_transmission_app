# Brokilon Transmission App

A desktop application to run the `breath_helper` tool from the [`brokilon`](https://github.com/Lars-B/pyccd) package.

## Quick Links

- [Installation](#installation)
- [Usage](#usage)
- [Detailed Example](https://gist.github.com/Lars-B/0909ffde2938c6782273719fabf1bb06)
- [Development](#development)

---

## What does this tool compute?

> [!Note]
> A detailed example can be found
> [here](https://gist.github.com/Lars-B/0909ffde2938c6782273719fabf1bb06)

This tool will create a CSV file with the following columns
```csv
Infector, Infectee, Start Date of infection, blockcount, Tree index
```

To convert the tree distances to dates we need the taxon labels to have date information.
The default assumption is that the tip labels are formatted like this:
```
ID+YYYY-MM-DD
2+2007-11-01
```
> [!Caution]
> Use the input options to specify your custom format.
> Be aware that using a separator that is also present in the date format will not work!

If this information is not present in the taxon names the tool will automatically create tip dates.
This is done by calibrating the leaf that is furthest from the root to be the current date.
If this is required, the tool will also produce a `csv` dataframe that contains 
the dates for all taxon labels and all trees in the input.

---

## Installation

Prebuilt versions are available on the **Releases** page.

Go to: **Releases**
- Download the correct build for your operating system:
  - macOS: `.zip`
  - Windows: `.zip`
  - Linux: `.zip`

- Extract the archive
- Start the application
    - macOS: extracted file is the app
    - Windows: open the extracted folder and run the `.exe`
    - Linux: open the extracted folder and run the executable

No installation or Python setup is required.

---

## Usage

1. Launch the application
2. Select an input file (tree / dataset)
3. Select an output file location
4. Set appropriate burn in
5. Set date format, separator, and scale accordingly
6. Click **Run Analysis**
7. Monitor progress in the log panel

---

## Development

This requires a python installation with the correct dependencies:

```bash
pip install -r requirements.txt 
```

### Run locally

```bash
python main.py
```

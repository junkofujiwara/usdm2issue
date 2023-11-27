# usdm2issue
Script to read USDM (Universal Specification Describing Manner) file and genarate GitHub Issues

### Requirements
see requirements.txt

### Usage
1. Create settings.py
Copy settings.py.sample to settings.py and edit it.
2. Prepare USDM file
data/RequirementsDocSample_USDM.xlsx is an example of USDM file. This file is downloaded from [content.mathworks.com](https://content.mathworks.com/viewer/63e1f6d06d0f7f6d93445507).
3. Execute script
```
pip install -r requirements.txt
python usdm2issue.py
```

### Settings
- FILE_NAME (USDM file name)
- GH_ENDPOINT (GitHub REST API endpoint)
- GH_TOKEN (GitHub personal access token)
- GH_OWNER (GitHub repository owner)
- GH_REPO (GitHub repository name)
- ISSUE_LABELS (GitHub issue labels)
- SKIP_IF_EXISTS (Skip if the issue already exists)
- MD_HEADER_ICON (Emoji Icon for markdown header)
- MD_ITEM_ICON (Emoji Icon for markdown item)
<br>
All parameter values including above settings are defined in settings.py


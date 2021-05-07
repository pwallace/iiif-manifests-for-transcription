
This folder contains IIIF manifests used to populate collections in From the Page with items stored in Internet Archive.

SETUP:
- Create a CSV containing two columns: Column A is a list of archive.org identifiers and has header cell "identifier", Column B is a list of item labels/titles and has the column header "label"

USAGE:

create-IIIF-manifest-from-IA-list.py [file.csv] "[Label/title for collection]"

EXPECTED OUTPUT:

- A valid IIIF manifest named [file_basename]_iiif.json

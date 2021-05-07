# Python program to write JSON
# to a file
  
  
import json
import sys
import os
from csv import DictReader

# infile expects the filename of a plaintext (line break delimited) list of Internet Archive identifiers  
infilename = sys.argv[1]

outfilename = os.path.splitext(infilename)[0] + "_iiif.json"

# collectionlabel expects a plaintext label in double quotes, e.g., "Hemingway Family archive" or "Alumni papers"
collectionlabel = sys.argv[2]

# Data to be written
manifestdata ={
	"@context" : "http://iiif.io/api/presentation/2/context.json",
	"@type" : "sc:Collection"
}

manifestdata["@id"] = "https://raw.githubusercontent.com/pwallace/iiif-manifests-for-transcription/main/" + outfilename

manifestdata["label"] = "IIIF Collection for the " + collectionlabel + " collection at Middlebury Special Collections"

itemmanifests = []

with open(infilename, 'r') as read_obj:
	csv_reader = DictReader(read_obj)
	for row in csv_reader:
		recorddict ={
			"@id" : 'http://iiif.archivelab.org/iiif/' + row['identifier'] + '/manifest.json',
			"@type" : "sc:Manifest",
			"label" : row['label']
			}
		itemmanifests.append(recorddict)
	manifestdata["manifests"] = itemmanifests
  
with open(outfilename, "w") as outfile:
    json.dump(manifestdata, outfile, indent=4)

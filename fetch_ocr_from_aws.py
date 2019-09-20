  
import boto3

# Document
documentName = "20190920_135440.jpg"

# Read document content
with open(documentName, 'rb') as document:
    imageBytes = bytearray(document.read())

# Amazon Textract client
textract = boto3.client('textract')

# Call Amazon Textract
response = textract.detect_document_text(Document={'Bytes': imageBytes})

#print(response)

# Print detected text
file = open("card.txt", "w")
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print ('\033' +  item["Text"] + '\033')
        file.write('\033' +  item["Text"] + '\033 \n')
file.close()




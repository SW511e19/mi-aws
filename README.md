MI OCR AWS - Card Text Recognition
=============
This project is using AWS textract to detect and extract images form Magic the Gathering Cards.
The project uses the text to categorize each card.

Installation / Setup
-----------
First, install the library and set a default region:

.. conda:: sh

    $ pip install boto3

Next, set up credentials (in e.g. ``~/.aws/credentials``):

.. conda:: ini

    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET

Then, set up a default region (in e.g. ``~/.aws/config``):

.. conda:: ini

    [default]
    region=eu-west-2




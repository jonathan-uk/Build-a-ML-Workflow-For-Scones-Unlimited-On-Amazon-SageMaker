{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import json\n",
    "import boto3\n",
    "import base64\n",
    "\n",
    "s3 = boto3.client('s3')\n",
    "\n",
    "def lambda_handler(event, context):\n",
    "    \"\"\"A function to serialize target data from S3\"\"\"\n",
    "\n",
    "    # Get the s3 address from the Step Function event input\n",
    "    key = event['s3_key']\n",
    "    bucket = event['s3_bucket']\n",
    "\n",
    "    # Download the data from s3 to /tmp/image.png\n",
    "    s3.download_file(bucket,key,\"/tmp/image.png\")\n",
    "\n",
    "    # We read the data from a file\n",
    "    with open(\"/tmp/image.png\", \"rb\") as f:\n",
    "        image_data = base64.b64encode(f.read())\n",
    "\n",
    "    # Pass the data back to the Step Function\n",
    "    print(\"Event:\", event.keys())\n",
    "    return {\n",
    "        'statusCode': 200,\n",
    "        'body': {\n",
    "            \"image_data\": image_data,\n",
    "            \"s3_bucket\": bucket,\n",
    "            \"s3_key\": key,\n",
    "            \"inferences\": []\n",
    "        }\n",
    "    }"
   ]
  }
 ],
 "metadata": {
  "instance_type": "ml.t3.medium",
  "kernelspec": {
   "display_name": "Python 3 (Data Science)",
   "language": "python",
   "name": "python3__SAGEMAKER_INTERNAL__arn:aws:sagemaker:us-east-1:081325390199:image/datascience-1.0"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

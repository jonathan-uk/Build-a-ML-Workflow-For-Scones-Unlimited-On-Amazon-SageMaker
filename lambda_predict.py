{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import boto3\n",
    "import base64\n",
    "import os\n",
    "import io\n",
    "# Fill this in with the name of your deployed model\n",
    "ENDPOINT = \"image-classification-2022-01-09-07-36-27-134\"\n",
    "runtime = boto3.client('runtime.sagemaker')\n",
    "def lambda_handler(event, context):\n",
    "    # Decode the image data\n",
    "    image = base64.b64decode(event[\"body\"][\"image_data\"])\n",
    "    # Instantiate a Predictor\n",
    "    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType=\"image/png\", Body = image)\n",
    "    # For this model the IdentitySerializer needs to be \"image/png\"\n",
    "    # Make a prediction:\n",
    "    inferences = response[\"Body\"].read()\n",
    "    # We return the data back to the Step Function\n",
    "    event[\"inferences\"] = inferences.decode('utf-8')\n",
    "    return {\n",
    "        'statusCode': 200,\n",
    "        'body': json.dumps(event)\n",
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

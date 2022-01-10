{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "THRESHOLD = .93\n",
    "def lambda_handler(event, context):\n",
    "    # Grab the inferences from the event\n",
    "    inferences = event[\"body\"][\"inferences\"]\n",
    "    # Check if any values in our inferences are above THRESHOLD\n",
    "    for i in range(len(inferences)):\n",
    "        meets_threshold = i > THRESHOLD\n",
    "    # If our threshold is met, pass our data back out of the\n",
    "    # Step Function, else, end the Step Function with an error\n",
    "    if meets_threshold:\n",
    "        pass\n",
    "    else:\n",
    "        raise(\"THRESHOLD_CONFIDENCE_NOT_MET\")\n",
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

#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Number of datapoints
print len(enron_data.keys())

# Number of features
print len(enron_data[enron_data.keys()[0]])

# Number of POIs in dataset
count = 0
for k in enron_data.keys():
    if enron_data[k]["poi"]: count += 1
print count

# James Prentice Stock

print enron_data["PRENTICE JAMES"]["total_stock_value"]

# Messages from Wesley Colwell

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# Stock options exercised by Jeff SKILLING

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Who took most money

print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

# Non NaN salary and email, and NaN total payments, and POIs without financial data

countSalary = 0
countEmail = 0
countTotalPayments = 0
countNanPOIs = 0

for k in enron_data.keys():
    if enron_data[k]['salary'] != 'NaN': countSalary += 1
    if enron_data[k]['email_address'] != 'NaN': countEmail += 1
    if enron_data[k]['total_payments'] == 'NaN': countTotalPayments += 1
    if (enron_data[k]['poi'] and enron_data[k]['total_payments'] == 'NaN'): countNanPOIs += 1

print countSalary, countEmail, countTotalPayments, countNanPOIs

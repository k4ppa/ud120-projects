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

import math
import pickle

from final_project.poi_email_addresses import poiEmails

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print len(enron_data['SKILLING JEFFREY K'].keys())

poi = 0
for p_key, p_value in enron_data.iteritems():
    if p_value['poi']:
        poi += 1
print poi

poi_name_record = open("../final_project/poi_names.txt").read().split("\n")
poi_name_total = [record for record in poi_name_record if "(y)" in record or "(n)" in record]
print "Total number of POIs: ", len(poi_name_total)

sal = 0
for key, value in enron_data.iteritems():
    if not math.isnan(float(value['salary'])):
        sal += 1
print sal

email = 0
for key, value in enron_data.iteritems():
    if str(value['email_address']) != 'NaN':
        email += 1
print 'email {}'.format(email)

total_pay = 0
for key, value in enron_data.iteritems():
    if str(value['total_payments']) == 'NaN' and value['poi']:
        total_pay += 1
print len(enron_data)
print total_pay
print 'percentage of total payment NaN: {}'.format(float(total_pay) / len(enron_data.keys()))

poi = 0
for key, value in enron_data.iteritems():
    if value['poi']:
        poi += 1
print poi




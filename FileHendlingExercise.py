import csv

import xlsxwriter
import xlsxwriter as ex
import pandas as pd

from openpyxl import Workbook

Read = open('/home/setu/Downloads/Data.txt')

# Write = open('/home/setu/Downloads/Extracted.xlsx', 'w')
# WriteW = open('/home/setu/Downloads/NEW_Extracted.xlsx', 'w')

d1 = {
    "value": [
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37000.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37000,
            "lastPrice": 315.75,
            "pChange": 34.333120612635604,
            "openPrice": 343.25,
            "highPrice": 587.2,
            "lowPrice": 281.65,
            "numberOfContractsTraded": 1210479,
            "totalTurnover": 111119.126105,
            "premiumTurnover": 1133741862610.5,
            "openInterest": 63270,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37000.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37000,
            "lastPrice": 505,
            "pChange": -34.96458467482292,
            "openPrice": 415,
            "highPrice": 620,
            "lowPrice": 415,
            "numberOfContractsTraded": 594330,
            "totalTurnover": 76985.4054625,
            "premiumTurnover": 558498115546.25,
            "openInterest": 31781,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37200.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37200,
            "lastPrice": 395.55,
            "pChange": -38.564883124951464,
            "openPrice": 453.55,
            "highPrice": 496,
            "lowPrice": 347,
            "numberOfContractsTraded": 733360,
            "totalTurnover": 76731.68013249998,
            "premiumTurnover": 691317098013.25,
            "openInterest": 38114,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37200.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37200,
            "lastPrice": 406.8,
            "pChange": 32.59452411994785,
            "openPrice": 446.45,
            "highPrice": 688.4,
            "lowPrice": 358.95,
            "numberOfContractsTraded": 550805,
            "totalTurnover": 60669.64926,
            "premiumTurnover": 520216534926,
            "openInterest": 25991,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37500.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37500,
            "lastPrice": 262,
            "pChange": -44.47976266158084,
            "openPrice": 359,
            "highPrice": 386,
            "lowPrice": 222.3,
            "numberOfContractsTraded": 818991,
            "totalTurnover": 57582.50338,
            "premiumTurnover": 775385750338,
            "openInterest": 59872,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37100.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37100,
            "lastPrice": 359.55,
            "pChange": 34.738617200674526,
            "openPrice": 376.2,
            "highPrice": 634,
            "lowPrice": 317.15,
            "numberOfContractsTraded": 527540,
            "totalTurnover": 53103.031695,
            "premiumTurnover": 495903080669.5,
            "openInterest": 21302,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37300.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37300,
            "lastPrice": 348.4,
            "pChange": -40.12716961677265,
            "openPrice": 584.4,
            "highPrice": 584.4,
            "lowPrice": 302,
            "numberOfContractsTraded": 541680,
            "totalTurnover": 50408.461275,
            "premiumTurnover": 511706328627.5,
            "openInterest": 29988,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37100.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37100,
            "lastPrice": 448.6,
            "pChange": -36.06498966721299,
            "openPrice": 668.95,
            "highPrice": 669.3,
            "lowPrice": 389.05,
            "numberOfContractsTraded": 406784,
            "totalTurnover": 47143.80242,
            "premiumTurnover": 382982270242,
            "openInterest": 18347,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36900.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36900,
            "lastPrice": 277.65,
            "pChange": 34.585555016965564,
            "openPrice": 300,
            "highPrice": 561.45,
            "lowPrice": 248.5,
            "numberOfContractsTraded": 428443,
            "totalTurnover": 35285.5725,
            "premiumTurnover": 399742307250,
            "openInterest": 19460,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36800.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36800,
            "lastPrice": 242.6,
            "pChange": 38.03698435277382,
            "openPrice": 291.45,
            "highPrice": 498.55,
            "lowPrice": 218.4,
            "numberOfContractsTraded": 479545,
            "totalTurnover": 34859.8386675,
            "premiumTurnover": 446043703866.75006,
            "openInterest": 26584,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36500.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36500,
            "lastPrice": 159.3,
            "pChange": 34.2038753159225,
            "openPrice": 172.5,
            "highPrice": 354.8,
            "lowPrice": 147.2,
            "numberOfContractsTraded": 635529,
            "totalTurnover": 32033.4871425,
            "premiumTurnover": 584298861214.25,
            "openInterest": 42258,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37400.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37400,
            "lastPrice": 302.4,
            "pChange": -42.79769223493805,
            "openPrice": 399.85,
            "highPrice": 439.85,
            "lowPrice": 259.15,
            "numberOfContractsTraded": 386985,
            "totalTurnover": 31438.8980675,
            "premiumTurnover": 365859374806.75,
            "openInterest": 20626,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37300.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37300,
            "lastPrice": 460,
            "pChange": 34.581626682270326,
            "openPrice": 453,
            "highPrice": 741.15,
            "lowPrice": 403.45,
            "numberOfContractsTraded": 254135,
            "totalTurnover": 31171.6203,
            "premiumTurnover": 240713499530,
            "openInterest": 16227,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37500.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37500,
            "lastPrice": 572.75,
            "pChange": 33.151226316401264,
            "openPrice": 580,
            "highPrice": 864.15,
            "lowPrice": 505.05,
            "numberOfContractsTraded": 201802,
            "totalTurnover": 31107.637275,
            "premiumTurnover": 192822326227.5,
            "openInterest": 24765,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36700.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36700,
            "lastPrice": 211.75,
            "pChange": 35.3035143769968,
            "openPrice": 192,
            "highPrice": 449.8,
            "lowPrice": 191.5,
            "numberOfContractsTraded": 318005,
            "totalTurnover": 20455.181835,
            "premiumTurnover": 294444510683.5,
            "openInterest": 18161,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE38000.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 38000,
            "lastPrice": 117.55,
            "pChange": -53.7932389937107,
            "openPrice": 200,
            "highPrice": 200,
            "lowPrice": 105.3,
            "numberOfContractsTraded": 567087,
            "totalTurnover": 18622.132275,
            "premiumTurnover": 541634163227.5,
            "openInterest": 69312,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37400.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37400,
            "lastPrice": 511.6,
            "pChange": 32.48737537226468,
            "openPrice": 455,
            "highPrice": 815.05,
            "lowPrice": 453,
            "numberOfContractsTraded": 117279,
            "totalTurnover": 16273.749375,
            "premiumTurnover": 111788139937.5,
            "openInterest": 8188,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37600.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37600,
            "lastPrice": 226.3,
            "pChange": -46.6839439274355,
            "openPrice": 320,
            "highPrice": 320,
            "lowPrice": 191.25,
            "numberOfContractsTraded": 264638,
            "totalTurnover": 16145.5494,
            "premiumTurnover": 250987154940.00003,
            "openInterest": 21547,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37700.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37700,
            "lastPrice": 193.15,
            "pChange": -48.739384288747345,
            "openPrice": 310,
            "highPrice": 310,
            "lowPrice": 163.25,
            "numberOfContractsTraded": 289715,
            "totalTurnover": 15243.5048325,
            "premiumTurnover": 275142467983.25,
            "openInterest": 29600,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36600.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36600,
            "lastPrice": 185,
            "pChange": 39.20240782543265,
            "openPrice": 206.55,
            "highPrice": 392.8,
            "lowPrice": 168.25,
            "numberOfContractsTraded": 208739,
            "totalTurnover": 11986.4282,
            "premiumTurnover": 192521482820,
            "openInterest": 13496,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36600.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "55-Oct-2021",
            "optionType": "Call",
            "strikePrice": 36600,
            "lastPrice": 185,
            "pChange": 39.20240782543265,
            "openPrice": 206.55,
            "highPrice": 392.8,
            "lowPrice": 168.25,
            "numberOfContractsTraded": 208739,
            "totalTurnover": 11986.4282,
            "premiumTurnover": 192521482820,
            "openInterest": 13496,
            "underlyingValue": 37137.3
        }
    ],
    "volume": [
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37000.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37000,
            "lastPrice": 315.75,
            "pChange": 34.333120612635604,
            "openPrice": 343.25,
            "highPrice": 587.2,
            "lowPrice": 281.65,
            "numberOfContractsTraded": 1210479,
            "totalTurnover": 111119.126105,
            "premiumTurnover": 1133741862610.5,
            "openInterest": 63270,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37500.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37500,
            "lastPrice": 262,
            "pChange": -44.47976266158084,
            "openPrice": 359,
            "highPrice": 386,
            "lowPrice": 222.3,
            "numberOfContractsTraded": 818991,
            "totalTurnover": 57582.50338,
            "premiumTurnover": 775385750338,
            "openInterest": 59872,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37200.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37200,
            "lastPrice": 395.55,
            "pChange": -38.564883124951464,
            "openPrice": 453.55,
            "highPrice": 496,
            "lowPrice": 347,
            "numberOfContractsTraded": 733360,
            "totalTurnover": 76731.68013249998,
            "premiumTurnover": 691317098013.25,
            "openInterest": 38114,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36500.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36500,
            "lastPrice": 159.3,
            "pChange": 34.2038753159225,
            "openPrice": 172.5,
            "highPrice": 354.8,
            "lowPrice": 147.2,
            "numberOfContractsTraded": 635529,
            "totalTurnover": 32033.4871425,
            "premiumTurnover": 584298861214.25,
            "openInterest": 42258,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37000.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37000,
            "lastPrice": 505,
            "pChange": -34.96458467482292,
            "openPrice": 415,
            "highPrice": 620,
            "lowPrice": 415,
            "numberOfContractsTraded": 594330,
            "totalTurnover": 76985.4054625,
            "premiumTurnover": 558498115546.25,
            "openInterest": 31781,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE38000.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 38000,
            "lastPrice": 117.55,
            "pChange": -53.7932389937107,
            "openPrice": 200,
            "highPrice": 200,
            "lowPrice": 105.3,
            "numberOfContractsTraded": 567087,
            "totalTurnover": 18622.132275,
            "premiumTurnover": 541634163227.5,
            "openInterest": 69312,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37200.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37200,
            "lastPrice": 406.8,
            "pChange": 32.59452411994785,
            "openPrice": 446.45,
            "highPrice": 688.4,
            "lowPrice": 358.95,
            "numberOfContractsTraded": 550805,
            "totalTurnover": 60669.64926,
            "premiumTurnover": 520216534926,
            "openInterest": 25991,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37300.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37300,
            "lastPrice": 348.4,
            "pChange": -40.12716961677265,
            "openPrice": 584.4,
            "highPrice": 584.4,
            "lowPrice": 302,
            "numberOfContractsTraded": 541680,
            "totalTurnover": 50408.461275,
            "premiumTurnover": 511706328627.5,
            "openInterest": 29988,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE37100.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 37100,
            "lastPrice": 359.55,
            "pChange": 34.738617200674526,
            "openPrice": 376.2,
            "highPrice": 634,
            "lowPrice": 317.15,
            "numberOfContractsTraded": 527540,
            "totalTurnover": 53103.031695,
            "premiumTurnover": 495903080669.5,
            "openInterest": 21302,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36800.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36800,
            "lastPrice": 242.6,
            "pChange": 38.03698435277382,
            "openPrice": 291.45,
            "highPrice": 498.55,
            "lowPrice": 218.4,
            "numberOfContractsTraded": 479545,
            "totalTurnover": 34859.8386675,
            "premiumTurnover": 446043703866.75006,
            "openInterest": 26584,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36900.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36900,
            "lastPrice": 277.65,
            "pChange": 34.585555016965564,
            "openPrice": 300,
            "highPrice": 561.45,
            "lowPrice": 248.5,
            "numberOfContractsTraded": 428443,
            "totalTurnover": 35285.5725,
            "premiumTurnover": 399742307250,
            "openInterest": 19460,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36000.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36000,
            "lastPrice": 79,
            "pChange": 33.44594594594594,
            "openPrice": 79.75,
            "highPrice": 198,
            "lowPrice": 74.05,
            "numberOfContractsTraded": 414586,
            "totalTurnover": 11110.22779,
            "premiumTurnover": 374843222778.99994,
            "openInterest": 41249,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37100.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37100,
            "lastPrice": 448.6,
            "pChange": -36.06498966721299,
            "openPrice": 668.95,
            "highPrice": 669.3,
            "lowPrice": 389.05,
            "numberOfContractsTraded": 406784,
            "totalTurnover": 47143.80242,
            "premiumTurnover": 382982270242,
            "openInterest": 18347,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37400.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37400,
            "lastPrice": 302.4,
            "pChange": -42.79769223493805,
            "openPrice": 399.85,
            "highPrice": 439.85,
            "lowPrice": 259.15,
            "numberOfContractsTraded": 386985,
            "totalTurnover": 31438.8980675,
            "premiumTurnover": 365859374806.75,
            "openInterest": 20626,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021PE36700.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Put",
            "strikePrice": 36700,
            "lastPrice": 211.75,
            "pChange": 35.3035143769968,
            "openPrice": 192,
            "highPrice": 449.8,
            "lowPrice": 191.5,
            "numberOfContractsTraded": 318005,
            "totalTurnover": 20455.181835,
            "premiumTurnover": 294444510683.5,
            "openInterest": 18161,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE38500.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Jigna",
            "strikePrice": 38500,
            "lastPrice": 48.9,
            "pChange": -60.88,
            "openPrice": 55.55,
            "highPrice": 112,
            "lowPrice": 47.65,
            "numberOfContractsTraded": 314521,
            "totalTurnover": 4450.479915,
            "premiumTurnover": 303761522991.5,
            "openInterest": 44577,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37700.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37700,
            "lastPrice": 193.15,
            "pChange": -48.739384288747345,
            "openPrice": 310,
            "highPrice": 310,
            "lowPrice": 163.25,
            "numberOfContractsTraded": 289715,
            "totalTurnover": 15243.5048325,
            "premiumTurnover": 275142467983.25,
            "openInterest": 29600,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE39000.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 39000,
            "lastPrice": 21.85,
            "pChange": -63.824503311258276,
            "openPrice": 59.5,
            "highPrice": 59.5,
            "lowPrice": 21.75,
            "numberOfContractsTraded": 286431,
            "totalTurnover": 1905.07083,
            "premiumTurnover": 280347982083,
            "openInterest": 46871,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37600.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37600,
            "lastPrice": 226.3,
            "pChange": -46.6839439274355,
            "openPrice": 320,
            "highPrice": 320,
            "lowPrice": 191.25,
            "numberOfContractsTraded": 264638,
            "totalTurnover": 16145.5494,
            "premiumTurnover": 250987154940.00003,
            "openInterest": 21547,
            "underlyingValue": 37137.3
        },
        {
            "underlying": "BANKNIFTY",
            "identifier": "OPTIDXBANKNIFTY07-10-2021CE37800.00",
            "instrumentType": "OPTIDX",
            "instrument": "Index Options",
            "expiryDate": "07-Oct-2021",
            "optionType": "Call",
            "strikePrice": 37800,
            "lastPrice": 164.7,
            "pChange": -50.11358473421173,
            "openPrice": 242.7,
            "highPrice": 242.7,
            "lowPrice": 142,
            "numberOfContractsTraded": 256152,
            "totalTurnover": 11583.96222,
            "premiumTurnover": 243667131222,
            "openInterest": 26059,
            "underlyingValue": 37137.3
        }
    ]
}
# out_put = []
# Call_out_put = []
# Put_out_put = []
#
# for i in d1:
#     for j in d1[i]:
#         out_put.append(
#             {"underlying": j["underlying"], "identifier": j["identifier"], "instrumentType": j["instrumentType"],
#              "instrument": j["instrument"], "expiryDate": j["expiryDate"], "optionType": j["optionType"],
#              "strikePrice": j["strikePrice"], "lastPrice": j["lastPrice"], "pChange": j["pChange"],
#              "openPrice": j["openPrice"], "highPrice": j["highPrice"], "lowPrice": j["lowPrice"],
#              "numberOfContractsTraded": j["numberOfContractsTraded"], "totalTurnover": j["totalTurnover"],
#              "premiumTurnover": j["premiumTurnover"], "openInterest": j["openInterest"],
#              "underlyingValue": j["underlyingValue"]})
#         if j["optionType"] == 'Call':
#             Call_out_put.append(
#                 {"underlying": j["underlying"], "identifier": j["identifier"], "instrumentType": j["instrumentType"],
#                  "instrument": j["instrument"], "expiryDate": j["expiryDate"], "optionType": j["optionType"],
#                  "strikePrice": j["strikePrice"], "lastPrice": j["lastPrice"], "pChange": j["pChange"],
#                  "openPrice": j["openPrice"], "highPrice": j["highPrice"], "lowPrice": j["lowPrice"],
#                  "numberOfContractsTraded": j["numberOfContractsTraded"], "totalTurnover": j["totalTurnover"],
#                  "premiumTurnover": j["premiumTurnover"], "openInterest": j["openInterest"],
#                  "underlyingValue": j["underlyingValue"]})
#         elif j["optionType"] == 'Put':
#             Put_out_put.append(
#                 {"underlying": j["underlying"], "identifier": j["identifier"], "instrumentType": j["instrumentType"],
#                  "instrument": j["instrument"], "expiryDate": j["expiryDate"], "optionType": j["optionType"],
#                  "strikePrice": j["strikePrice"], "lastPrice": j["lastPrice"], "pChange": j["pChange"],
#                  "openPrice": j["openPrice"], "highPrice": j["highPrice"], "lowPrice": j["lowPrice"],
#                  "numberOfContractsTraded": j["numberOfContractsTraded"], "totalTurnover": j["totalTurnover"],
#                  "premiumTurnover": j["premiumTurnover"], "openInterest": j["openInterest"],
#                  "underlyingValue": j["underlyingValue"]})
#         else:
#             continue

# ########using File handling *********************************************************
# fields = ["underlying", "identifier", "instrumentType", "instrument", "expiryDate", "optionType", "strikePrice",
#           "lastPrice",
#           "pChange",
#           "openPrice",
#           "highPrice",
#           "lowPrice",
#           "numberOfContractsTraded",
#           "totalTurnover",
#           "premiumTurnover",
#           "openInterest",
#           "underlyingValue"]

# workBook = xlsxwriter.Workbook('/home/setu/Downloads/NEW_Extracted.xlsx')
# workSheet1 = workBook.add_worksheet("Call")
# workSheet2 = workBook.add_worksheet("Put")
#
# workBook.close()
# with open('/home/setu/Downloads/Data_Extracted.csv', 'w') as csvFile:
#     writer = csv.DictWriter(csvFile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(out_put)
########using File handling *********************************************************

########Using pandas library *********************************************************

########Excel File
# Call = pd.DataFrame(Call_out_put)
# Put = pd.DataFrame(Put_out_put)
# with pd.ExcelWriter('/home/setu/Downloads/Extracted.xlsx') as writer:
#     Call.to_excel(writer, 'Call')
#     Put.to_excel(writer, "Put")
########CSV FILE
# df=pd.DataFrame(out_put)
# df.to_csv('/home/setu/Downloads/Extracted.xlsx') #csv
########Using pandas library *********************************************************

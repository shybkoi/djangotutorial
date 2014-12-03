import os
import datetime
import math
import csv
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


def process_square(dic_params):
    result = {'err': False, 'err_mes': ''}
    try:
        a, b, c = int(dic_params['a']), int(dic_params['b']), int(dic_params['c'])
    except MultiValueDictKeyError:
        result['err'] = True
        result['err_mes'] = "Wrong input parameters!"
        return result
    except ValueError:
        result['err'] = True
        result['err_mes'] = "Wrong type of input parameters!"
        return result
    result['a'], result['b'], result['c'] = a, b, c
    D = b ** 2 - 4 * a * c
    print D
    if D < 0:
        result['mes'] = "No squares"
    elif D == 0:
        x = -b / (2 * a)
        result['mes'] = "Just one square x=" + str(x)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        result['mes'] = "Square x1=" + str(x1) + " x2=" + str(x2)
    return result

def get_heroes_info(heroes_nik):
    file_name = "nine/data.csv"
    result = {'err': False, 'err_mes': '', 'detail': heroes_nik}
    if not os.path.isfile(file_name):
        result['err'] = True
        result['err_mes'] = u"No source data file!"
        print u"No source data file!"
        return result
    input_file = open(file_name, "rU")
    read_csv = csv.DictReader(input_file, fieldnames=['id', 'surname',
                                  'name', 'birthdate', 'nickname'])
    res_dic = []
    for row in read_csv:
        if row.values() == row.keys():
            continue
        res_dic.append(row)
        if row['nickname'].lower() == heroes_nik:
            res_dic = []
            res_dic.append(row)
            break
    input_file.close()
    result['csv'] = res_dic
    return result

def square(request):
    res = process_square(request.GET)
    return render(request, 'square.html', {'result': res})

def heroes(request, heroes_nik=None):
    res = get_heroes_info(heroes_nik)
    return render(request, 'heroes.html', {'result': res})

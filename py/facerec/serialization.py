#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) Philipp Wagner. All rights reserved.
# Licensed under the BSD license. See LICENSE file in the project root for full license information.

import sys

IsPython3=sys.version_info >= (3, 0)

if IsPython3:
    import pickle as cPickle
else:
    import cPickle

def save_model(filename, model):
    output = open(filename, 'wb')
    cPickle.dump(model, output)
    output.close()


def load_model(filename):
    pkl_file = open(filename, 'rb')
    if IsPython3:
        res = cPickle.load(pkl_file, encoding='latin-1')
    else:
        res = cPickle.load(pkl_file)
    pkl_file.close()
    return res

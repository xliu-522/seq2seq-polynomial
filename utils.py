import os
import random

import torch
import numpy as np


def load_file(file_path):
    with open(file_path) as fi:
        pairs = [line.strip().split("=") for line in fi]
    return pairs


def score(true_expansion, pred_expansion):
    return int(true_expansion == pred_expansion)


def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    os.environ["PYTHONHASHSEED"] = str(seed)

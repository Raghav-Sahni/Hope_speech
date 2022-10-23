import numpy as np
import os

def load_glove_twitter_25():
    parent_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    gt25_save_path = os.path.join(parent_dir, 'Word_Embeddings\Pre Computed Word Embeddings')
    train = np.load(os.path.join(gt25_save_path, 'gt_25_train_english.npy'), allow_pickle=True)
    dev = np.load(os.path.join(gt25_save_path, 'gt_25_dev_english.npy'), allow_pickle=True)
    test = np.load(os.path.join(gt25_save_path, 'gt_25_test_english.npy'), allow_pickle=True)
    return train, dev, test

def load_fasttext_300():
    parent_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    ft300_save_path = os.path.join(parent_dir, 'Word_Embeddings\Pre Computed Word Embeddings')
    train = np.load(os.path.join(ft300_save_path, 'ft_300_train_english.npy'), allow_pickle=True)
    dev = np.load(os.path.join(ft300_save_path, 'ft_300_dev_english.npy'), allow_pickle=True)
    test = np.load(os.path.join(ft300_save_path, 'ft_300_test_english.npy'), allow_pickle=True)
    return train, dev, test

def load_word2vec_300():
    parent_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    wv300_save_path = os.path.join(parent_dir, 'Word_Embeddings\Pre Computed Word Embeddings')
    train = np.load(os.path.join(wv300_save_path, 'w2v_300_train_english.npy'), allow_pickle=True)
    dev = np.load(os.path.join(wv300_save_path, 'w2v_300_dev_english.npy'), allow_pickle=True)
    test = np.load(os.path.join(wv300_save_path, 'w2v_300_test_english.npy'), allow_pickle=True)
    return train, dev, test

def load_labels():
    parent_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    labels_save_path = os.path.join(parent_dir, 'Word_Embeddings\Pre Computed Word Embeddings')
    train = np.load(os.path.join(labels_save_path, 'train_labels.npy'), allow_pickle=True)
    dev = np.load(os.path.join(labels_save_path, 'dev_labels.npy'), allow_pickle=True)
    test = np.load(os.path.join(labels_save_path, 'test_labels.npy'), allow_pickle=True)
    return train, dev, test
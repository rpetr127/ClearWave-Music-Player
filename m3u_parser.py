import re
from pprint import pprint

import requests


class Datas(object):
    def __init__(self, files=None, urls=None, content=''):
        self.files = files
        self.urls = urls
        if self.files:
            self.files = Files(files)
        if self.urls:
            self.urls = Urls(urls)
            self.content = content
        else:
            self.urls = None
            self.content = None


class Files:
    def __init__(self, files=None):
        self.files = files

    def __getitem__(self, item):
        cls = FileMetadata(self.files[item])
        return cls

class Urls:
    def __init__(self, urls=None):
        self.urls = urls

    def __getitem__(self, item):
        cls = StreamMetadata(self.urls[item])
        return cls


class FileMetadata:
    def __init__(self, item=None):
        self.item = item

    @property
    def file(self):
        self._file = self.item.split('\n')[1]
        return self._file

    @property
    def title(self):
        self._title = self.item.split('\n')[0].split(',')[1]
        return self._title

    @property
    def duration(self):
        self._duration = self.item.split('\n')[0].split(',')[0]
        return self._duration

    @file.setter
    def file(self, value):
        self._file = ''

    @title.setter
    def title(self, value):
        self._title = ''

    @duration.setter
    def duration(self, value):
        self._duration = ''


class StreamMetadata:
    def __init__(self, item=None):
        self.item = item

    @property
    def picture(self):
        match = re.search(r'\"(https?:\/\/[\w\.\/:]+)\"', self.item)
        if match:
            self._picture = match.group(1)
            return self._picture

    @property
    def title(self):
        self._title = self.item.split('\n')[0].split(',')[1]
        return self._title


    @property
    def url(self):
        match = re.search(r'(https?:\/\/[\w\-\.\/:]*)', self.item)
        if match:
            self._url = match.group(0)
            print(self._url)
            return self._url


    @url.setter
    def url(self, value):
        self._url = ''

    @picture.setter
    def picture(self, value):
        self._picture = ''


def load(url=None, filepath=None):
    if url:
        response = requests.get(url)
        metadata = response.text
    else:
        file = open(filepath, 'r', encoding='utf-8', errors='ignore')
        metadata = file.read()
    return split(metadata)


def split(metadata):
    files = None
    urls = None
    content = metadata
    datas = re.split(r'EXTM3U[\w\S ]*\r?\n', metadata[1:])
    datas = re.split(r'\n#EXTINF:', datas[1])
    for i in datas[1:]:
        if not re.search(r'https?', i):
            files = datas[1:]
            break
        if re.search(r'https?', i):
            urls = datas[1:]
            break
    data = Datas(files, urls, content)
    return data
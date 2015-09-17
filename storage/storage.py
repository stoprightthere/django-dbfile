# -*- coding: utf-8

import base64, StringIO, mimetypes
from django.core.files.storage import Storage
from .models import DbFile

class DbStorage(Storage):
    def _open(self, name, mode='rb'):
        try:
            obj = DbFile.objects.get(name = name)
            f = StringIO.StringIO(base64.b64decode(obj.content))
            f.name = name
            f.mode = mode
            return files.File(f)
        except DbFile.DoesNotExist:
            return None

    def _save(self, name, content):
        mimetype = mimetypes.guess_type(name)
        content.seek(0)
        print 'Tell: ', content.tell()
        print 'Size: ', content.size
        f = DbFile.objects.create(content = base64.b64encode(content.read()),
                                  name = name,
                                  mimetype = mimetype[0])
        return name

    def exists(self, name):
        try:
            f = DbFile.objects.get(name = name)
            return True
        except DbFile.DoesNotExist:
            return False


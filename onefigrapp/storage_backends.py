from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class PrivateFileStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_FILE_LOCATION
    default_acl = 'private'
    file_overwrite = False
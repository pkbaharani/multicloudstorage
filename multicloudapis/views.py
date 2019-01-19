# Create your views here.

import json

from azure.storage.blob import BlockBlobService, PublicAccess
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@require_http_methods(["POST"])
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def uploadfile_gcp(request):
    if request.method == 'POST':
        credentials_dict = {
            "type": "service_account",
            "project_id": "hackator",
            "private_key_id": "a09f4cc95ee28ffa03ffec6c244c7529c14589d0",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCrUIdG9Aua7JW9\nUFAla0tUsP2tVwqFLvsJ2fdNd6r78/2Vg3fQi8uXSRU53c55cqnsKm0Rcffsm0wR\ny1kENmpMtlKwwpSDWleNE6dOEn5XaIgz3k7mCZIwpZr2Id3z1iHyZkzMkHLyRrMb\n4boJ2InEVVyNkjk0lFHUYYUA6v3wpnzZmGWUb7dx+TulabnoG3ftWh3nXDgvu1Ko\nMaoV/PIjwMX9FmmIYjrs/VofaXA60MZ4TAl5ZJFEGglXfdFF07pJDa5IkcI/LDxd\nx1jmPYhvOm/UPeOwQ+aTBOgf5z7dHGX5oRc8NCdgyerY457TSzVXLRmWq7HLBxrw\nLc3TTyt/AgMBAAECggEAMjsabyN/g517CldSKKadH+gFeZ3b59EuqmTOrlg4OkgA\nQqaZqvxSZbl4D8+JivKkACswb70LBMVEOLN3FlUeNf//nvRut1T19tecZrflc5ui\n1BKK78g+pSTpmuGzQpu2uGxmeFSiX4d7XOGCuwBS5M5ipOALBe+3Tp6JcQt2CelL\nK55lLW1AwfL84kkHRT9y3+p3KAyne9tMkIvMJsiPV8NBdBEdLT5D5QURt5dBfesv\nj+RYNG3aa4UlkonHPKgLFk8RQYu0Bb9ktLS74xTDNV+Elk0xtV1VznYdPOlb9/QK\nLohWR2L4k09QXI14J27csose1O/TG5ruSc8pmJXiAQKBgQDvRR/zff7HRRvzlDYX\nYpk6aBe7BFp0v07mCAQetU+gW0ZusaJlzAcqhQ83rI36lCuSjlBSk13WZiMUTv4M\nWYxg40oqf8K6ihfHIVuFJMSWaKwNvmzz8W85dH8lzSxvmRTrKP44tFpBC9h29Qqe\nSTL8NFVpJZpbj5gjR4/sZc34cQKBgQC3SwR6dNY2Gdf32bPTyJAzTCtFcBCwx/5S\n46MJiAxOJ7lP8ywqICxeKf7iVVJ+G7ZJ70KWYcn+87ZbPtzJvWTf67QRGTV7252X\nSUxFsJ/eflA43l83wgp0sGAWercRU5bntAoviJSf6CDwAHB+PGmX+L8ocpPk5Osa\n+rczY7Ta7wKBgEP648UOeyCqpfJinauvO9G4WWWtKvYYlJYOmP0QjnsE89Hnbjh1\n62NNQrGSuRQEnQyamn+blwGfK0BN4SgpGRU9/ohsnCrbqT3OYG5HsAL74kZVYCc+\n5Vbxnl5jGMjsOWFG2FPMCgiJEQtbO5UVPwMg61Ngd6aj+Zmsb1u+4PJBAoGAQXBx\nCt9H00zqxDxfbY8/nHDnSgU2kEb2z9Uh0jdWXVjlWlvxOqD99ih8LYZUy11NeZwI\nY/RJz9JnGrCY1xXdO+zE/w3HAI9p9idfKcpjaWYjcgpCaH/Ih9yokZ4CWhdD2zl2\nIX5bwbN4fvdJMmiTMoTGisRNdP0dyyYT3i8M1NUCgYBxX6o/Nz+v+7wboimfqvOW\nKdTZLufpWrFTl7pvK1PfHMFyVwEaCCJ3sx2yTy6c4fNRbeke4/y+4Ei+tHPrqQ09\niz3fDB0xfP5qbIO7yj5W+N/+TRCDqlSd4u9G3uiMhWcMz81H4jJU1t+R9wJ8obfH\nf3aCp6N8Qc6PhQ/JPD5Ebw==\n-----END PRIVATE KEY-----\n",
            "client_email": "koushikhack44@hackator.iam.gserviceaccount.com",
            "client_id": "115303967008267449969",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/koushikhack44%40hackator.iam.gserviceaccount.com"
        }
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(
            credentials_dict
        )

        file_location = request.data['file_location']
        client = storage.Client(credentials=credentials, project='hackator')
        bucket = client.get_bucket('kbuckethack')
        blob = bucket.blob('get-pip.py')
        blob.upload_from_filename(file_location)

        return HttpResponse(
            json.dumps(
                {
                    'message': 'Successfully Uploaded file to the Google CLoud Platform'
                }
            )
        )





@require_http_methods(["POST"])
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def uploadfile_azure(request):
    if request.method == 'POST':
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='smokies',
                                              account_key='ak9T7Jnd1gBJZdr9Bx5cVH85Iqwf7dFf7HN/WWEiadWDvh46O2/FMGkYtZVeCS9oT3DNiqMAe4uXP0SYZSByVw==')

        # Create a container called 'quickstartblobs'.
        container_name = 'quickstartblobs'
        block_blob_service.create_container(container_name)

        # Set the permission so the blobs are public.
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        full_path_to_file = request.data['file_location']

        # Write text to the file.
        file = open(full_path_to_file, 'w')
        # file.write("Hello, World!")
        file.close()

        print("Temp file = " + full_path_to_file)
        print("\nUploading to Blob storage as blob" + full_path_to_file)

        # Upload the created file, use local_file_name for the blob name
        block_blob_service.create_blob_from_path(container_name, 'ram', full_path_to_file)

        return HttpResponse(
            json.dumps(
                {
                    'message': 'Successfully Uploaded file to the Google CLoud Platform'
                }
            )
        )




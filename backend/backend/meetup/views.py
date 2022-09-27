# meetup/views.py

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import datetime
import requests
import jwt
import json

from django.conf import settings
from django.core.mail import send_mail

private_key = """
fill this in with meetup private key
"""
private_key_binary = private_key.encode('ascii')
consumer_key = 'meetup_consumer_key'
client_id = 'meetup_client_id'
authed_member_id = 'member_id'
audience = 'api.meetup.com'
signing_key_id = "signing_key"

meetup_url = 'https://api.meetup.com/gql'

def get_access_token():

    signed_key = jwt.encode(
            {
                "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(milliseconds=120),
                "iss": client_id, 
                "aud": audience,
                "sub": authed_member_id,
                "jti": signing_key_id,
            },
            private_key,
            algorithm='RS256',
        )
    
    token_url = "https://secure.meetup.com/oauth2/access"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data=f'grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion={signed_key}'
    response = requests.post(token_url, headers=headers, data=data)
    
    return json.loads(response.content)

class ListGroups(APIView):
    """
    List all the groups in a pro network on meetup.com
    """
    def get(self, request, format=None):

        access_token = get_access_token()


        headers = {
            'Authorization': 'bearer ' + access_token["access_token"],
            'Content-Type': 'application/json'
        }
        data = {
            'query' : """query($urlname: String!) {
                proNetworkByUrlname(urlname: $urlname) {
                    id
                    name
                    link
                    groupsSearch {
                        edges {
                            node {
                                id
                                urlname
                                name
                                description
                            }
                        }
                    }

                }
            }
            """,
            'variables': """{
                "urlname": "djangosocial"
            }
            """
        }
        r = requests.post(meetup_url, headers=headers, data=json.dumps(data))
        return Response(r.content)
        

class RetrieveGroup(APIView):
    """
    List all the groups in a pro network on meetup.com
    """

    def get(self, request, urlname, format=None):

        access_token = get_access_token()

        connectionInput = {
            "last": 10,
        }
     
        headers = {
            'Authorization': 'bearer ' + access_token["access_token"],
            'Content-Type': 'application/json'
        }
        data = {
            'query' : """query($urlname: String!) {
                groupByUrlname(urlname: $urlname) {
                    id
                    latitude
                    longitude
                    description
                    name
                    urlname
                    unifiedEvents {
                        count
                        edges {
                            node {
                                id
                                title
                                eventUrl
                                description
                                timeStatus
                                dateTime
                            }
                        }
                    }
                }
            }
            """,
            'variables': {"urlname": urlname}
        }
        r = requests.post(meetup_url, headers=headers, data=json.dumps(data))
        
        return Response(r.content)

class Send(APIView):
    def post(self, request, format=None):
        fullName = request.data['fullName'] 
        email = request.data['email'] 
        number = request.data['number'] 
        message = request.data['message']

        send_mail(
            'Message from ' + fullName,
            message,
            email,
            ['leokthomas@outlook.com'],
            fail_silently=False,
        )

        return Response(status.HTTP_200_OK)
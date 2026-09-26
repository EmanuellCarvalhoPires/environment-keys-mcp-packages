---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/snippets/{workspace}/{encoded_id}"
category: "Snippets"
writes_data: false
tool_note: "[[bitbucket_get_a_snippet]]"
---
# Bitbucket - Get a snippet

**Get a snippet** — `GET /snippets/{workspace}/{encoded_id}`

- Run by the tool [[bitbucket_get_a_snippet]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/snippets/{{service.workspace}}/{{param:encoded_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `encoded_id` (path, string, required) — Value of encodedid in the path.

## Original description

Retrieves a single snippet.

Snippets support multiple content types:

* application/json
* multipart/related
* multipart/form-data


application/json
----------------

The default content type of the response is `application/json`.
Since JSON is always `utf-8`, it cannot reliably contain file contents
for files that are not text. Therefore, JSON snippet documents only
contain the filename and links to the file contents.

This means that in order to retrieve all parts of a snippet, N+1
requests need to be made (where N is the number of files in the
snippet).


multipart/related
-----------------

To retrieve an entire snippet in a single response, use the
`Accept: multipart/related` HTTP request header.

    $ curl -H "Accept: multipart/related" https://api.bitbucket.org/2.0/snippets/evzijst/1

Response:

    HTTP/1.1 200 OK
    Content-Length: 2214
    Content-Type: multipart/related; start="snippet"; boundary="===============1438169132528273974=="
    MIME-Version: 1.0

    --===============1438169132528273974==
    Content-Type: application/json; charset="utf-8"
    MIME-Version: 1.0
    Content-ID: snippet

    {
      "links": {
        "self": {
          "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj"
        },
        "html": {
          "href": "https://bitbucket.org/snippets/evzijst/kypj"
        },
        "comments": {
          "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/comments"
        },
        "watchers": {
          "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/watchers"
        },
        "commits": {
          "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/commits"
        }
      },
      "id": kypj,
      "title": "My snippet",
      "created_on": "2014-12-29T22:22:04.790331+00:00",
      "updated_on": "2014-12-29T22:22:04.790331+00:00",
      "is_private": false,
      "files": {
        "foo.txt": {
          "links": {
            "self": {
              "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/foo.txt"
            },
            "html": {
              "href": "https://bitbucket.org/snippets/evzijst/kypj#file-foo.txt"
            }
          }
        },
        "image.png": {
          "links": {
            "self": {
              "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/image.png"
            },
            "html": {
              "href": "https://bitbucket.org/snippets/evzijst/kypj#file-image.png"
            }
          }
        }
      ],
      "owner": {
        "username": "evzijst",
        "nickname": "evzijst",
        "display_name": "Erik van Zijst",
        "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}",
        "links": {
          "self": {
            "href": "https://api.bitbucket.org/2.0/users/evzijst"
          },
          "html": {
            "href": "https://bitbucket.org/evzijst"
          },
          "avatar": {
            "href": "https://bitbucket-staging-assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png"
          }
        }
      },
      "creator": {
        "username": "evzijst",
        "nickname": "evzijst",
        "display_name": "Erik van Zijst",
        "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}",
        "links": {
          "self": {
            "href": "https://api.bitbucket.org/2.0/users/evzijst"
          },
          "html": {
            "href": "https://bitbucket.org/evzijst"
          },
          "avatar": {
            "href": "https://bitbucket-staging-assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png"
          }
        }
      }
    }

    --===============1438169132528273974==
    Content-Type: text/plain; charset="us-ascii"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: "foo.txt"
    Content-Disposition: attachment; filename="foo.txt"

    foo

    --===============1438169132528273974==
    Content-Type: image/png
    MIME-Version: 1.0
    Content-Transfer-Encoding: base64
    Content-ID: "image.png"
    Content-Disposition: attachment; filename="image.png"

    iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
    TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
    cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
    EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
    73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
    AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
    --===============1438169132528273974==--

multipart/form-data
-------------------

As with creating new snippets, `multipart/form-data` can be used as an
alternative to `multipart/related`. However, the inherently flat
structure of form-data means that only basic, root-level properties
can be returned, while nested elements like `links` are omitted:

    $ curl -H "Accept: multipart/form-data" https://api.bitbucket.org/2.0/snippets/evzijst/kypj

Response:

    HTTP/1.1 200 OK
    Content-Length: 951
    Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

    ------------------------------63a4b224c59f
    Content-Disposition: form-data; name="title"
    Content-Type: text/plain; charset="utf-8"

    My snippet
    ------------------------------63a4b224c59f--
    Content-Disposition: attachment; name="file"; filename="foo.txt"
    Content-Type: text/plain

    foo

    ------------------------------63a4b224c59f
    Content-Disposition: attachment; name="file"; filename="image.png"
    Content-Transfer-Encoding: base64
    Content-Type: application/octet-stream

    iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
    TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
    cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
    EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
    73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
    AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
    ------------------------------5957323a6b76--

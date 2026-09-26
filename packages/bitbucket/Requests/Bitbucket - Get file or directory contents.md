---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/source
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/src/{commit}/{path}"
category: "Source"
writes_data: false
tool_note: "[[bitbucket_get_file_or_directory_contents]]"
---
# Bitbucket - Get file or directory contents

**Get file or directory contents** — `GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path}`

- Run by the tool [[bitbucket_get_file_or_directory_contents]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/src/{{param:commit}}/{{param:path}}?format={{param:format}}&q={{param:q}}&sort={{param:sort}}&max_depth={{param:max_depth}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `commit` (path, string, required) — Value of commit in the path.
- `path` (path, string, required) — Value of path in the path.
- `format` (query, string, optional) — If 'meta' is provided, returns the (json) meta data for the contents of the file. If 'rendered' is provided, returns the contents of a non-binary file in HTML-formatted rendered markup.
- `q` (query, string, optional) — Optional filter expression as per filtering and sorting.
- `sort` (query, string, optional) — Optional sorting parameter as per filtering and sorting.
- `max_depth` (query, string, optional) — If provided, returns the contents of the repository and its subdirectories recursively until the specified maxdepth of nested directories. When omitted, this defaults to 1.

## Original description

This endpoints is used to retrieve the contents of a single file,
or the contents of a directory at a specified revision.

#### Raw file contents

When `path` points to a file, this endpoint returns the raw contents.
The response's Content-Type is derived from the filename
extension (not from the contents). The file contents are not processed
and no character encoding/recoding is performed and as a result no
character encoding is included as part of the Content-Type.

The `Content-Disposition` header will be "attachment" to prevent
browsers from running executable files.

If the file is managed by LFS, then a 301 redirect pointing to
Atlassian's media services platform is returned.

The response includes an ETag that is based on the contents of the file
and its attributes. This means that an empty `__init__.py` always
returns the same ETag, regardless on the directory it lives in, or the
commit it is on.

#### File meta data

When the request for a file path includes the query parameter
`?format=meta`, instead of returning the file's raw contents, Bitbucket
instead returns the JSON object describing the file's properties:

```javascript
$ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests/__init__.py?format=meta
{
  "links": {
    "self": {
      "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py"
    },
    "meta": {
      "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py?format=meta"
    }
  },
  "path": "tests/__init__.py",
  "commit": {
    "type": "commit",
    "hash": "eefd5ef5d3df01aed629f650959d6706d54cd335",
    "links": {
      "self": {
        "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335"
      },
      "html": {
        "href": "https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335"
      }
    }
  },
  "attributes": [],
  "type": "commit_file",
  "size": 0
}
```

File objects contain an `attributes` element that contains a list of
possible modifiers. Currently defined values are:

* `link` -- indicates that the entry is a symbolic link. The contents
    of the file represent the path the link points to.
* `executable` -- indicates that the file has the executable bit set.
* `subrepository` -- indicates that the entry points to a submodule or
    subrepo. The contents of the file is the SHA1 of the repository
    pointed to.
* `binary` -- indicates whether Bitbucket thinks the file is binary.

This endpoint can provide an alternative to how a HEAD request can be
used to check for the existence of a file, or a file's size without
incurring the overhead of receiving its full contents.


#### Directory listings

When `path` points to a directory instead of a file, the response is a
paginated list of directory and file objects in the same order as the
underlying SCM system would return them.

For example:

```javascript
$ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests
{
  "pagelen": 10,
  "values": [
    {
      "path": "tests/test_project",
      "type": "commit_directory",
      "links": {
        "self": {
          "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/"
        },
        "meta": {
          "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/?format=meta"
        }
      },
      "commit": {
        "type": "commit",
        "hash": "eefd5ef5d3df01aed629f650959d6706d54cd335",
        "links": {
          "self": {
            "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335"
          },
          "html": {
            "href": "https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335"
          }
        }
      }
    },
    {
      "links": {
        "self": {
          "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py"
        },
        "meta": {
          "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py?format=meta"
        }
      },
      "path": "tests/__init__.py",
      "commit": {
        "type": "commit",
        "hash": "eefd5ef5d3df01aed629f650959d6706d54cd335",
        "links": {
          "self": {
            "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335"
          },
          "html": {
            "href": "https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335"
          }
        }
      },
      "attributes": [],
      "type": "commit_file",
      "size": 0
    }
  ],
  "page": 1,
  "size": 2
}
```

When listing the contents of the repo's root directory, the use of a
trailing slash at the end of the URL is required.

The response by default is not recursive, meaning that only the direct contents of
a path are returned. The response does not recurse down into
subdirectories. In order to "walk" the entire directory tree, the
client can either parse each response and follow the `self` links of each
`commit_directory` object, or can specify a `max_depth` to recurse to.

The max_depth parameter will do a breadth-first search to return the contents of the subdirectories
up to the depth specified. Breadth-first search was chosen as it leads to the least amount of
file system operations for git. If the `max_depth` parameter is specified to be too
large, the call will time out and return a 555.

Each returned object is either a `commit_file`, or a `commit_directory`,
both of which contain a `path` element. This path is the absolute path
from the root of the repository. Each object also contains a `commit`
object which embeds the commit the file is on. Note that this is merely
the commit that was used in the URL. It is *not* the commit that last
modified the file.

Directory objects have 2 representations. Their `self` link returns the
paginated contents of the directory. The `meta` link on the other hand
returns the actual `directory` object itself, e.g.:

```javascript
{
  "path": "tests/test_project",
  "type": "commit_directory",
  "links": {
    "self": {
      "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/"
    },
    "meta": {
      "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/?format=meta"
    }
  },
  "commit": { ... }
}
```

#### Querying, filtering and sorting

Like most API endpoints, this API supports the Bitbucket
querying/filtering syntax and so you could filter a directory listing
to only include entries that match certain criteria. For instance, to
list all binary files over 1kb use the expression:

`size > 1024 and attributes = "binary"`

which after urlencoding yields the query string:

`?q=size%3E1024+and+attributes%3D%22binary%22`

To change the ordering of the response, use the `?sort` parameter:

`.../src/eefd5ef/?sort=-size`

See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more
details.

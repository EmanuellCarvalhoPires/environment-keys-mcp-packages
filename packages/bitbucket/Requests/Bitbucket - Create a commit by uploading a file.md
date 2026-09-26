---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/source
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/src"
category: "Source"
writes_data: true
tool_note: "[[bitbucket_create_a_commit_by_uploading_a_file]]"
---
# Bitbucket - Create a commit by uploading a file

**Create a commit by uploading a file** — `POST /repositories/{workspace}/{repo_slug}/src`

- Run by the tool [[bitbucket_create_a_commit_by_uploading_a_file]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/src?message={{param:message}}&author={{param:author}}&parents={{param:parents}}&files={{param:files}}&branch={{param:branch}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `message` (query, string, optional) — The commit message. When omitted, Bitbucket uses a canned string.
- `author` (query, string, optional) — The raw string to be used as the new commit's author. This string follows the format Erik van Zijst .
- `parents` (query, string, optional) — Deprecation Notice: Support for specifying multiple parent commits is deprecated and will be removed in a future release. Only a single SHA1 is accepted.
- `files` (query, string, optional) — Optional field that declares the files that the request is manipulating. When adding a new file to a repo, or when overwriting an existing file, the client can just upload the full contents of the fil…
- `branch` (query, string, optional) — The name of the branch that the new commit should be created on. When omitted, the commit will be created on top of the main branch and will become the main branch's new head.

## Original description

This endpoint is used to create new commits in the repository by
uploading files.

To add a new file to a repository:

```
$ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
  -F /repo/path/to/image.png=@image.png
```

This will create a new commit on top of the main branch, inheriting the
contents of the main branch, but adding (or overwriting) the
`image.png` file to the repository in the `/repo/path/to` directory.

To create a commit that deletes files, use the `files` parameter:

```
$ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
  -F files=/file/to/delete/1.txt \
  -F files=/file/to/delete/2.txt
```

You can add/modify/delete multiple files in a request. Rename/move a
file by deleting the old path and adding the content at the new path.

This endpoint accepts `multipart/form-data` (as in the examples above),
as well as `application/x-www-form-urlencoded`.

Note: `multipart/form-data` is currently not supported by Forge apps
for this API.

#### multipart/form-data

A `multipart/form-data` post contains a series of "form fields" that
identify both the individual files that are being uploaded, as well as
additional, optional meta data.

Files are uploaded in file form fields (those that have a
`Content-Disposition` parameter) whose field names point to the remote
path in the repository where the file should be stored. Path field
names are always interpreted to be absolute from the root of the
repository, regardless whether the client uses a leading slash (as the
above `curl` example did).

File contents are treated as bytes and are not decoded as text.

The commit message, as well as other non-file meta data for the
request, is sent along as normal form field elements. Meta data fields
share the same namespace as the file objects. For `multipart/form-data`
bodies that should not lead to any ambiguity, as the
`Content-Disposition` header will contain the `filename` parameter to
distinguish between a file named "message" and the commit message field.

#### application/x-www-form-urlencoded

It is also possible to upload new files using a simple
`application/x-www-form-urlencoded` POST. This can be convenient when
uploading pure text files:

```
$ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src \
  --data-urlencode "/path/to/me.txt=Lorem ipsum." \
  --data-urlencode "message=Initial commit" \
  --data-urlencode "author=Erik van Zijst "
```

There could be a field name clash if a client were to upload a file
named "message", as this filename clashes with the meta data property
for the commit message. To avoid this and to upload files whose names
clash with the meta data properties, use a leading slash for the files,
e.g. `curl --data-urlencode "/message=file contents"`.

When an explicit slash is omitted for a file whose path matches that of
a meta data parameter, then it is interpreted as meta data, not as a
file.

#### Executables and links

While this API aims to facilitate the most common use cases, it is
possible to perform some more advanced operations like creating a new
symlink in the repository, or creating an executable file.

Files can be supplied with a `x-attributes` value in the
`Content-Disposition` header. For example, to upload an executable
file, as well as create a symlink from `README.txt` to `README`:

```
--===============1438169132528273974==
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-ID: "bin/shutdown.sh"
Content-Disposition: attachment; filename="shutdown.sh"; x-attributes:"executable"

#!/bin/sh
halt

--===============1438169132528273974==
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-ID: "/README.txt"
Content-Disposition: attachment; filename="README.txt"; x-attributes:"link"

README
--===============1438169132528273974==--
```

Links are files that contain the target path and have
`x-attributes:"link"` set.

When overwriting links with files, or vice versa, the newly uploaded
file determines both the new contents, as well as the attributes. That
means uploading a file without specifying `x-attributes="link"` will
create a regular file, even if the parent commit hosted a symlink at
the same path.

The same applies to executables. When modifying an existing executable
file, the form-data file element must include
`x-attributes="executable"` in order to preserve the executable status
of the file.

Note that this API does not support the creation or manipulation of
subrepos / submodules.

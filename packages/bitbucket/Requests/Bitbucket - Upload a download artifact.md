---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/downloads
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/downloads"
category: "Downloads"
writes_data: true
tool_note: "[[bitbucket_upload_a_download_artifact]]"
---
# Bitbucket - Upload a download artifact

**Upload a download artifact** — `POST /repositories/{workspace}/{repo_slug}/downloads`

- Run by the tool [[bitbucket_upload_a_download_artifact]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/downloads
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Upload new download artifacts.

To upload files, perform a `multipart/form-data` POST containing one
or more `files` fields:

    $ echo Hello World > hello.txt
    $ curl -s -u evzijst -X POST https://api.bitbucket.org/2.0/repositories/evzijst/git-tests/downloads -F files=@hello.txt

When a file is uploaded with the same name as an existing artifact,
then the existing file will be replaced.

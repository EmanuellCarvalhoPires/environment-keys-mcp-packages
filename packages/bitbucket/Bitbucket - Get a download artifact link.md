---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/downloads
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/downloads/{filename}"
category: "Downloads"
writes_data: false
tool_note: "[[bitbucket_get_a_download_artifact_link]]"
---
# Bitbucket - Get a download artifact link

**Get a download artifact link** — `GET /repositories/{workspace}/{repo_slug}/downloads/{filename}`

- Run by the tool [[bitbucket_get_a_download_artifact_link]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/downloads/{{param:filename}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `filename` (path, string, required) — Value of filename in the path.

## Original description

Return a redirect to the contents of a download artifact.

This endpoint returns the actual file contents and not the artifact's
metadata.

    $ curl -s -L https://api.bitbucket.org/2.0/repositories/evzijst/git-tests/downloads/hello.txt
    Hello World

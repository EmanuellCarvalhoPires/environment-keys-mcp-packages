---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/downloads
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/downloads"
category: "Downloads"
writes_data: false
tool_note: "[[bitbucket_list_download_artifacts]]"
---
# Bitbucket - List download artifacts

**List download artifacts** — `GET /repositories/{workspace}/{repo_slug}/downloads`

- Run by the tool [[bitbucket_list_download_artifacts]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/downloads
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Returns a list of download links associated with the repository.

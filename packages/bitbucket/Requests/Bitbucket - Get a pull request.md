---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_get_a_pull_request]]"
---
# Bitbucket - Get a pull request

**Get a pull request** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}`

- Run by the tool [[bitbucket_get_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Returns the specified pull request.

---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_merge_a_pull_request]]"
---
# Bitbucket - Merge a pull request

**Merge a pull request** — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge`

- Run by the tool [[bitbucket_merge_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/merge?async={{param:async}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.
- `async` (query, string, optional) — Default value is false. When set to true, runs merge asynchronously and immediately returns a 202 with polling link to the task-status API in the Location header.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Merges the pull request.

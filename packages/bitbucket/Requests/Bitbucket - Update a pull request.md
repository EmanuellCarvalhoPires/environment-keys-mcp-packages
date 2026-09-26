---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_update_a_pull_request]]"
---
# Bitbucket - Update a pull request

**Update a pull request** — `PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}`

- Run by the tool [[bitbucket_update_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Mutates the specified pull request.

This can be used to change the pull request's branches or description.

Only open pull requests can be mutated.

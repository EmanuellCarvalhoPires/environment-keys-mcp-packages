---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_create_a_comment_on_a_pull_request]]"
---
# Bitbucket - Create a comment on a pull request

**Create a comment on a pull request** — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments`

- Run by the tool [[bitbucket_create_a_comment_on_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/comments
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new pull request comment.

Returns the newly created pull request comment.

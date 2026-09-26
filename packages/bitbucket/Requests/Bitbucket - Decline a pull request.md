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
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_decline_a_pull_request]]"
---
# Bitbucket - Decline a pull request

**Decline a pull request** — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline`

- Run by the tool [[bitbucket_decline_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/decline
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Declines the pull request.

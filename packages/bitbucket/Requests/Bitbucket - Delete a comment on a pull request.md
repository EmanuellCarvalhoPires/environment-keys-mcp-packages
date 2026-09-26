---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}"
category: "Pullrequests"
writes_data: true
tool_note: "[[bitbucket_delete_a_comment_on_a_pull_request]]"
---
# Bitbucket - Delete a comment on a pull request

**Delete a comment on a pull request** — `DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}`

- Run by the tool [[bitbucket_delete_a_comment_on_a_pull_request]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/comments/{{param:comment_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.
- `comment_id` (path, string, required) — Value of commentid in the path.

## Original description

Deletes a specific pull request comment.

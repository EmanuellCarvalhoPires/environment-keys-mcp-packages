---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/operations
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/operations/1.0/post-incident-reviews/{reviewId}"
category: "Operations"
writes_data: true
---
# JSW - Delete a Review by ID

**Delete a Review by ID** — `DELETE /rest/operations/1.0/post-incident-reviews/{reviewId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete a Review by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/operations/1.0/post-incident-reviews/{{param:reviewId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `reviewId` (path, string, required) — The ID of the Review to delete.

## Original description

Delete the Review data currently stored for the given ID.

Deletion is performed asynchronously. The getReviewById operation can be used to confirm that data has been deleted successfully (if needed).

Only Connect apps that define the `jiraOperationsInfoProvider` module can access this resource.
This resource requires the 'DELETE' scope for Connect apps.

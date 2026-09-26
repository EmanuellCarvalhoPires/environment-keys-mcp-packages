---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/development-information
  - api/operation/get
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/devinfo/0.10/repository/{repositoryId}"
category: "Development Information"
writes_data: false
---
# JSW - Get repository

**Get repository** — `GET /rest/devinfo/0.10/repository/{repositoryId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get repository"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/devinfo/0.10/repository/{{param:repositoryId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repositoryId` (path, string, required) — The ID of repository to fetch

## Original description

For the specified repository ID, retrieves the repository and the most recent 400 development information entities. The result will be what is currently stored, ignoring any pending updates or deletes.

---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/devops-components
  - api/operation/get
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/devopscomponents/1.0/devopscomponents/{componentId}"
category: "DevOps Components"
writes_data: false
---
# JSW - Get a Component by ID

**Get a Component by ID** — `GET /rest/devopscomponents/1.0/devopscomponents/{componentId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get a Component by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/devopscomponents/1.0/devopscomponents/{{param:componentId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `componentId` (path, string, required) — The ID of the Component to fetch.

## Original description

Retrieve the currently stored Component data for the given ID.

The result will be what is currently stored, ignoring any pending updates or deletes.

Only Connect apps that define the `jiraDevOpsComponentProvider` module can access this resource.
This resource requires the 'READ' scope for Connect apps.

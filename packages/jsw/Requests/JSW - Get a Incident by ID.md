---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/operations
  - api/operation/get
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/operations/1.0/incidents/{incidentId}"
category: "Operations"
writes_data: false
---
# JSW - Get a Incident by ID

**Get a Incident by ID** — `GET /rest/operations/1.0/incidents/{incidentId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get a Incident by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/operations/1.0/incidents/{{param:incidentId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `incidentId` (path, string, required) — The ID of the Incident to fetch.

## Original description

Retrieve the currently stored Incident data for the given ID.

The result will be what is currently stored, ignoring any pending updates or deletes.

Only Connect apps that define the `jiraOperationsInfoProvider` module can access this resource.
This resource requires the 'READ' scope for Connect apps.

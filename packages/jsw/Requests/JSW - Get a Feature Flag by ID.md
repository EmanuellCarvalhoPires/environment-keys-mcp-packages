---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/feature-flags
  - api/operation/get
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/featureflags/0.1/flag/{featureFlagId}"
category: "Feature Flags"
writes_data: false
---
# JSW - Get a Feature Flag by ID

**Get a Feature Flag by ID** — `GET /rest/featureflags/0.1/flag/{featureFlagId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get a Feature Flag by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/featureflags/0.1/flag/{{param:featureFlagId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `featureFlagId` (path, string, required) — The ID of the Feature Flag to fetch.

## Original description

Retrieve the currently stored Feature Flag data for the given ID.

The result will be what is currently stored, ignoring any pending updates or deletes.

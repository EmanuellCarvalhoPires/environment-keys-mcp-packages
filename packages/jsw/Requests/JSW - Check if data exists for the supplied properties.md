---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/development-information
  - api/operation/list
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/devinfo/0.10/existsByProperties"
category: "Development Information"
writes_data: false
---
# JSW - Check if data exists for the supplied properties

**Check if data exists for the supplied properties** — `GET /rest/devinfo/0.10/existsByProperties`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Check if data exists for the supplied properties"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/devinfo/0.10/existsByProperties?_updateSequenceId={{param:_updateSequenceId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `_updateSequenceId` (query, string, optional) — An optional property. Filters out entities and repositories which have updateSequenceId greater than specified.

## Original description

Checks if repositories which have all the provided properties exists. For example, if request is `GET existsByProperties?accountId=123&projectId=ABC` then result will be positive only if there is at least one repository with both properties `accountId=123` and `projectId=ABC`. Special property `_updateSequenceId` can be used to filter all entities with updateSequenceId less or equal than the value specified. In addition to the optional `_updateSequenceId`, one or more query params must be supplied to specify properties to search by.

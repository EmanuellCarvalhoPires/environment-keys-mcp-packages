---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/devops-components
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/devopscomponents/1.0/bulk"
category: "DevOps Components"
writes_data: true
---
# JSW - Submit DevOps Components

**Submit DevOps Components** — `POST /rest/devopscomponents/1.0/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Submit DevOps Components"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/devopscomponents/1.0/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update / insert DevOps Component data.

Components are identified by their ID, and existing Component data for the same ID will be replaced if it exists and the updateSequenceNumber of existing data is less than the incoming data.

Submissions are performed asynchronously. Submitted data will eventually be available in Jira; most updates are available within a short period of time, but may take some time during peak load and/or maintenance times. The getComponentById operation can be used to confirm that data has been stored successfully (if needed).

In the case of multiple Components being submitted in one request, each is validated individually prior to submission. Details of which Components failed submission (if any) are available in the response object.

A maximum of 1000 components can be submitted in one request.

Only Connect apps that define the `jiraDevOpsComponentProvider` module can access this resource.
This resource requires the 'WRITE' scope for Connect apps.

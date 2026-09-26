---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/usage
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/usage"
category: "Usage"
writes_data: false
tool_note: "[[assets_get_tenant_usage_information]]"
---
# Assets - Get tenant usage information

**Get tenant usage information** — `GET /usage`

- Run by the tool [[assets_get_tenant_usage_information]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/usage
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Retrieves comprehensive usage statistics for the current tenant including total object counts and a per-schema breakdown for billing and analytics.

---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/pipelines-config/identity/oidc/keys.json"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_keys_for_oidc_in_pipelines]]"
---
# Bitbucket - Get keys for OIDC in Pipelines

**Get keys for OIDC in Pipelines** — `GET /workspaces/{workspace}/pipelines-config/identity/oidc/keys.json`

- Run by the tool [[bitbucket_get_keys_for_oidc_in_pipelines]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/identity/oidc/keys.json
Authorization: {{service.auth_token}}
```

## Original description

This is part of OpenID Connect for Pipelines, see https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/

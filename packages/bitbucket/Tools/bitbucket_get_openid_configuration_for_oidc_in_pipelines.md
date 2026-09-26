---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_openid_configuration_for_oidc_in_pipelines
title: "Bitbucket - Get OpenID configuration for OIDC in Pipelines"
kind: request
request: "[[Bitbucket - Get OpenID configuration for OIDC in Pipelines]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration · Get OpenID configuration for OIDC in Pipelines. This is part of OpenID Connect for Pipelines, see https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/ Writes data: no."
writes: false
expose: false
---
# bitbucket_get_openid_configuration_for_oidc_in_pipelines

`GET /workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration` — Get OpenID configuration for OIDC in Pipelines

- Request: [[Bitbucket - Get OpenID configuration for OIDC in Pipelines]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
